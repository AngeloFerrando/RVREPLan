from connectors import *
from mappers import *
from data.action import *
from data.snapshot import *
from os.path import exists
import sys
import time
import os
import argparse
import importlib

def main(args):
    global actions, DEJAVU_PATH, connector, snapshot, PLANNER_PATH, DOMAIN_FILE, PROBLEM_FILE, initial_planning_time, replanning_time, replanning_calls, avg_size_replanning_plans, errors_to_inject
    parser = argparse.ArgumentParser(
        description='RvEPlan python implementation',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('domain_file', # needed to synthesise the failure handling monitor
        help='PDDL domain file (describing the actions preconditions and effects)',
        type=str)
    parser.add_argument('problem_file', # needed to generate the initial snapshot (and maybe in the future the instantiated failure monitor)
        help='PDDL problem file (describing the initial system setup and goals)',
        type=str)
    parser.add_argument('connector', # what is going to be executed on the system
        help='The connector (the component that connects the tool with the actual system)',
        type=str)
    parser.add_argument('dejavu_path', # needed to compile and execute the failure handling monitor
        help='Path to Dejavu folder (the one containing dejavu.jar)',
        type=str)
    parser.add_argument('planner_path', # needed to (re)plan
        help='Path to the planner of choice including any flags it may use (e.g.: "/.../fast-downward.sif --alias seq-opt-lmcut")',
        type=str)
    parser.add_argument('-no_monitor_synthesis', '--no_monitor_synthesis', action='store_true',
        help='if added the monitor will not be generated (it is assumed has already been generated in previous run)')
    parser.add_argument('-inject_errors', '--inject_errors', type=int,
        help='number of errors to inject')
    args = parser.parse_args() # maybe in the future we will need more arguments, for now it's just one

    replanning_calls = 0
    avg_size_replanning_plans = 0
    replanning_time = 0
    if args.inject_errors:
        errors_to_inject = args.inject_errors
    else:
        errors_to_inject = 0

    # setup instructions
    os.system('rm ./out/*.csv')
    DEJAVU_PATH = args.dejavu_path
    PLANNER_PATH = args.planner_path
    DOMAIN_FILE = args.domain_file
    PROBLEM_FILE = args.problem_file
    CONNECTOR_MODULE = importlib.import_module(args.connector)

    start = time.time()
    # Generation of the plan (given the Domain and Problem PDDL files)
    os.system(PLANNER_PATH + ' ' + args.domain_file + ' ' + args.problem_file)
    initial_planning_time = time.time() - start
    
    # Translation from PDDL to Failure handling monitor (RVPlan paper)
    if not args.no_monitor_synthesis:
        os.system('python3 translators/translator.py ' + args.domain_file)
        os.system('java -cp ' + DEJAVU_PATH + '/dejavu.jar dejavu.Verify ./out/prop.qtl | grep -v "Elapsed total"')
        os.system('scalac -cp .:' + DEJAVU_PATH + '/dejavu.jar TraceMonitor.scala 2>&1 | grep -v "warning"')

    # Create snapshot
    # createSnapshot(args.problem_file)

    snapshot = Snapshot(args.problem_file)

    # Connector instantiation
    # connector = JsonConnector() # Domain dependent: With another system, we may use another connector
    # connector = raw_connector_logistics.RawConnectorLogistics(raw_mapper.RawMapper())
    # connector = raw_connector_depot.RawConnectorDepot(raw_mapper.RawMapper())
    # connector = raw_connector_satellite.RawConnectorRover(raw_mapper.RawMapper())
    connector = CONNECTOR_MODULE.CONNECTOR
    connector.set_errors_to_inject(errors_to_inject)
    if not exists('./sas_plan'):
        print('No plan found, stop execution')
        return
    with open('./sas_plan', 'r') as plan:
        actions = plan.readlines()
        actions = actions[:-1]
    # initial_propositions = connector.get_initial_propositions()
    # here I am setting the initial propositions to the same ones used in the Problem file
    # however, in general, the initial propositions should come from the system
    snapshot.update(connector.get_initial_propositions())
    initial_propositions = set(snapshot.get_props())
    callbackNewProps(initial_propositions)

def callbackNewProps(props):
    # print(props)
    if props:
        # Update the snapshot
        snapshot.update(props)
    monitor_outcome = '0 errors detected!'
    if not actions:
        # os.system('rm *.class')
        print(snapshot)
        log_metrics()
        return
    action = Action.fromStrToAction(actions.pop(0))
    print(action)
    with open('./out/trace.csv', 'a') as monitor_input:
        if props:
            # update the failure handling monitor
            for prop in props:
                monitor_input.write(str(prop) + '\n')
        monitor_input.write(str(action))
    monitor_outcome = os.popen('scala -J-Xmx32g -cp .:' + DEJAVU_PATH + '/dejavu.jar TraceMonitor ./out/trace.csv 20  2>&1  | grep -v "Resizing" | grep -v "load BDD package" | grep -v "Garbage collection"').read()
    print(monitor_outcome)
    if '0 errors detected!' not in monitor_outcome:
        with open('./out/trace.csv') as monitor_input:
            lines = monitor_input.readlines()
        with open('./out/trace.csv', 'w') as monitor_input:
            monitor_input.writelines(lines[:-1])
        # connector.set_time_to_fail(True)
        replan() # replan
    else:
        connector.perform(action, callbackNewProps)

def replan():
    global actions, replanning_time, replanning_calls, avg_size_replanning_plans
    replanning_calls += 1
    start = time.time()
    # Creation of the newly updated problem file (starting from the snapshot)
    with open('./out/updated_problem.pddl', 'w') as updated_problem_file:
        with open(PROBLEM_FILE, 'r') as old_problem_file:
            instructions = old_problem_file.readlines()
            for instruction in instructions:
                if '(:init' in instruction:
                    index = instruction.index('(:init')
                    updated_problem_file.write(instruction[:index])
                    break
                else:
                    updated_problem_file.write(instruction)
            updated_problem_file.write(str(snapshot) + '\n)')
    # Generation of a new plan (given the Domain and the updated Problem PDDL files)
    os.system(PLANNER_PATH + ' ' + DOMAIN_FILE + ' ' + './out/updated_problem.pddl')
    if not exists('./sas_plan'):
        print('No plan found, stop execution')
        return
    with open('./sas_plan', 'r') as plan:
        actions = plan.readlines()
        actions = actions[:-1]
    avg_size_replanning_plans += len(actions)
    replanning_time += time.time() - start
    props = connector.get_errors()
    callbackNewProps(props)

def log_metrics():
    # (initial solution planning time,  replanning time, total plan size of executed actions, replanning calls, average size of replanning plans)
    with open('./res_'+ str(errors_to_inject) +'.csv', 'a') as f:
        f.write(str(initial_planning_time) + ';')
        f.write(str(replanning_time) + ';')
        f.write(str(connector.get_actions_executed()) + ';')
        f.write(str(replanning_calls) + ';')
        if replanning_calls == 0:
            f.write(str(0) + '\n')
        else:
            f.write(str(avg_size_replanning_plans/replanning_calls) + '\n')

if __name__ == '__main__':
    main(sys.argv)
