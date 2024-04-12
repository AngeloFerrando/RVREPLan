from connectors import *
from connectors.abstract_connector import ResultCode
from mappers import *
from data.action import *
from data.snapshot import *
from os.path import exists
import sys
import time
import os
import argparse
import importlib
import copy
import shutil

def main(args):
    global actions, DEJAVU_PATH, connector, snapshot, PLANNER_PATH, DOMAIN_FILE, PROBLEM_FILE, initial_planning_time, replanning_time, replanning_calls, avg_size_replanning_plans, update_monitor_time, simulation_time, errors_to_inject, dict_pre_eff, counter, counter_store_plans, past_actions, simulating, simulation_violations, GLOBAL_PATH
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
    counter = 0
    counter_store_plans = 1
    avg_size_replanning_plans = 0
    replanning_time = 0
    update_monitor_time = 0
    simulation_time = 0
    simulation_violations = []
    if args.inject_errors:
        errors_to_inject = args.inject_errors
        if errors_to_inject < 0:
            errors_to_inject = 0
        if errors_to_inject > 3:
            errors_to_inject = 3
    else:
        errors_to_inject = 0

    simulating = False

    if os.path.exists('./abstract_system.py'):
        GLOBAL_PATH = os.path.dirname('./abstract_system.py') + '/'
    elif os.path.exists('../../../abstract_system.py'):
        GLOBAL_PATH = os.path.dirname('../../../abstract_system.py') + '/'
    else:
        print('I cannot find the path to the abstract_system.py script. Please, be sure to run the script either in the folder that contains abstract_system.py, or through the experiments.sh shell script.')
        return


    # checking if the temporary directory out exists or not. 
    if not os.path.exists(GLOBAL_PATH + './out/'):   
        # if the out directory is not present, then create it. 
        os.makedirs(GLOBAL_PATH + './out/')
        os.makedirs(GLOBAL_PATH + './out/pre/')
        os.makedirs(GLOBAL_PATH + './out/eff/') 

    # setup instructions
    os.system('rm ' + GLOBAL_PATH + './out/*.csv')
    DEJAVU_PATH = args.dejavu_path
    PLANNER_PATH = args.planner_path
    DOMAIN_FILE = args.domain_file
    PROBLEM_FILE = args.problem_file
    CONNECTOR_MODULE = importlib.import_module(args.connector)

    start = time.time()
    # Generation of the plan (given the Domain and Problem PDDL files)
    os.system(PLANNER_PATH + ' ' + args.domain_file + ' ' + args.problem_file)
    initial_planning_time = time.time() - start

    with open(GLOBAL_PATH + './out/log', 'w') as file:
        file.write('')        
    
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
    
    os.system('rm ./plans/*')
    store_plans() # store the plans for plan stability evaluation
    
    with open('./sas_plan', 'r') as plan:
        actions = plan.readlines()
        actions = actions[:-1]

    # Translation from PDDL to Failure handling monitor (RVPlan paper)
    if not args.no_monitor_synthesis:
        # synthesise_decentralised_monitors(args.domain_file, None)
        synthesise_centralised_monitor(args.domain_file, './sas_plan', None)
    
    # initial_propositions = connector.get_initial_propositions()
    # here I am setting the initial propositions to the same ones used in the Problem file
    # however, in general, the initial propositions should come from the system
    snapshot.update(connector.get_initial_propositions())
    initial_propositions = set(snapshot.get_props())
    past_actions = []
    callbackNewProps(None, initial_propositions)

