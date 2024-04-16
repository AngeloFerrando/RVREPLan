#! /bin/bash

PLANNER_PATH="/home/angelo/downward" #"<path_to_fastdownward>"
DEJAVU_PATH="/home/angelo/dejavu" #"<path_to_dejavu>"

cd ./experiments/lama/logistics/

# python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias lama-first" --inject_errors 0 
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias lama-first" --inject_errors 1
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias lama-first" --inject_errors 2 
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias lama-first" --inject_errors 3 
done

cd ../depot/

# python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias lama-first" --inject_errors 0
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias lama-first" --inject_errors 1
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias lama-first" --inject_errors 2
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias lama-first" --inject_errors 3
done

cd ../satellite/
# python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias lama-first" --inject_errors 0
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias lama-first" --inject_errors 1
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias lama-first" --inject_errors 2
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias lama-first" --inject_errors 3
done

cd ../../bjolp/logistics/

# python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 1 
# for i in `seq 1 1`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 1
# done
# for i in `seq 1 1`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 2 
# done
# for i in `seq 1 1`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 3 
# done

cd ../depot/

# python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 1 
for i in `seq 1 1`
do
   python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 1
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 2
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 3
done

cd ../satellite/
# python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 1 
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 1
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 2
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 3
done

cd ../../lmcut/logistics/

# python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 1 
# for i in `seq 1 1`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 1
# done
# for i in `seq 1 1`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 2 
# done
# for i in `seq 1 1`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 3 
# done

cd ../depot/

# python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 1 
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 1
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 2
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 3
done

cd ../satellite/
# python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 1 
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 1
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 2
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite $DEJAVU_PATH "$PLANNER_PATH/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 3
done
