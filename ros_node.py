#!/usr/bin/env python
import rospy
import json
from websocket_server import WebsocketServer
from gazebo_radiation_plugins.msg import Command

client = None

def new_client(c, server):
	client = c

def client_left(c, server):
	client = None

def message_received(c, server, message):
    global client
    message_dict = json.loads(message)
    pass # convert action to command (so, publish stuff..)
    client =  c
    # server.send_message(client, json.dumps(message_dict))

def main(args):
    rospy.init_node('ros_node', anonymous=True)
    # pub = rospy.Publisher(name = 'command', data_class = Command, latch = True, queue_size = 1000)
    # rospy.Subscriber('', , callback_front_scan)
    # Here we should add the publishers and subscribers.. But, we need a way to decide when is time to send a message to the connector.
    # For instance, when the last action performed is considered completed, then we can send a message with the propositions denoting
    # the current environment state.
    server = WebsocketServer(8080)
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received)
    server.run_forever()

if __name__ == '__main__':
    main(sys.argv)