prev_action = None
def callbackNewProps(RESULTCODE, props):
    global prev_action, counter, counter_store_plans
    counter += 1
    if not simulating: counter_store_plans += 1

    # check whether the previous action failed
    if RESULTCODE == ResultCode.FAILURE:
        log('FAILURE', counter, connector._case-1, prev_action, set())
        with open(GLOBAL_PATH + './out/log', 'r') as file: 
            log_lines = file.readlines()
        actions_to_modify = {}
        log_lines = [line for line in log_lines if 'DIFF_PRE' in line]
        for i in range(len(log_lines)-1, -1, -1):
            log_line = log_lines[i]
            # print(log_line)
            act = 'begin_' + log_line.split(' ')[3]
            # print(act)
            if log_line.split(' ')[3] == str(prev_action).replace('begin_', '').replace('end_', ''):
                log_line = log_line.split(' ')[4].replace('{', '').replace('}', '').replace('\',\'', ';').replace('\'', '').split(';')
                # print(log_line)
                for issue in log_line:
                    if act not in actions_to_modify:
                        actions_to_modify[act] = set()
                    actions_to_modify[act].add(issue)
                issues = actions_to_modify[act]
                break
        if len(actions_to_modify.keys()) == 0:
            replan()
            return
        else:
            aux_dict_pre_eff = update_monitors(actions_to_modify, 0)
            for act in aux_dict_pre_eff:
                dict_pre_eff[act] = aux_dict_pre_eff[act]
            with open(GLOBAL_PATH + './out/dict_pre_eff_new.json', 'w') as file:
                json.dump(dict_pre_eff, file)
            new_domain_file_name = DOMAIN_FILE
            if not DOMAIN_FILE.endswith('_1.pddl'):
                new_domain_file_name = DOMAIN_FILE.replace('.pddl', '_1.pddl')
            os.system('python3 ' + GLOBAL_PATH + 'translators/translator.py ' + DOMAIN_FILE + ' ' + new_domain_file_name + ' ' + GLOBAL_PATH + './out/dict_pre_eff_new.json')
            if not DOMAIN_FILE.endswith('_1.pddl'):
                DOMAIN_FILE = new_domain_file_name
            replan()
            # if not aux_dict_pre_eff:
            #     replan()
            #     pass
            # props_to_add = set()
            # for i in issues:
            #     if i.split(',')[0].startswith('not_'):
            #         props_to_add.add(Proposition(False, i.split(',')[0][4:], i.split(',')[1:]))
            #     else:
            #         props_to_add.add(Proposition(True, i.split(',')[0], i.split(',')[1:]))
            # if not simulate([k.split(',')[0] for k in actions_to_modify.keys()], props_to_add, aux_dict_pre_eff, prev_action):
            #     return
    # check props against effects of previous action to check whether additional propositions are in props, but not in the effects
    if prev_action:
        past_actions.append(prev_action)
        _, issues = detect_issue('end_', prev_action, props)
        if issues:
            log('DIFF_POST', counter, connector._case-1, prev_action, issues)

    # print(props)
    if props:
        # Update the snapshot
        snapshot.update(props)
    monitor_outcome_pre = '0 errors detected!'
    monitor_outcome_eff = '0 errors detected!'
    if not actions:
        # os.system('rm *.class')
        print(snapshot)
        log_metrics()
        return
    act_str = actions.pop(0)
    action = Action.fromStrToAction(act_str)
    print(action)
    _, issues = detect_issue('begin_', action, props)
    if issues:
        log('DIFF_PRE', counter, connector._case, action, issues)
    to_remove = -1
    with open(GLOBAL_PATH + './out/trace.csv', 'a') as monitor_input:
        if props:
            # update the failure handling monitor
            for prop in props:
                monitor_input.write(str(prop) + '\n')
        monitor_input.write('begin_' + str(action))
        if prev_action:
            to_remove = -2
            monitor_input.write('end_' + str(prev_action))
    current_path = os.getcwd()
    # os.chdir(GLOBAL_PATH + './out/pre/' + str(action).split(',')[0])
    os.chdir(GLOBAL_PATH + './out/pre/')
    monitor_outcome_pre = os.popen('scala -J-Xmx32g -cp .:' + DEJAVU_PATH + '/dejavu.jar TraceMonitor ../trace.csv 20  2>&1  | grep -v "Resizing" | grep -v "load BDD package" | grep -v "Garbage collection"').read()
    os.chdir(current_path)
    # POST CONDITIONS MONITOR STUFF
    if prev_action:
        # os.chdir(GLOBAL_PATH + './out/eff/' + str(prev_action).split(',')[0])
        os.chdir(GLOBAL_PATH + './out/eff/')
        monitor_outcome_eff = os.popen('scala -J-Xmx32g -cp .:' + DEJAVU_PATH + '/dejavu.jar TraceMonitor ../trace.csv 20  2>&1  | grep -v "Resizing" | grep -v "load BDD package" | grep -v "Garbage collection"').read()
        os.chdir(current_path)
    if '0 errors detected!' not in monitor_outcome_eff:
        print(monitor_outcome_eff)
        # TRIGGER to LOG [A postcondition is violated]
        issues, _ = detect_issue('end_', prev_action, snapshot.get_props())
        issues_backup = copy.deepcopy(issues)
        log('POST', counter, connector._case-1, prev_action, issues)

        with open(GLOBAL_PATH + './out/log', 'r') as file: 
            log_lines = file.readlines()
        actions_to_modify = {}

        (params, cond) = dict_pre_eff['end_' + prev_action._functor]
        actions_to_modify['end_'+str(prev_action).replace('\n', '')] = set()
        for c in cond:
            add = True
            for issue in issues:
                if c[:c.index('(')].replace('!', 'not_') == issue[:issue.index(',')]:
                    add = False
            if add:
                actions_to_modify['end_'+str(prev_action).replace('\n', '')].add(c.replace('(', ',').replace(')', ''))

        log_lines = [line for line in log_lines if 'DIFF_PRE' in line]
        for i in range(len(log_lines)-1, -1, -1):
            log_line = log_lines[i]
            # print(log_line)
            act = 'begin_' + log_line.split(' ')[3]
            # print(act)
            log_line = log_line.split(' ')[4].replace('{', '').replace('}', '').replace('\',\'', ';').replace('\'', '').split(';')
            # print(log_line)
            issues_to_remove = set()
            for issue in issues:
                aux = issue
                # if 'not_' in issue:
                #     issue = issue[4:]
                # else:
                #     issue = 'not_' + issue
                if issue in log_line:
                    add = False
                    for future_action in actions:
                        if future_action._functor == act[6:]:
                            add = True
                            break
                    if add:
                        if act not in actions_to_modify:
                            actions_to_modify[act] = set()
                        actions_to_modify[act].add(issue)
                        issues_to_remove.add(aux)
            issues.difference_update(issues_to_remove)
            if not issues:
                break
        with open(GLOBAL_PATH + './out/trace.csv') as monitor_input:
            lines = monitor_input.readlines()
        with open(GLOBAL_PATH + './out/trace.csv', 'w') as monitor_input:
            monitor_input.writelines(lines[:-1])
            to_remove = -1
        run_simulation = True
        if len(actions_to_modify.keys()) == 1: # no DIFF_PRE in the past (whose action is also used in the future) uses propositions missing in the POST 
            violate_future_action = False
            for future_action in actions:
                cond, _ = get_instantiated_pre_eff_action('begin_', Action.fromStrToAction(future_action))
                if issues_backup.intersection(cond):
                    violate_future_action = True
                    break
            cond = set([str(c).replace('(', ',').replace(')', '').replace(' ', '').replace('!','not_') for c in snapshot._goals])
            if not violate_future_action and not issues_backup.intersection(cond):
                run_simulation = False
        if run_simulation:
            aux_dict_pre_eff = update_monitors(actions_to_modify, 0)
            # at this point, we should have a new version of the monitors related to the updated actions
            # run simulation with monitors 
            if not simulate([k.split(',')[0] for k in actions_to_modify.keys()], set(), aux_dict_pre_eff, act_str):
                return
            # if errors is reported by monitors so modified, then delete prop.qtl and rename prop_old.qtl to prop.qtl, then replan
            # otherwise, if error is reported by other monitors, then remove prop_old.qtl, then replan
            # otherwise, remove prop_old.qtl and keep running            
    # PRE CONDITIONS MONITOR STUFF
    if '0 errors detected!' not in monitor_outcome_pre:
        print(monitor_outcome_pre)
        # TRIGGER to LOG [A precondition is violated]
        issues, _ = detect_issue('begin_', action, snapshot.get_props())
        log('PRE', counter, connector._case, action, issues)
        props_to_add = set()
        for i in issues:
            if i.split(',')[0].startswith('not_'):
                props_to_add.add(Proposition(False, i.split(',')[0][4:], i.split(',')[1:]))
            else:
                props_to_add.add(Proposition(True, i.split(',')[0], i.split(',')[1:]))
        with open(GLOBAL_PATH + './out/log', 'r') as file: 
            log_lines = file.readlines()
        actions_to_modify = {}

        # (params, cond) = dict_pre_eff['begin_' + action._functor]
        # actions_to_modify['begin_'+str(action).replace('\n', '')] = set()
        # for c in cond:
        #     add = True
        #     for issue in issues:
        #         if c[:c.index('(')].replace('!', 'not_') == issue[:issue.index(',')]:
        #             add = False
        #     if add:
        #         actions_to_modify['begin_'+str(action).replace('\n', '')].add(c.replace('(', ',').replace(')', ''))

        log_lines = [line for line in log_lines if 'DIFF_POST' in line]
        for i in range(len(log_lines)-1, -1, -1):
            log_line = log_lines[i]
            # print(log_line)
            act = 'end_' + log_line.split(' ')[3]
            # print(act)
            log_line = log_line.split(' ')[4].replace('{', '').replace('}', '').replace('\',\'', ';').replace('\'', '').split(';')
            # print(log_line)
            issues_to_remove = set()
            for issue in issues:
                aux = issue
                if 'not_' in issue:
                    issue = issue[4:]
                else:
                    issue = 'not_' + issue
                if issue in log_line:
                    if act not in actions_to_modify:
                        actions_to_modify[act] = set()
                    actions_to_modify[act].add(issue)
                    issues_to_remove.add(aux)
            issues.difference_update(issues_to_remove)
            if not issues:
                break
        with open(GLOBAL_PATH + './out/trace.csv') as monitor_input:
            lines = monitor_input.readlines()
        with open(GLOBAL_PATH + './out/trace.csv', 'w') as monitor_input:
            monitor_input.writelines(lines[:to_remove])
        if issues:
            replan() # but where we enforce to create a new plan
        else:
            aux_dict_pre_eff = update_monitors(actions_to_modify, 1)
            # at this point, we should have a new version of the monitors related to the updated actions
            # run simulation with monitors 
            backup_prev_action = prev_action
            prev_action = None
            actions.insert(0, act_str)
            if simulate([k.split(',')[0] for k in actions_to_modify.keys()], props_to_add, aux_dict_pre_eff, act_str):
                prev_action = backup_prev_action
                connector.perform(action, callbackNewProps)
            # if errors is reported by monitors so modified, then delete prop.qtl and rename prop_old.qtl to prop.qtl, then replan
            # otherwise, if error is reported by other monitors, then remove prop_old.qtl, then replan
            # otherwise, remove prop_old.qtl and keep running            
    else:
        prev_action = action
        connector.perform(action, callbackNewProps)

