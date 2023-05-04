#! /bin/bash

cd ./experiments/lama/logistics/

python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --inject_errors 1 
for i in `seq 1 19`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 1 
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 2 
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 3 
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 4 
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 5
done

cd ../depot/

python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --inject_errors 1 
for i in `seq 1 19`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 1
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 2
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 3
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 4
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 5
done

cd ../satellite/
python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --inject_errors 1 
for i in `seq 1 19`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 1
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 1
done
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 2
done
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 3
done
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 4
done
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias lama-first" --no_monitor_synthesis --inject_errors 5
done

cd ../../bjolp/logistics/

python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --inject_errors 1 
for i in `seq 1 19`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 1 
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 2 
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 3 
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 4 
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/logistics/domain.pddl ../../../benchmarks/logistics/problem.pddl connectors.raw_connector_logistics /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 5
done

cd ../depot/

python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --inject_errors 1 
for i in `seq 1 19`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 1
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 2
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 3
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 4
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/depot/domain.pddl ../../../benchmarks/depot/problem.pddl connectors.raw_connector_depot /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 5
done

cd ../satellite/
python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --inject_errors 1 
for i in `seq 1 19`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 1
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 1
done
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 2
done
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 3
done
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 4
done
done
for i in `seq 1 20`
do
    python3 ../../../abstract_system.py ../../../benchmarks/satellite/domain.pddl ../../../benchmarks/satellite/problem.pddl connectors.raw_connector_satellite /media/angelo/WorkData/dejavu/ "/media/angelo/WorkData/downward/fast-downward.py --alias seq-opt-bjolp" --no_monitor_synthesis --inject_errors 5
done
