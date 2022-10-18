from connectors import abstract_connector
import websocket
import json

class JsonConnector(abstract_connector.AbstractConnector):
    def __init__(self, end_node, mapper):
        self._mapper = mapper
        websocket.enableTrace(True)
        self._ws = websocket.WebSocketApp(end_node,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close)
        wst = threading.Thread(target=ws.run_forever)
        wst.daemon = True
        wst.start()

    def _on_message(ws, message):
        propositions = self._mapper.mapPerceptionsToPropositions(json.loads(message))
        if self._callback:
            self._callback(propositions)

    def _on_error(ws, error):
        print(error)

    def _on_close(ws, close_status_code, close_msg):
        print('### closed ###')

    def _on_open(ws):
        print('### open ###')

    def get_initial_propositions(self):
        return set()

    def perform(self, action, callback):
        ws.send(self._mapper.mapActionToCommand(action).toJSON())
        self._callback = callback
