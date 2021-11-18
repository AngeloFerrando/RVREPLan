#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from gazebo_radiation_plugins.srv import *

def extinguish_client(w):
    rospy.wait_for_service('extinguish')
    try:
        extinguish = rospy.ServiceProxy('extinguish', Extinguish)
        resp1 = extinguish(w)
	if resp1.result == True:
		print("Fire from [%s] extinguished."%w)
	else:
		print("Fire from [%s] NOT extinguished."%w)
        return resp1.result
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    extinguish_client("Waypoint 5")
