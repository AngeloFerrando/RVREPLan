from connectors import abstract_connector
from data.proposition import Proposition
from time import sleep
from mappers import *

class RawConnectorRover(abstract_connector.AbstractConnector):
    def __init__(self, mapper):
        self._mapper = mapper
        self._case = 0
        self._actions_executed = 0
        self._n_errors = 3
        self._errors = (
            [
                [Proposition(False, 'power_avail', ['satellite1'])],
                [Proposition(False, 'power_avail', ['satellite0'])],
                [Proposition(False, 'pointing', ['satellite1', 'star6'])],
                [Proposition(False, 'calibration_target', ['instrument2', 'star2'])],
                [Proposition(False, 'calibration_target', ['instrument0', 'star1'])]
            ],
            [
                [Proposition(True, 'power_on', ['instrument2'])],
                [Proposition(True, 'power_on', ['instrument0'])],
                [Proposition(True, 'pointing', ['satellite1', 'star0'])],
                [Proposition(True, 'calibration_target', ['instrument2', 'groundstation3'])],       
                [Proposition(True, 'calibration_target', ['instrument0', 'planet5'])]
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
        #     # print('##############################################################################################', len(self._errors))
        #     for p in self._errors[0].pop(0):
        #         props.add(p)
        #     for p in self._errors[1].pop(0):
        #         props.add(p)
        #     self._time_to_fail = False
        #     self._n_errors -= 1
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
            instrument = action[l:i]
            sat = action[i+1:-1]
            # (and (power_on ?i) (not (calibrated ?i)) (not (power_avail ?s)))
            props.add(Proposition(False, 'calibrated', [instrument]))
            props.add(Proposition(False, 'power_avail', [sat]))
            props.add(Proposition(True, 'power_on', [instrument]))
        elif 'switch_off' in action:
            l = 11
            i = action.index(',', l)
            instrument = action[l:i]
            sat = action[i+1:-1]
            # (and (power_avail ?s) (not (power_on ?i)))
            props.add(Proposition(False, 'power_on', [instrument]))
            props.add(Proposition(True, 'power_avail', [sat]))
        elif 'calibrate' in action:
            l = 10
            i = action.index(',', l)
            j = action.index(',', i+1)
            sat = action[l:i]
            instrument = action[i+1:j]
            d = action[j+1:-1]
            # (calibrated ?i)
            props.add(Proposition(True, 'calibrated', [instrument]))
        elif 'take_image' in action:
            l = 11
            i = action.index(',', l)
            j = action.index(',', i+1)
            k = action.index(',', j+1)
            sat = action[l:i]
            d = action[i+1:j]
            instrument = action[j+1:k]
            mode = action[k+1:-1]
            # (have_image ?d ?m)
            props.add(Proposition(True, 'have_image', [d, mode]))
        self._case = self._case + 1
        callback(props)
    def set_errors_to_inject(self, v):
        self._n_errors = v
    # def set_time_to_fail(self, v):
    #     self._time_to_fail = v
    def get_actions_executed(self):
        return self._actions_executed
CONNECTOR = RawConnectorRover(raw_mapper.RawMapper())