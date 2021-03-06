#!/usr/bin/env python


"""
PWallFollowNode(local).py

MIT RACECAR 2016

This program implements the bbWallFollow (bang bang
wall follow) method defined in the racecar.py class.

"""

# IMPORTS

import rospy
import math
from racecar import racecar
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped



# VARIABLES

DATA_THREAD = "/scan"
# CONTROLLER_THREAD = " "
NODE_NAME = 'PDWallFollow'

D_DESIRED = 0.2
SPEED = 1.0

SIDE = "L"
RACER = racecar()
TURN = "CCW"
FRONT_DISTANCE = .65


# CALLBACK

def callBack(msg):

    # Query for side
    # <implement here>
    
    # Query for safety
    #RACER.safety(msg.ranges)

    # Query for P Wall Follow Controller

    if(msg.ranges[540] < FRONT_DISTANCE):
		RACER.turn(msg.ranges, TURN)
		print("turn")
    else:
    	RACER.bothWallFollow(msg.ranges, SPEED)


# MAIN()      

rospy.init_node(NODE_NAME)
scanResult = rospy.Subscriber(DATA_THREAD,LaserScan,callBack)

#sideEntry = rospy.Subscriber("", ,)

rospy.spin()
