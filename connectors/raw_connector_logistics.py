from connectors import abstract_connector
from data.proposition import Proposition
from time import sleep
from mappers import *

class RawConnectorLogistics(abstract_connector.AbstractConnector):
    def __init__(self, mapper):
        self._mapper = mapper
        self._case = 0
        self._actions_executed = 0
        self._n_errors = 3
# [(at obj33 pos2),(at obj33 pos3),(at obj33 pos4),(at obj33 apt1),(at obj33 apt2),(at obj33 apt3),(at obj33 apt4),(in obj33 tru1),(in obj33 tru2),(in obj33 tru3),(in obj33 tru4),(in obj33 apn1)], [(at obj33 pos1)]
# [(at obj12 pos1),(at obj12 pos2),(at obj12 pos3),(at obj12 apt1),(at obj12 apt2),(at obj12 apt3),(at obj12 apt4),(in obj12 tru1),(in obj12 tru2),(in obj12 tru3),(in obj12 tru4),(in obj12 apn1)], [(at obj12 pos4)]
# [(at apn1 apt1),(at apn1 apt2),(at apn1 apt4)], [(at apn1 apt3)]
# [(at obj32 pos1),(at obj32 pos2),(at obj32 pos3),(at obj32 pos4),(at obj32 apt1),(at obj32 apt2),(at obj32 apt3),(in obj32 tru1),(in obj32 tru2),(in obj32 tru3),(in obj32 tru4),(in obj32 apn1)], [(at obj32 apt4)]

        self._errors = (
            [
                [Proposition(False, 'in_city', ['pos2', 'cit2'])],
                [
                    Proposition(False, 'at', ['obj33', 'pos2']),
                    Proposition(False, 'at', ['obj33', 'pos3']),
                    Proposition(False, 'at', ['obj33', 'pos4']),
                    Proposition(False, 'at', ['obj33', 'apt1']),
                    Proposition(False, 'at', ['obj33', 'apt2']),
                    Proposition(False, 'at', ['obj33', 'apt3']),
                    Proposition(False, 'at', ['obj33', 'apt4']),
                    Proposition(False, 'in', ['obj33', 'tru1']),
                    Proposition(False, 'in', ['obj33', 'tru2']),
                    Proposition(False, 'in', ['obj33', 'tru3']),
                    Proposition(False, 'in', ['obj33', 'tru4']),
                    Proposition(False, 'in', ['obj33', 'apn1'])
                ],
                [
                    Proposition(False, 'at', ['obj12', 'pos1']),
                    Proposition(False, 'at', ['obj12', 'pos2']),
                    Proposition(False, 'at', ['obj12', 'pos3']),
                    Proposition(False, 'at', ['obj12', 'apt1']),
                    Proposition(False, 'at', ['obj12', 'apt2']),
                    Proposition(False, 'at', ['obj12', 'apt3']),
                    Proposition(False, 'at', ['obj12', 'apt4']),
                    Proposition(False, 'in', ['obj12', 'tru1']),
                    Proposition(False, 'in', ['obj12', 'tru2']),
                    Proposition(False, 'in', ['obj12', 'tru3']),
                    Proposition(False, 'in', ['obj12', 'tru4']),
                    Proposition(False, 'in', ['obj12', 'apn1'])
                ],
                [
                    Proposition(False, 'at', ['apn1', 'apt1']),
                    Proposition(False, 'at', ['apn1', 'apt2']),
                    Proposition(False, 'at', ['apn1', 'apt4'])
                ],
                [
                    Proposition(False, 'at', ['obj32', 'pos1']),
                    Proposition(False, 'at', ['obj32', 'pos2']),
                    Proposition(False, 'at', ['obj32', 'pos3']),
                    Proposition(False, 'at', ['obj32', 'pos4']),
                    Proposition(False, 'at', ['obj32', 'apt1']),
                    Proposition(False, 'at', ['obj32', 'apt2']),
                    Proposition(False, 'at', ['obj32', 'apt3']),
                    Proposition(False, 'in', ['obj32', 'tru1']),
                    Proposition(False, 'in', ['obj32', 'tru2']),
                    Proposition(False, 'in', ['obj32', 'tru3']),
                    Proposition(False, 'in', ['obj32', 'tru4']),
                    Proposition(False, 'in', ['obj32', 'apn1'])
                ]                
            ], 
            [
                [Proposition(True, 'in_city', ['pos2', 'cit3'])],
                [Proposition(True, 'at', ['obj33', 'pos1'])],
                [Proposition(True, 'at', ['obj12', 'pos4'])],
                [Proposition(True, 'at', ['apn1', 'apt3'])],
                [Proposition(True, 'at', ['obj32', 'apt4'])]                
            ]
        )
        # self._time_to_fail = True
        self.__trigger_remove = {}
        # self.__trigger_remove['load_truck'] = lambda : True if self._case >= 2 and self._case <= 8 else False 

        self.__trigger_add = {}
        # self.__trigger_add['unload_truck'] = lambda : True 

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
        #     for p in self._errors[0].pop(0):
        #         props.add(p)
        #     for p in self._errors[1].pop(0):
        #         props.add(p)
        #     self._time_to_fail = False
        #     self._n_errors -= 1
        # if self._counter == 4:
        #     props.add(Proposition(False, 'at', ['tru1', 'pos1']))
        #     props.add(Proposition(True, 'at', ['tru1', 'pos2']))
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
            if 'unload_truck' not in self.__trigger_remove or not self.__trigger_remove['unload_truck']():
                props.add(Proposition(False, 'in', [obj, vehicle]))
                props.add(Proposition(True, 'at', [obj, loc]))
            if 'unload_truck' in self.__trigger_add and self.__trigger_add['unload_truck']():
                props.add(Proposition(True, 'fake', [obj, vehicle]))
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
            if 'load_truck' not in self.__trigger_remove or not self.__trigger_remove['load_truck']():
                props.add(Proposition(False, 'at', [obj, loc])) 
                props.add(Proposition(False, 'in', [obj, vehicle]))
            if 'load_truck' in self.__trigger_add and self.__trigger_add['load_truck']():
                props.add(Proposition(True, 'fake', [obj, vehicle]))
        elif 'drive_truck' in action:
            l = 12
            i = action.index(',', l)
            j = action.index(',', i+1)
            k = action.index(',', j+1)
            vehicle = action[l:i]
            locfrom = action[i+1:j]
            locto = action[j+1:k]
            city = action[k+1:-1]
            # (and (not (at ?truck ?loc-from)) (at ?truck ?loc-to)))
            if 'drive_truck' not in self.__trigger_remove or not self.__trigger_remove['drive_truck']():
                props.add(Proposition(False, 'at', [vehicle, locfrom]))
                props.add(Proposition(True, 'at', [vehicle, locto]))
            if 'drive_truck' in self.__trigger_add and self.__trigger_add['drive_truck']():
                props.add(Proposition(True, 'fake', [vehicle]))
        elif 'fly_airplane' in action:
            l = 13
            i = action.index(',', l)
            j = action.index(',', i+1)
            vehicle = action[l:i]
            locfrom = action[i+1:j]
            locto = action[j+1:-1]
            # (and (not (at ?airplane ?loc-from)) (at ?airplane ?loc-to)))
            if 'fly_airplane' not in self.__trigger_remove or not self.__trigger_remove['fly_airplane']():
                props.add(Proposition(False, 'at', [vehicle, locfrom]))
                props.add(Proposition(True, 'at', [vehicle, locto]))
            if 'fly_airplane' in self.__trigger_add and self.__trigger_add['fly_airplane']():
                props.add(Proposition(True, 'fake', [vehicle]))
        self._case = self._case + 1
        callback(abstract_connector.ResultCode.SUCCESS, props)
    def set_errors_to_inject(self, v):
        self._n_errors = v
    # def set_time_to_fail(self, v):
    #     self._time_to_fail = v
    def get_actions_executed(self):
        return self._actions_executed

CONNECTOR = RawConnectorLogistics(raw_mapper.RawMapper())