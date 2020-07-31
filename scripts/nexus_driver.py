#!/usr/bin/env python

import rospy
import serial
from geometry_msgs.msg import Twist

def callback(twist):
	lin_vel_x = twist.linear.x
	ang_vel_z = twist.angular.z
	ser = serial.Serial('/dev/ttyUSB0', 19200)

	#pub = rospy.Publisher('nexus/cmd_vel', Twist, queus_size=1)

	ser.write((int(lin_vel_x)).to_bytes(2, byteorder='big'))
	#ser1 = serial.Serial('/dev/ttyUSB0', 19200)
	#s = ser1.read(100)
	#ser1.close()
	
	rospy.spin()
	ser.close()

	
	'''while not rospy.is_shutdown():
		ser = serial.Serial('/dev/ttyYSB0', 19200, timeout=60)
		s = ser.read(100)
		print(s)
		ser.close()'''
	
	'''while not rospy.is_shutdown():
		#ser.write(int(lin_vel_x))
		#ser.write(bytes(int(lin_vel_x)))
		#ser.write((int(lin_vel_x)).to_bytes(2, byteorder='big'))
		ser.write((int(lin_vel_x)).to_bytes(2, byteorder='big'))'''
	
	
def nexus_driver():

	#pub = rospy.Publisher('nexus/cmd_vel', Twist, queue_size=1)
	#move_cmd = Twist()
	#move_cmd.linear.x = 100
	#move_cmd.angular.z = 0

	rospy.init_node('nexus_driver', anonymous=True)
	rospy.Subscriber('nexus/cmd_vel', Twist, callback)
	
	"""rate = rospy.Rate(5)
	while not rospy.is_shutdown():
		pub.publish(move_cmd)
		rate.sleep()"""
	while not rospy.is_shutdown():
		rospy.spin()
	
if __name__ == '__main__':
	nexus_driver()
