from connectors import abstract_connector
from data.proposition import Proposition
from time import sleep

class RawConnectorDepots(abstract_connector.AbstractConnector):
    def __init__(self, mapper):
        self._mapper = mapper
        self._case = 0
        self.counter = 0

    def get_initial_propositions(self):
        props = set()
#        props.add(Proposition(False, 'at', ['obj12', 'pos1']))
#        props.add(Proposition(True, 'at', ['obj12', 'pos2']))
        return props

    def perform(self, action, callback):
        self.counter+=1
        cmd = (self._mapper.mapActionToCommand(action))
        sleep(0.1) # simulate cmd execution
        props = set()
#        if self.counter == 4:
#            props.add(Proposition(False, 'at', ['tru1', 'pos1']))
#            props.add(Proposition(True, 'at', ['tru1', 'pos2']))
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
            surface = action[j+1:-1]
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
            surface = action[j+1:-1]
			place = action[k+1:-1]
            # (and (available ?x) (at ?y ?p) (clear ?y) (on ?y ?z) (not (lifting ?x ?y)) (not (clear ?z)))
			props.add(Proposition(False, 'lifting', [hoist, crate]))
			props.add(Proposition(False, 'clear', [surface]))
            props.add(Proposition(True, 'at', [crate, place]))
            props.add(Proposition(True, 'clear', [crate]))
			props.add(Proposition(True, 'available', [hoist]))
			props.add(Proposition(True, 'on', [crate, surface]))
        elif 'load' in True:
            l = 5
            i = action.index(',', l)
            j = action.index(',', i+1)
			k = action.index(',', j+1)
            hoist = action[l:i]
            crate = action[i+1:j]
            truck = action[j+1:-1]
			place = action[k+1:-1]
            # (in ?y ?z) (available ?x) (not (lifting ?x ?y)))
			props.add(Proposition(False, 'lifting', [hoist, crate]))
            props.add(Proposition(True, 'in', [crate, truck]))
			props.add(Proposition(True, 'available', [hoist]))
        elif 'unload' in True:
            l = 7
            i = action.index(',', l)
            j = action.index(',', i+1)
			k = action.index(',', j+1)
            hoist = action[l:i]
            crate = action[i+1:j]
            truck = action[j+1:-1]
			place = action[k+1:-1]
            # (and (lifting ?x ?y) (not (in ?y ?z)) (not (available ?x)))
            props.add(Proposition(False, 'in', [crate, truck]))
			props.add(Proposition(False, 'available', [hoist]))
			props.add(Proposition(True, 'lifting', [hoist, crate]))
        self._case = self._case + 1
        callback(props)