def update_monitors(actions_to_modify, kind):
    global update_monitor_time
    aux_dict_pre_eff = {}
    for act in actions_to_modify:
        prefix = 'begin_' if act.startswith('begin_') else 'end_'
        act1 = act.replace(prefix, '')
        issues = actions_to_modify[act]
        issues = list(issues)
        (params, cond) = dict_pre_eff[prefix + act1.split(',')[0]]
        
        if (prefix == 'end_' and kind == 1) or (prefix == 'begin_' and kind == 0):
            _, paramsMap = get_instantiated_pre_eff_action(prefix, Action(act1.split(',')[0], act1.split(',')[1:]))
            for param in paramsMap:
                for i in range(0, len(issues)): 
                    if paramsMap[param] in issues[i]:
                        issues[i] = issues[i].replace(paramsMap[param], param)
            problem = False
            for i in issues:
                aux = i.split(',')
                for j in range(1, len(aux)):
                    if '?' not in aux[j]:
                        problem = True
            if not problem:
                for i in range(0, len(issues)):
                    aux = issues[i].split(',')
                    issues[i] = aux[0] + '(' + ','.join(aux[1:]) + ')'
                aux_dict_pre_eff[prefix + act1.split(',')[0]] = (params, list(set(cond).union(issues)))
                        # aux_dict_pre_eff['begin_' + act.split(',')[0]] = dict_pre_eff['begin_' + act.split(',')[0]]
        else:
            aux_dict_pre_eff[prefix + act1.split(',')[0]] = (params, list(issues))
    # for k in copy.deepcopy(aux_dict_pre_eff):
    for k in copy.deepcopy(dict_pre_eff):
        if 'begin_' in k:
            k = k.replace('begin_', 'end_')
        else:
            k = k.replace('end_', 'begin_')
        if k not in aux_dict_pre_eff:
            aux_dict_pre_eff[k] = dict_pre_eff[k]
    start = time.time()
    if len(aux_dict_pre_eff.keys()) != 0:
        with open(GLOBAL_PATH + './out/dict_pre_eff_new.json', 'w') as file:
            json.dump(aux_dict_pre_eff, file)
        os.system('python3 ' + GLOBAL_PATH + 'translators/translator.py ' + DOMAIN_FILE + ' ' + DOMAIN_FILE.replace('.pddl', '_new.pddl') + ' ' + GLOBAL_PATH + './out/dict_pre_eff_new.json')
        for act in actions_to_modify:
            prefix = 'begin_' if act.startswith('begin_') else 'end_'
            act = act.replace(prefix, '')
            if prefix == 'begin_':
                # if os.path.exists(GLOBAL_PATH + './out/pre/' + act.split(',')[0] + '/prop.qtl'):
                #     os.rename(GLOBAL_PATH + './out/pre/' + act.split(',')[0] + '/prop.qtl', GLOBAL_PATH + './out/pre/' + act.split(',')[0] + '/prop_old.qtl')
                os.rename(GLOBAL_PATH + './out/pre/prop.qtl', GLOBAL_PATH + './out/pre/prop_old.qtl')
            else:
                # if os.path.exists(GLOBAL_PATH + './out/eff/' + act.split(',')[0] + '/prop.qtl'):
                    # os.rename(GLOBAL_PATH + './out/eff/' + act.split(',')[0] + '/prop.qtl', GLOBAL_PATH + './out/eff/' + act.split(',')[0] + '/prop_old.qtl')
                os.rename(GLOBAL_PATH + './out/eff/prop.qtl', GLOBAL_PATH + './out/eff/prop_old.qtl')
        # synthesise_decentralised_monitors(DOMAIN_FILE.replace('.pddl', '_new.pddl'), aux_dict_pre_eff)
        synthesise_centralised_monitor(DOMAIN_FILE.replace('.pddl', '_new.pddl'), './sas_plan', aux_dict_pre_eff)
    update_monitor_time += time.time() - start
    return aux_dict_pre_eff

