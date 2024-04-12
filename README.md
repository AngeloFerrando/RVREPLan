# RVRepLan

## What to install
- Download and Install DEJAVU (https://github.com/havelund/dejavu) and be sure it works [tested on version 1.0].
- Download and Install Fast-Downward (https://www.fast-downward.org) and be sure it works [tested on version 22.12+]
- Download and Install Python 3 and be sure it works [tested on version 3.10.12].

## How to run

To run RVReplan, open a terminal in the installation folder and run:

```bash
python3 abstract_system.py DOMAIN PROBLEM CONNECTOR DEJAVU PLANNER
```

where:
- abstract_system.py: the main script which implements RVReplan algorithms
- DOMAIN: the domain file (.pddl) describing the domain of interest
- PROBLEM: the problem file (.pddl) describing the initial state of the system (i.e., the problem to solve)
- CONNECTOR: the connector used by RVReplan to connect with the real system (the connectors for the three domains used in the experiments are available)
- DEJAVU: the path to the folder where Dejavu has been installed (where dejavu.jar is)
- PLANNER: the path to the planner and any flags it may use

## Example of use for the three different domains experimented in the paper:

Logistics:

```bash
python3 abstract_system.py ./benchmarks/logistics/domain.pddl ./benchmarks/logistics/problem.pddl connectors.raw_connector_logistics DEJAVU "PLANNER/fast-downward.py --alias lama-first"
```

```bash
python3 abstract_system.py ./benchmarks/logistics/domain.pddl ./benchmarks/logistics/problem.pddl connectors.raw_connector_logistics DEJAVU "PLANNER/fast-downward.py --alias seq-opt-bjolp"
```

```bash
python3 abstract_system.py ./benchmarks/logistics/domain.pddl ./benchmarks/logistics/problem.pddl connectors.raw_connector_logistics DEJAVU "PLANNER/fast-downward.py --alias seq-opt-lmcut"
```

Depot:

```bash
python3 abstract_system.py ./benchmarks/depot/domain.pddl ./benchmarks/depot/problem.pddl connectors.raw_connector_depot DEJAVU "PLANNER/fast-downward.py --alias lama-first"
```

```bash
python3 abstract_system.py ./benchmarks/depot/domain.pddl ./benchmarks/depot/problem.pddl connectors.raw_connector_depot DEJAVU "PLANNER/fast-downward.py --alias seq-opt-bjolp"
```

```bash
python3 abstract_system.py ./benchmarks/depot/domain.pddl ./benchmarks/depot/problem.pddl connectors.raw_connector_depot DEJAVU "PLANNER/fast-downward.py --alias seq-opt-lmcut"
```

Satellite:

```bash
python3 abstract_system.py ./benchmarks/satellite/domain.pddl ./benchmarks/satellite/problem.pddl connectors.raw_connector_satellite DEJAVU "PLANNER/fast-downward.py --alias lama-first"
```

```bash
python3 abstract_system.py ./benchmarks/satellite/domain.pddl ./benchmarks/satellite/problem.pddl connectors.raw_connector_satellite DEJAVU "PLANNER/fast-downward.py --alias seq-opt-bjolp"
```

```bash
python3 abstract_system.py ./benchmarks/satellite/domain.pddl ./benchmarks/satellite/problem.pddl connectors.raw_connector_satellite DEJAVU "PLANNER/fast-downward.py --alias seq-opt-lmcut"
```

where DEJAVU and PLANNER (replace .py with .sif if using the container version of FD) need to be replaced with their respective paths.

## To simulate failures and cause replanning

To ask RVReplan to simulate failures in order to cause replanning it is enough to pass an additional flag:

```bash
python3 abstract_system.py DOMAIN PROBLEM CONNECTOR DEJAVU PLANNER --inject_errors N
```

where the N parameter denotes the kind of failures to introduce:
- 0 no failures (this is the default if no --inject_errors flag is passed)
- 1 one failure on the precondition of an action
- 2 one failure on the postcondition of an action
- 3 both previous failures are added
Note that, the addition of a failure may cause more replanning calls.

## Other useful flags

In addition to the other parameters and flags, it is also possible to pass:
- --no_monitor_synthesis: this flag causes RVReplan to not synthesise a new monitor, but to use an existing one (i.e., the one available in the folder); this is useful when running multiple times on the same domain, since the monitor would be the same.

## To run experiments

To run the experiments on all benchmarks using all three Fast-Downward options (lama-first, bjolp, and lmcut).

```bash
sh ./experiments.sh
```

Once the script is done, you should find in each sub-folder of the experiments folder the CSV containing the experimental results.