# RvEPLan

## How to run

```bash
python3 abstract_system.py DOMAIN PROBLEM CONNECTOR DEJAVU_PATH PLANNER
```

Example:

```bash
python3 abstract_system.py ./benchmarks/logistics/domain.pddl ./benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-lmcut"
```