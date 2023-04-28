from connectors import abstract_connector
from data.proposition import Proposition
from time import sleep

class RawConnectorRover(abstract_connector.AbstractConnector):
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
        if 'turn_to' in action:
            l = 8
            i = action.index(',', l)
            j = action.index(',', i+1)
            sat = action[l:i]
            d_new = action[i+1:j]
            d_prev = action[j+1:-1]
            # (and (pointing ?s ?d_new) (not (pointing ?s ?d_prev)))
            props.add(Proposition(False, 'pointing', [sat, d_prev]))
            props.add(Proposition(True, 'pointing', [sat, d_new]))
        elif 'switch_on' in action: 
            l = 10
            i = action.index(',', l)
            j = action.index(',', i+1)
            instrument = action[l:i]
            sat = action[i+1:j]
            surface = action[j+1:-1]
            # (and (power_on ?i) (not (calibrated ?i)) (not (power_avail ?s)))
            props.add(Proposition(False, 'calibrated', [instrument]))
            props.add(Proposition(False, 'power_avail', [sat]))
			props.add(Proposition(True, 'power_on', [instrument]))
        elif 'switch_off' in action:
            l = 11
            i = action.index(',', l)
            j = action.index(',', i+1)
            instrument = action[l:i]
            sat = action[i+1:j]
            surface = action[j+1:-1]
            # (and (power_avail ?s) (not (power_on ?i)))
			props.add(Proposition(False, 'power_on', [instrument]))
			props.add(Proposition(True, 'power_avail', [sat]))
        elif 'calibrate' in True:
            l = 10
            i = action.index(',', l)
            j = action.index(',', i+1)
            sat = action[l:i]
            instrument = action[i+1:j]
            d = action[j+1:-1]
            # (calibrated ?i)
			props.add(Proposition(True, 'calibrated', [instrument]))
        elif 'take_image' in True:
            l = 11
            i = action.index(',', l)
            j = action.index(',', i+1)
			k = action.index(',', j+1)
            sat = action[l:i]
            d = action[i+1:j]
            instrument = action[j+1:k]
			mode = action[k+1:-1]
            # (have_image ?d ?m)
			props.add(Proposition(True, 'lifting', [d, mode]))
        self._case = self._case + 1
        callback(props)
