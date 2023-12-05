#! /bin/bash

cd ./experiments/lama/logistics/

# python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --inject_errors 0 
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --inject_errors 1
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --inject_errors 2 
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --inject_errors 3 
done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --no_monitor_synthesis --inject_errors 4 
# done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --no_monitor_synthesis --inject_errors 5
# done

cd ../depot/

# python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --inject_errors 0
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --inject_errors 1
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --inject_errors 2
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --inject_errors 3
done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --no_monitor_synthesis --inject_errors 4
# done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --no_monitor_synthesis --inject_errors 5
# done

cd ../satellite/
# python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --inject_errors 0
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --inject_errors 1
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --inject_errors 2
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --inject_errors 3
done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --no_monitor_synthesis --inject_errors 4
# done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias lama-first" --no_monitor_synthesis --inject_errors 5
# done

cd ../../bjolp/logistics/

# python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 1 
# for i in `seq 1 1`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 1
# done
# for i in `seq 1 1`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 2 
# done
# for i in `seq 1 1`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 3 
# done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 4 
# done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 5
# done

cd ../depot/

# python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 1 
for i in `seq 1 1`
do
   python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 1
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 2
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 3
done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 4
# done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 5
# done

cd ../satellite/
# python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 1 
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 0
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 2
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --inject_errors 3
done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 4
# done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 5
# done

cd ../../lmcut/logistics/

# python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 1 
# for i in `seq 1 1`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 1
# done
# for i in `seq 1 1`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 2 
# done
# for i in `seq 1 1`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 3 
# done
# for i in `seq 1 5`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --no_monitor_synthesis --inject_errors 4 
# done
# for i in `seq 1 5`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --no_monitor_synthesis --inject_errors 5
# done

cd ../depot/

# python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 1 
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 0
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 2
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 3
done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --no_monitor_synthesis --inject_errors 4
# done
# for i in `seq 1 20`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --no_monitor_synthesis --inject_errors 5
# done

cd ../satellite/
# python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 1 
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 1
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 2
done
for i in `seq 1 1`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --inject_errors 3
done
# for i in `seq 1 5`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --no_monitor_synthesis --inject_errors 4
# done
# for i in `seq 1 5`
# do
#     python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /home/angelo/dejavu/ "/home/angelo/downward/fast-downward.sif --alias seq-opt-lmcut" --no_monitor_synthesis --inject_errors 5
# done
