#!/usr/bin/env python
import rospy
import math
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped
from racecar import racecar
import time
import numpy as np

class getAround:

	

	def __init__(self):

		# create Subscriber and initialize racecar class
		self.scanResult = rospy.Subscriber("/scan",LaserScan,self.callBack)
		self.car = racecar()

	def callBack(self,msg):

		'''
		MAGNITUDE_CONSTANT = .05
		FORWARD_FORCE = 60.0
		STEERING_CONSTANT = .8
		SPEED_CONSTANT = .05

		'''
		MAGNITUDE_CONSTANT = .05
		FORWARD_FORCE = 60.0
		STEERING_CONSTANT = .8
		SPEED_CONSTANT = .03
		
		
		#self.car.safety(msg.ranges)
		resultList = []
		for i in range(2,1078):				# creates array with 960 elements
			average = 0
			for j in range(-2,3):
				average = average+msg.ranges[i+j]	# averages 5 values together
			resultList.append(average/5)

		x_net = 0
		y_net = 0

<<<<<<< HEAD
		for i in range (0,1076):				
=======
		for i in range (0,720):
>>>>>>> 3bbe586e5957a47e39449a9db1f9b169fd372378
			distance = resultList[i]
			angle = (i - 538)/4

<<<<<<< HEAD
			magnitude = -MAGNITUDE_CONSTANT/(distance * distance)			# magnitude changes x_net and y_net
			
			x_net += np.cos(math.radians(angle)) * magnitude
			y_net += np.sin(math.radians(angle)) * magnitude
				
		
		x_net += FORWARD_FORCE

		print("X_NET: %f Y_NET: %f"%(x_net,y_net))

		steering_angle = STEERING_CONSTANT * math.atan2(y_net, x_net) * np.sign(x_net)
		speed = SPEED_CONSTANT * math.sqrt(x_net*x_net + y_net*y_net) * np.sign(x_net)
=======
			magnitude = -.05/(distance * distance)

			x_net += np.cos(math.radians(angle)) * magnitude
			y_net += np.sin(math.radians(angle)) * magnitude


		x_net += 35.0

		print("X_NET: %f Y_NET: %f"%(x_net,y_net))

		steering_angle = 1.0 * math.atan2(y_net,x_net) * np.sign(x_net)
		speed = .08 * math.sqrt(x_net*x_net + y_net*y_net) * np.sign(x_net)
>>>>>>> 3bbe586e5957a47e39449a9db1f9b169fd372378

		
		if(speed < 0):
			self.car.drive(-2.0, steering_angle)
			time.sleep(0.01)
		elif(speed > 5): 
			self.car.drive(5.0, steering_angle)
		else:
			self.car.drive(speed, steering_angle)

if __name__ == "__main__":
	rospy.init_node("getAround")
	getAround = getAround()
	rospy.spin()
