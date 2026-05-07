# Experiments

This directory stores experiment drivers, result summaries, and plan traces
produced by the benchmark runs.

The main repository script `experiments.sh` runs RVRepLan across the configured
planner/domain combinations and writes CSV metrics into the relevant experiment
subdirectories. Stored plan files named `original`, `replan_1`, `replan_2`, and
similar capture the evolution of the planner output after monitor violations.

The optional `stability.py` helper compares stored plans and reports simple
addition/removal counts. `stability.xlsx` contains the corresponding spreadsheet
summary used during analysis.

Experiment subdirectories are organised by planner configuration first, then by
benchmark domain, for example:

- `lama/logistics`
- `bjolp/depot`
- `lmcut/satellite`

Before rerunning the full experiment suite, update the local Dejavu and
Fast-Downward paths in `experiments.sh`.
