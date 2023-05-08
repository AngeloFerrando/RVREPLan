# RVRepLan

## What to install
- Download and Install DEJAVU (https://github.com/havelund/dejavu) and be sure it works [tested on version 1.0].
- Download and Install Python 3 and be sure it works [tested on version 3.6.9].

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

## Example of use for the three different domains:

- Download and Install Fast Downward (https://www.fast-downward.org/) and be sure it works [tested on version 22.06+].

Logistics:

```bash
python3 abstract_system.py ./benchmarks/logistics/domain.pddl ./benchmarks/logistics/problem.pddl connectors.raw_connector_logistics DEJAVU "PLANNER/fast-downward.py --alias lama-first"
```

Depot:

```bash
python3 abstract_system.py ./benchmarks/depot/domain.pddl ./benchmarks/depot/problem.pddl connectors.raw_connector_depot DEJAVU "PLANNER/fast-downward.py --alias lama-first"
```

Satellite:

```bash
python3 abstract_system.py ./benchmarks/satellite/domain.pddl ./benchmarks/satellite/problem.pddl connectors.raw_connector_satellite DEJAVU "PLANNER/fast-downward.py --alias lama-first"
```

where DEJAVU and PLANNER (replace .py with .sif if using the container version of FD) need to be replaced with their respective paths.

## To simulate failures and cause replanning

To ask RVReplan to simulate failures in order to cause replanning it is enough to pass an additional flag:

```bash
python3 abstract_system.py DOMAIN PROBLEM CONNECTOR DEJAVU PLANNER --inject_errors N
```

where the N parameter denotes the number of failures to instroduce (5 is the maximum value in our current experiments).

## Other useful flags

In addition to the other parameters and flags, it is also possible to pass:
- --no_monitor_synthesis: this flag causes RVReplan to not synthesise a new monitor, but to use an existing one (i.e., the one available in the folder); this is useful when running multiple times on the same domain, since the monitor would be the same.