def simulate(modified_actions, props_to_add, aux_dict_pre_eff, action):
    global simulating, snapshot, actions, connector, DOMAIN_FILE, simulation_time, simulation_violations
    simulating = True
    snapshot_backup = copy.deepcopy(snapshot)
    case_backup = connector._case
    actions_backup = copy.deepcopy(actions)
    actions_backup.insert(0, action)
    start = time.time()
    with open(GLOBAL_PATH + './out/trace.csv', 'r') as file:
        trace_backup = file.read()
    e = ''
    try:
        callbackNewProps(None, props_to_add)
    except Exception as ex:
        e = str(ex)
    simulation_violations.append(e.replace('begin_', 'PRE_').replace('end_', 'POST_'))
    e = e.replace('failure_', 'begin_')
    simulation_time += time.time() - start
    simulating = False
    snapshot = snapshot_backup
    connector._case = case_backup
    actions = actions_backup
    with open(GLOBAL_PATH + './out/trace.csv', 'w') as file:
        file.write(trace_backup)
    if e in modified_actions:
        for act in modified_actions:
            prefix = 'begin_' if act.startswith('begin_') else 'end_'
            act = act.replace(prefix, '')
            # if os.path.exists(GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/' + act + '/prop.qtl'):
            #     os.remove(GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/' + act + '/prop.qtl')
            os.remove(GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/prop.qtl')
            # if os.path.exists(GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/' + act + '/prop_old.qtl'):
            #     os.rename(GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/' + act + '/prop_old.qtl', GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/' + act + '/prop.qtl')
            os.rename(GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/prop_old.qtl', GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/prop.qtl')
            current_path = os.getcwd()
            os.chdir(GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/')
            os.system('java -cp ' + DEJAVU_PATH + '/dejavu.jar dejavu.Verify ./prop.qtl | grep -v "Elapsed total"')
            os.system('scalac -cp .:' + DEJAVU_PATH + '/dejavu.jar TraceMonitor.scala 2>&1 | grep -v "warning"')
            os.chdir(current_path)
        replan()
        return False
    elif e != '':
        for act in modified_actions:
            prefix = 'begin_' if act.startswith('begin_') else 'end_'
            act = act.replace(prefix, '')
            # if os.path.exists(GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/' + act + '/prop_old.qtl'):
            #     os.remove(GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/' + act + '/prop_old.qtl')   
            os.remove(GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/prop_old.qtl')   
        for act in aux_dict_pre_eff:
            dict_pre_eff[act] = aux_dict_pre_eff[act]
        with open(GLOBAL_PATH + './out/dict_pre_eff_new.json', 'w') as file:
            json.dump(dict_pre_eff, file)
        new_domain_file_name = DOMAIN_FILE
        if not DOMAIN_FILE.endswith('_1.pddl'):
            new_domain_file_name = DOMAIN_FILE.replace('.pddl', '_1.pddl')
        os.system('python3 ' + GLOBAL_PATH + 'translators/translator.py ' + DOMAIN_FILE + ' ' + new_domain_file_name + ' ' + GLOBAL_PATH + './out/dict_pre_eff_new.json')
        if not DOMAIN_FILE.endswith('_1.pddl'):
            DOMAIN_FILE = new_domain_file_name
        replan()
        return False
    else:
        for act in modified_actions:
            prefix = 'begin_' if act.startswith('begin_') else 'end_'
            act = act.replace(prefix, '')
            # if os.path.exists(GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/' + act + '/prop_old.qtl'):
            #     os.remove(GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/' + act + '/prop_old.qtl')   
            os.remove(GLOBAL_PATH + './out/' + ('pre' if prefix == 'begin_' else 'eff') + '/prop_old.qtl')   
        for act in aux_dict_pre_eff:
            dict_pre_eff[act] = aux_dict_pre_eff[act]
        with open(GLOBAL_PATH + './out/dict_pre_eff_new.json', 'w') as file:
            json.dump(dict_pre_eff, file)
        new_domain_file_name = DOMAIN_FILE
        if not DOMAIN_FILE.endswith('_1.pddl'):
            new_domain_file_name = DOMAIN_FILE.replace('.pddl', '_1.pddl')
        os.system('python3 ' + GLOBAL_PATH + 'translators/translator.py ' + DOMAIN_FILE + ' ' + new_domain_file_name + ' ' + GLOBAL_PATH + './out/dict_pre_eff_new.json')
        if not DOMAIN_FILE.endswith('_1.pddl'):
            DOMAIN_FILE = new_domain_file_name
        return True

# def synthesise_centralised_monitors(args):
#     os.system('python3 translators/translator.py ' + args.domain_file)
#     os.chdir('./out/pre/')
#     os.system('java -cp ' + DEJAVU_PATH + '/dejavu.jar dejavu.Verify ./prop.qtl | grep -v "Elapsed total"')
#     os.system('scalac -cp .:' + DEJAVU_PATH + '/dejavu.jar TraceMonitor.scala 2>&1 | grep -v "warning"')
#     os.chdir('../eff/')
#     os.system('java -cp ' + DEJAVU_PATH + '/dejavu.jar dejavu.Verify ./prop.qtl | grep -v "Elapsed total"')
#     os.system('scalac -cp .:' + DEJAVU_PATH + '/dejavu.jar TraceMonitor.scala 2>&1 | grep -v "warning"')
#     os.chdir('../../')

def synthesise_decentralised_monitors(domain_file, aux_dict_pre_eff):
    aux_dict_pre_eff = translate_fol(domain_file, aux_dict_pre_eff)
    with open(GLOBAL_PATH + './out/synthesised_properties', 'r') as file:
        synthesised_properties = file.read()
    synthesised_properties = synthesised_properties.replace(' ', '').replace('\'', '').replace('[', '').replace(']', '').split(',')
    print(synthesised_properties)
    current_path = os.getcwd()
    os.chdir(GLOBAL_PATH + './out/pre/')
    for action in aux_dict_pre_eff:
        if 'begin_' not in action: continue
        if action not in synthesised_properties: continue
        action = action[6:]
        os.chdir('./' + action)
        os.system('java -cp ' + DEJAVU_PATH + '/dejavu.jar dejavu.Verify ./prop.qtl | grep -v "Elapsed total"')
        os.system('scalac -cp .:' + DEJAVU_PATH + '/dejavu.jar TraceMonitor.scala 2>&1 | grep -v "warning"')
        os.chdir('../')
    os.chdir('../eff/')
    for action in aux_dict_pre_eff:
        if 'end_' not in action: continue
        if action not in synthesised_properties: continue
        action = action[4:]
        os.chdir('./' + action)
        os.system('java -cp ' + DEJAVU_PATH + '/dejavu.jar dejavu.Verify ./prop.qtl | grep -v "Elapsed total"')
        os.system('scalac -cp .:' + DEJAVU_PATH + '/dejavu.jar TraceMonitor.scala 2>&1 | grep -v "warning"')
        os.chdir('../')
    os.chdir(current_path)

def synthesise_centralised_monitor(domain_file, plan_file, aux_dict_pre_eff):
    aux_dict_pre_eff = translate_fol(domain_file, aux_dict_pre_eff)
    translate_ltl(domain_file, plan_file)
    with open(GLOBAL_PATH + './out/synthesised_properties', 'r') as file:
        synthesised_properties = file.read()
    synthesised_properties = synthesised_properties.replace(' ', '').replace('\'', '').replace('[', '').replace(']', '').split(',')
    print(synthesised_properties)
    current_path = os.getcwd()
    os.chdir(GLOBAL_PATH + './out/pre/')
    os.system('java -cp ' + DEJAVU_PATH + '/dejavu.jar dejavu.Verify ./prop.qtl | grep -v "Elapsed total"')
    os.system('scalac -cp .:' + DEJAVU_PATH + '/dejavu.jar TraceMonitor.scala 2>&1 | grep -v "warning"')
    os.chdir('../eff/')
    os.system('java -cp ' + DEJAVU_PATH + '/dejavu.jar dejavu.Verify ./prop.qtl | grep -v "Elapsed total"')
    os.system('scalac -cp .:' + DEJAVU_PATH + '/dejavu.jar TraceMonitor.scala 2>&1 | grep -v "warning"')
    os.chdir(current_path)

def translate_fol(domain_file, aux_dict_pre_eff):
    if aux_dict_pre_eff:
        with open(GLOBAL_PATH + './out/dict_pre_eff.json', 'r') as file:
            backup = file.read()
    os.system('python3 ' + GLOBAL_PATH + 'translators/translator.py ' + domain_file)
    if aux_dict_pre_eff:
        with open(GLOBAL_PATH + './out/dict_pre_eff.json', 'w') as file:
            file.write(backup)
        return aux_dict_pre_eff
    else:
        global dict_pre_eff
        # Load the JSON file which contains the information about each action's preconditions and effects
        with open(GLOBAL_PATH + './out/dict_pre_eff.json', 'r') as file:
            dict_pre_eff = json.load(file)
        return dict_pre_eff
def translate_ltl(domain_file, plan_file):
    os.system('python3 ' + GLOBAL_PATH + 'translators/translator.py ' + domain_file + ' ' + plan_file)

def get_instantiated_pre_eff_action(prefix, action):
    (params, cond) = dict_pre_eff[prefix + action._functor]
    auxMap = {}
    for i in range(0, len(params)):
        auxMap[params[i]] = action._args[i].replace('\n', '')
    cond = cond.copy()
    for i in range(0, len(cond)):
        for m in auxMap:
            cond[i] = cond[i].replace(m, auxMap[m])
    cond = set([c.replace('(', ',').replace(')', '').replace(' ', '').replace('!','not_') for c in cond])
    return cond, auxMap

def detect_issue(prefix, action, props):
    cond, _ = get_instantiated_pre_eff_action(prefix, action)
    props = set([str(p) for p in props])
    return cond.difference(props), props.difference(cond)

def log(*things):
    if simulating:
        if things[0] == 'PRE':
            raise Exception('begin_' + str(things[3]).split(',')[0])
        if things[0] == 'POST':
            raise Exception('end_' + str(things[3]).split(',')[0])
        if things[0] == 'FAILURE':
            raise Exception('failure_' + str(things[3]).split(',')[0])
    with open(GLOBAL_PATH + './out/log', 'a') as file:
        for t in things:
            file.write(str(t).replace('\n', '').replace(' ', '') + ' ')
        file.write('\n')

def store_plans():
    global replanning_calls, counter_store_plans
    os.makedirs('./plans/', exist_ok=True)
    if replanning_calls > 0:
        name = f'replan_{replanning_calls}'
    else:
        name = 'original'
    shutil.copy('./sas_plan', './plans/')
    shutil.move('./plans/sas_plan', f'./plans/{name}')
    if replanning_calls > 0:
        if replanning_calls > 1:
            previous = f'replan_{replanning_calls-1}'
        else:
            previous = 'original'
        with open('./plans/dictionary_plans.txt', 'a+') as f:
            f.write(f'{previous}: {counter_store_plans}\n')
    counter_store_plans = 1
        

def replan():
    global actions, replanning_time, replanning_calls, avg_size_replanning_plans, prev_action, past_actions
    replanning_calls += 1
    if os.path.exists('./sas_plan'):
        os.rename('./sas_plan', './sas_plan_' + str(replanning_calls))
    start = time.time()
    # Creation of the newly updated problem file (starting from the snapshot)
    with open(GLOBAL_PATH + './out/updated_problem.pddl', 'w') as updated_problem_file:
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
    os.system(PLANNER_PATH + ' ' + DOMAIN_FILE + ' ' + GLOBAL_PATH + './out/updated_problem.pddl')
    store_plans()
    if not exists('./sas_plan'):
        print('No plan found, stop execution')
        exit()
    with open('./sas_plan', 'r') as plan:
        actions = plan.readlines()
        actions = actions[:-1]
    avg_size_replanning_plans += len(actions)
    replanning_time += time.time() - start
    translate_ltl(DOMAIN_FILE, './sas_plan')
    # props = connector.get_errors()
    prev_action = None
    past_actions = []
    callbackNewProps(None, set())

def log_metrics():
    # (initial solution planning time,  replanning time, total plan size of executed actions, replanning calls, monitor synthesis runtime, simulation time, kind of simulation violations, average size of replanning plans)
    with open('./res_'+ str(errors_to_inject) +'.csv', 'a') as f:
        f.write(str(initial_planning_time) + ';')
        f.write(str(replanning_time) + ';')
        f.write(str(connector.get_actions_executed()) + ';')
        f.write(str(replanning_calls) + ';')
        f.write(str(update_monitor_time) + ';')
        f.write(str(simulation_time) + ';')
        f.write(','.join(simulation_violations) + ';')
        if replanning_calls == 0:
            f.write(str(0) + '\n')
        else:
            f.write(str(avg_size_replanning_plans/replanning_calls) + '\n')

if __name__ == '__main__':
    main(sys.argv)
