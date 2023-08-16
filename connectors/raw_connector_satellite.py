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

        self.__trigger_remove = {}
        self.__trigger_add = {}

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
            if 'turn_to' not in self.__trigger_remove or not self.__trigger_remove['turn_to']():
                props.add(Proposition(False, 'pointing', [sat, d_prev]))
                props.add(Proposition(True, 'pointing', [sat, d_new]))
            if 'turn_to' in self.__trigger_add and self.__trigger_add['turn_to']():
                props.add(Proposition(False, 'orbit', [sat]))
        elif 'switch_on' in action:
            l = 10
            i = action.index(',', l)
            instrument = action[l:i]
            sat = action[i+1:-1]
            # (and (power_on ?i) (not (calibrated ?i)) (not (power_avail ?s)))
            if 'switch_on' not in self.__trigger_remove or not self.__trigger_remove['switch_on']():
                props.add(Proposition(False, 'calibrated', [instrument]))
                props.add(Proposition(False, 'power_avail', [sat]))
                props.add(Proposition(True, 'power_on', [instrument]))
            if 'switch_on' in self.__trigger_add and self.__trigger_add['switch_on']():
                props.add(Proposition(True, 'fake', [sat]))
        elif 'switch_off' in action:
            l = 11
            i = action.index(',', l)
            instrument = action[l:i]
            sat = action[i+1:-1]
            # (and (power_avail ?s) (not (power_on ?i)))
            if 'switch_off' not in self.__trigger_remove or not self.__trigger_remove['switch_off']():
                props.add(Proposition(False, 'power_on', [instrument]))
                props.add(Proposition(True, 'power_avail', [sat]))
            if 'switch_off' in self.__trigger_add and self.__trigger_add['switch_off']():
                props.add(Proposition(True, 'fake', [sat]))
        elif 'calibrate_and_take_image' in action:
            l = 25
            i = action.index(',', l)
            j = action.index(',', i+1)
            k = action.index(',', j+1)
            sat = action[l:i]
            d = action[i+1:j]
            instrument = action[j+1:k]
            mode = action[k+1:-1]
            # (have_image ?d ?m)
            if 'calibrate_and_take_image' not in self.__trigger_remove or not self.__trigger_remove['calibrate_and_take_image']():
                props.add(Proposition(True, 'have_image', [d, mode]))
                props.add(Proposition(True, 'calibrated', [instrument]))
            if 'calibrate_and_take_image' in self.__trigger_add and self.__trigger_add['calibrate_and_take_image']():
                props.add(Proposition(True, 'fake', [sat]))
        elif 'calibrate' in action:
            l = 10
            i = action.index(',', l)
            j = action.index(',', i+1)
            sat = action[l:i]
            instrument = action[i+1:j]
            d = action[j+1:-1]
            # (calibrated ?i)
            if 'calibrate' not in self.__trigger_remove or not self.__trigger_remove['calibrate']():
                props.add(Proposition(True, 'calibrated', [instrument]))
            if 'calibrate' in self.__trigger_add and self.__trigger_add['calibrate']():
                props.add(Proposition(True, 'fake', [sat]))
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
            if 'take_image' not in self.__trigger_remove or not self.__trigger_remove['take_image']():
                props.add(Proposition(True, 'have_image', [d, mode]))
            if 'take_image' in self.__trigger_add and self.__trigger_add['take_image']():
                props.add(Proposition(True, 'fake', [sat]))
        elif 'orbiting' in action:
            l = 9
            sat = action[l:-1]
            if 'orbiting' not in self.__trigger_remove or not self.__trigger_remove['orbiting']():
                props.add(Proposition(True, 'orbit', [sat]))
            if 'orbiting' in self.__trigger_add and self.__trigger_add['orbiting']():
                props.add(Proposition(True, 'fake', [sat]))
        self._case = self._case + 1
        callback(abstract_connector.ResultCode.SUCCESS, props)
    def set_errors_to_inject(self, v):
        self._n_errors = v
        if self._n_errors == 1 or self._n_errors == 3:
            self.__trigger_remove['calibrate_and_take_image'] = lambda : True
        if self._n_errors == 2 or self._n_errors == 3:
            self.__trigger_add['turn_to'] = lambda : True
    # def set_time_to_fail(self, v):
    #     self._time_to_fail = v
    def get_actions_executed(self):
        return self._actions_executed
CONNECTOR = RawConnectorRover(raw_mapper.RawMapper())