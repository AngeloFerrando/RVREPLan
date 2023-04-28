from connectors import abstract_connector
from data.proposition import Proposition
from time import sleep

class RawConnectorLogistics(abstract_connector.AbstractConnector):
    def __init__(self, mapper):
        self._mapper = mapper
        self._case = 0
        self.counter = 0

    def get_initial_propositions(self):
        props = set()
        props.add(Proposition(False, 'at', ['obj12', 'pos1']))
        props.add(Proposition(True, 'at', ['obj12', 'pos2']))
        return props

    def perform(self, action, callback):
        self.counter+=1
        cmd = (self._mapper.mapActionToCommand(action))
        sleep(0.1) # simulate cmd execution
        props = set()
        if self.counter == 4:
            props.add(Proposition(False, 'at', ['tru1', 'pos1']))
            props.add(Proposition(True, 'at', ['tru1', 'pos2']))
        action = str(action)
        if 'unload_truck' in action or 'unload_airplane' in action: # unloading actions
            if 'unload_truck' in action:
                l = 13
            elif 'unload_airplane' in action:
                l = 16
            i = action.index(',', l)
            j = action.index(',', i+1)
            obj = action[l:i]
            vehicle = action[i+1:j]
            loc = action[j+1:-1]
            # (and (not (in ?obj ?truck)) (at ?obj ?loc)))
            props.add(Proposition(False, 'in', [obj, vehicle]))
            props.add(Proposition(True, 'at', [obj, loc]))
        elif 'load_truck' in action or 'load_airplane' in action: # loading actions
            if 'load_truck' in action:
                l = 11
            elif 'load_airplane' in action:
                l = 14
            i = action.index(',', l)
            j = action.index(',', i+1)
            obj = action[l:i]
            vehicle = action[i+1:j]
            loc = action[j+1:-1]
            # (and (not (at ?obj ?loc)) (in ?obj ?truck)))
            props.add(Proposition(False, 'at', [obj, loc]))
            props.add(Proposition(True, 'in', [obj, vehicle]))
        elif 'drive_truck' in action:
            if 'drive_truck' in action:
                l = 12
            i = action.index(',', l)
            j = action.index(',', i+1)
            k = action.index(',', j+1)
            vehicle = action[l:i]
            locfrom = action[i+1:j]
            locto = action[j+1:k]
            city = action[k+1:-1]
            # (and (not (at ?truck ?loc-from)) (at ?truck ?loc-to)))
            props.add(Proposition(False, 'at', [vehicle, locfrom]))
            props.add(Proposition(True, 'at', [vehicle, locto]))
        elif 'fly_airplane' in action:
            if 'fly_airplane' in action:
                l = 13
            i = action.index(',', l)
            j = action.index(',', i+1)
            vehicle = action[l:i]
            locfrom = action[i+1:j]
            locto = action[j+1:-1]
            # (and (not (at ?airplane ?loc-from)) (at ?airplane ?loc-to)))
            props.add(Proposition(False, 'at', [vehicle, locfrom]))
            props.add(Proposition(True, 'at', [vehicle, locto]))
        self._case = self._case + 1
        callback(props)
