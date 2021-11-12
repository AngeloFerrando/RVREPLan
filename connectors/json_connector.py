from connectors import abstract_connector
import websocket
import json

class JsonConnector(abstract_connector.AbstractConnector):
    def __init__(self, end_node):
        websocket.enableTrace(True)
        self._ws = websocket.WebSocketApp(end_node,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close)
        ws.run_forever()

    def _on_message(ws, message):
        if self.callback:
            propositions_dict = json.loads(message)
            props = set()
            for prop in propositions_dict:
                props.add(Proposition(prop['truth'], prop['functor'], prop['args']))
            self.callback(props)
            
    def _on_error(ws, error):
        print(error)

    def _on_close(ws, close_status_code, close_msg):
        print('### closed ###')

    def _on_open(ws):
        print('### open ###')

    def perform(self, action, callback):
        ws.send(action.toJSON())
        self.callback = callback
