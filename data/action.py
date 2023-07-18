import json

class Action(object):
    def __init__(self, functor, args):
        self._functor = functor
        self._args = args
    def __str__(self):
        res = self._functor
        if self._args:
            aux_args = [str(arg) for arg in self._args]
            res = res + ',' + ','.join(aux_args)
        return res
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    def fromStrToAction(actionStr):
        actionStr = actionStr.replace('(', '').replace(')', '')
        firstComma = actionStr.index(' ', 0)
        action = Action(actionStr[0:firstComma], actionStr[firstComma+1:].split(' '))
        return action
