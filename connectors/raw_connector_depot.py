from connectors import abstract_connector
from data.proposition import Proposition
from time import sleep
from mappers import *

class RawConnectorDepot(abstract_connector.AbstractConnector):
    def __init__(self, mapper):
        self._mapper = mapper
        self._case = 0
        self._actions_executed = 0
        self._n_errors = 3
        self._errors = (
            [
                [
                    Proposition(False, 'at', ['truck1', 'distributor0']),
                    Proposition(False, 'at', ['truck1', 'distributor2']),
                    Proposition(False, 'at', ['truck1', 'depot0']),
                    Proposition(False, 'at', ['truck1', 'depot1']),
                    Proposition(False, 'at', ['truck1', 'depot2'])
                ],
                [
                    Proposition(False, 'at', ['truck0', 'distributor0']),
                    Proposition(False, 'at', ['truck0', 'distributor1']),
                    Proposition(False, 'at', ['truck0', 'depot0']),
                    Proposition(False, 'at', ['truck0', 'depot1']),
                    Proposition(False, 'at', ['truck0', 'depot2'])
                ],
                [
                    Proposition(False, 'at', ['truck1', 'distributor0']),
                    Proposition(False, 'at', ['truck1', 'distributor1']),
                    Proposition(False, 'at', ['truck1', 'distributor2']),
                    Proposition(False, 'at', ['truck1', 'depot1']),
                    Proposition(False, 'at', ['truck1', 'depot2'])
                ],
                [
                    Proposition(False, 'at', ['truck0', 'distributor0']),
                    Proposition(False, 'at', ['truck0', 'distributor1']),
                    Proposition(False, 'at', ['truck0', 'distributor2']),
                    Proposition(False, 'at', ['truck0', 'depot0']),
                    Proposition(False, 'at', ['truck0', 'depot1'])
                ],
                [
                    Proposition(False, 'at', ['truck1', 'distributor0']),
                    Proposition(False, 'at', ['truck1', 'distributor1']),
                    Proposition(False, 'at', ['truck1', 'distributor2']),
                    Proposition(False, 'at', ['truck1', 'depot0']),
                    Proposition(False, 'at', ['truck1', 'depot1'])
                ]
            ], 
            [
                [Proposition(True, 'at', ['truck1', 'distributor1'])],
                [Proposition(True, 'at', ['truck0', 'distributor2'])],
                [Proposition(True, 'at', ['truck1', 'depot0'])],
                [Proposition(True, 'at', ['truck0', 'depot2'])],
                [Proposition(True, 'at', ['truck1', 'depot2'])]
            ]
        )
        # self._time_to_fail = True

    def get_initial_propositions(self):
        props = self.get_errors()
#        props.add(Proposition(False, 'at', ['obj12', 'pos1']))
#        props.add(Proposition(True, 'at', ['obj12', 'pos2']))
        return props
    
    def get_errors(self):
        props = set()
        if self._errors[0] and self._errors[1] and self._n_errors:
            for p in self._errors[0].pop(0):
                props.add(p)
            for p in self._errors[1].pop(0):
                props.add(p)
            self._time_to_fail = False
            self._n_errors -= 1
        return props

    def perform(self, action, callback):
        self._actions_executed+=1
        cmd = (self._mapper.mapActionToCommand(action))
        sleep(0.1) # simulate cmd execution
        props = set()
        # if self._time_to_fail and self._errors[0] and self._errors[1] and self._n_errors:
        #     print('##############################################################################################', action)
        #     for p in self._errors[0].pop(0):
        #         props.add(p)
        #     for p in self._errors[1].pop(0):
        #         props.add(p)
        #     self._time_to_fail = False
        #     self._n_errors -= 1
        action = str(action)
        if 'drive' in action:
            l = 6
            i = action.index(',', l)
            j = action.index(',', i+1)
            truck = action[l:i]
            place_at = action[i+1:j]
            place_to = action[j+1:-1]
            # (and (at ?x ?z) (not (at ?x ?y)))
            props.add(Proposition(False, 'at', [truck, place_at]))
            props.add(Proposition(True, 'at', [truck, place_to]))
        elif 'lift' in action: 
            l = 5
            i = action.index(',', l)
            j = action.index(',', i+1)
            k = action.index(',', j+1)
            hoist = action[l:i]
            crate = action[i+1:j]
            surface = action[j+1:k]
            place = action[k+1:-1]
            # (and (lifting ?x ?y) (clear ?z) (not (at ?y ?p)) (not (clear ?y)) (not (available ?x)) (not (on ?y ?z)))
            props.add(Proposition(False, 'at', [crate, place]))
            props.add(Proposition(False, 'clear', [crate]))
            props.add(Proposition(False, 'available', [hoist]))
            props.add(Proposition(False, 'on', [crate, surface]))
            props.add(Proposition(True, 'lifting', [hoist, crate]))
            props.add(Proposition(True, 'clear', [surface]))
        elif 'drop' in action:
            l = 5
            i = action.index(',', l)
            j = action.index(',', i+1)
            k = action.index(',', j+1)
            hoist = action[l:i]
            crate = action[i+1:j]
            surface = action[j+1:k]
            place = action[k+1:-1]
            # (and (available ?x) (at ?y ?p) (clear ?y) (on ?y ?z) (not (lifting ?x ?y)) (not (clear ?z)))
            props.add(Proposition(False, 'lifting', [hoist, crate]))
            props.add(Proposition(False, 'clear', [surface]))
            props.add(Proposition(True, 'at', [crate, place]))
            props.add(Proposition(True, 'clear', [crate]))
            props.add(Proposition(True, 'available', [hoist]))
            props.add(Proposition(True, 'on', [crate, surface]))
        elif 'unload' in action:
            l = 7
            i = action.index(',', l)
            j = action.index(',', i+1)
            k = action.index(',', j+1)
            hoist = action[l:i]
            crate = action[i+1:j]
            truck = action[j+1:k]
            place = action[k+1:-1]
            # (and (lifting ?x ?y) (not (in ?y ?z)) (not (available ?x)))
            props.add(Proposition(False, 'in', [crate, truck]))
            props.add(Proposition(False, 'available', [hoist]))
            props.add(Proposition(True, 'lifting', [hoist, crate]))
        elif 'load' in action:
            l = 5
            i = action.index(',', l)
            j = action.index(',', i+1)
            k = action.index(',', j+1)
            hoist = action[l:i]
            crate = action[i+1:j]
            truck = action[j+1:k]
            place = action[k+1:-1]
            # (in ?y ?z) (available ?x) (not (lifting ?x ?y)))
            props.add(Proposition(False, 'lifting', [hoist, crate]))
            props.add(Proposition(True, 'in', [crate, truck]))
            props.add(Proposition(True, 'available', [hoist]))
        self._case = self._case + 1
        callback(props)
    def set_errors_to_inject(self, v):
        self._n_errors = v
    # def set_time_to_fail(self, v):
    #     self._time_to_fail = v
    def get_actions_executed(self):
        return self._actions_executed
CONNECTOR = RawConnectorDepot(raw_mapper.RawMapper())