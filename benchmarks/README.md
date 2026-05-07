# Benchmarks

This directory contains the PDDL domains and problems used by the RVRepLan
experiments.

Each benchmark subdirectory follows the same convention:

- `domain.pddl`: baseline domain used for initial planning and monitor
  synthesis.
- `problem.pddl`: initial state and goal specification.
- `domain_1.pddl`, `domain_new.pddl`, and `domain_1_new.pddl`: domain variants
  produced or used while evaluating monitor updates and replanning.
- `errors.txt`: notes about injected or observed benchmark-specific deviations.

The benchmark set currently includes `logistics`, `depot`, and `satellite`.
These domains are intentionally small enough to support repeated replanning
runs while still exercising precondition and postcondition violation handling.
