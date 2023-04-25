from connectors import abstract_connector
from data.proposition import Proposition
from time import sleep

class RawConnector(abstract_connector.AbstractConnector):
    def __init__(self, mapper):
        self._mapper = mapper
        self._case = 0

    def get_initial_propositions(self):
        return set()
        # props = set()
        # props.add(Proposition(False, 'radiation', ['cell0']))
        # props.add(Proposition(False, 'radiation', ['cell1']))
        # props.add(Proposition(False, 'radiation', ['cell2']))
        # props.add(Proposition(False, 'radiation', ['cell3']))
        # props.add(Proposition(False, 'radiation', ['cell4']))
        # props.add(Proposition(False, 'radiation', ['cell5']))
        # props.add(Proposition(False, 'radiation', ['cell6']))
        # props.add(Proposition(False, 'radiation', ['cell7']))
        # props.add(Proposition(False, 'radiation', ['cell8']))
        # props.add(Proposition(False, 'inspected', ['tank1']))
        # props.add(Proposition(False, 'inspected', ['tank2']))
        # props.add(Proposition(True, 'robot_at', ['rover', 'cell0']))
        # props.add(Proposition(True, 'right', ['cell0', 'cell1']))
        # props.add(Proposition(True, 'empty', ['cell1']))
        # props.add(Proposition(False, 'empty', ['cell0']))
        # return props

    def perform(self, action, callback):
        action = (self._mapper.mapActionToCommand(action))
        sleep(1) # simulate cmd execution
        props = set()
        action = str(action)
        if 'act_up' in action or 'act_down' in action or 'act_right' in action or 'act_left' in action:
            if 'act_up' in action:
                l = 7
            elif 'act_down' in action:
                l = 9
            elif 'act_right' in action:
                l = 10
            elif 'act_left' in action:
                l = 9
            i = action.index(',', l)
            j = action.index(',', i+1)
            rover = action[l:i]
            cell0 = action[i+1:j]
            cell1 = action[j+1:-1]
            props.add(Proposition(False, 'robot_at', ['rover', cell0]))
            props.add(Proposition(True, 'robot_at', ['rover', cell1]))
            props.add(Proposition(False, 'empty', [cell1]))
            props.add(Proposition(True, 'empty', [cell0]))
        if 'act_inspect_up' in action or 'act_inspect_down' in action or 'act_inspect_right' in action or 'act_inspect_left' in action:
            if 'act_inspect_up' in action:
                l = 15
            elif 'act_inspect_down' in action:
                l = 17
            elif 'act_inspect_right' in action:
                l = 18
            elif 'act_inspect_left' in action:
                l = 17
            # (act_inspect-down rover cell5 cell8 tank2)
            i = action.index(',', l)
            j = action.index(',', i+1)
            k = action.index(',', j+1)
            rover = action[l:i]
            cell0 = action[i+1:j]
            cell1 = action[j+1:k]
            tank = action[k+1:-1]
            props.add(Proposition(True, 'inspected', [tank]))
            props.add(Proposition(True, 'radiation', ['cell7']))

        # if self._case == 0:
        #     props.add(Proposition(False, 'robot_at', ['rover', 'cell0']))
        #     props.add(Proposition(False, 'empty', ['cell1']))
        #     props.add(Proposition(True, 'robot_at', ['rover', 'cell1']))
        #     props.add(Proposition(True, 'empty', ['cell0']))
        #     props.add(Proposition(True, 'tank_at', ['tank1', 'cell2']))
        #     props.add(Proposition(True, 'right', ['cell1', 'cell2']))
        # elif self._case == 1:
        #     props.add(Proposition(True, 'inspected', ['tank1']))
        #     props.add(Proposition(True, 'down', ['cell1', 'cell4']))
        #     props.add(Proposition(True, 'empty', ['cell4']))
        # elif self._case == 2:
        #     props.add(Proposition(True, 'robot_at', ['rover', 'cell4']))
        #     props.add(Proposition(False, 'robot_at', ['rover', 'cell1']))
        #     props.add(Proposition(False, 'empty', ['cell4']))
        #     props.add(Proposition(True, 'empty', ['cell1']))
        #     props.add(Proposition(True, 'down', ['cell4', 'cell7']))
        #     props.add(Proposition(True, 'empty', ['cell7']))
        #     props.add(Proposition(True, 'radiation', ['cell7']))
        # elif self._case == 3:
        #     props.add(Proposition(True, 'robot_at', ['rover', 'cell7']))
        #     props.add(Proposition(False, 'robot_at', ['rover', 'cell4']))
        #     props.add(Proposition(True, 'empty', ['cell4']))
        #     props.add(Proposition(False, 'empty', ['cell7']))
        #     props.add(Proposition(True, 'tank_at', ['tank2', 'cell8']))
        #     props.add(Proposition(True, 'right', ['cell7', 'cell8']))
        # elif self._case == 4:
        #     props.add(Proposition(True, 'inspected', ['tank2']))
        self._case = self._case + 1
        callback(props)
