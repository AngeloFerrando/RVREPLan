#!/usr/bin/env python

from __future__ import print_function

from gazebo_radiation_plugins.srv import Extinguish,ExtinguishResponse
import rospy

def handle_extinguish(req):
    # missing test to see if there is a fire here
    print("Ready to extinguish fire from [%s]."%req.waypoint)
    return ExtinguishResponse(True)

def extinguish_server():
    rospy.init_node('extinguish_server')
    s = rospy.Service('extinguish', Extinguish, handle_extinguish)
    print("Ready to extinguish fire.")
    rospy.spin()

if __name__ == "__main__":
    extinguish_server()
