from connectors import abstract_connector
from data.proposition import Proposition
from time import sleep

class RawConnector(abstract_connector.AbstractConnector):
    def __init__(self, mapper):
        self._mapper = mapper

    def perform(self, action, callback):
        cmd = (self._mapper.mapActionToCommand(action))
        sleep(1) # simulate cmd execution
        props = set()
        props.add(Proposition(True, 'prop1', ['a', 1]))
        props.add(Proposition(False, 'prop2', ['b', 3]))
        props.add(Proposition(True, 'prop3', ['c']))
        callback(props)
