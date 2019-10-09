#!/usr/bin/env python
import rospy
import math
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import String

#write a class 
class Camera:
	def __init__(self):
		self.data = -1
		return None

	def callback(self,data):
	 #   rospy.loginfo((data))
		self.data = data.data
		#print data

	def publisher_node(self):
		cmd_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
		cmd_sub = rospy.Subscriber('color_mono', String, self.callback, queue_size=1)

		rospy.sleep(2)
		twist=Twist()
		init_t = rospy.get_time()
		rate = rospy.Rate(10)
			
		desired = 320 
		while rospy.get_time()-init_t < (35):
			actual = int(self.data)
			print actual
			error = desired - actual 
			if error < 0: 
				correction = -1 
			elif error > 0:
				correction = 1 
			else: 
				correction = 0 
			twist.linear.x = 0.03 
			print correction
			twist.angular.z = correction*0.12
			cmd_pub.publish(twist)
			rate.sleep()
			#rospy.loginfo(twist.angular.z
		twist.linear.x = 0
		twist.angular.z = 0
		rospy.loginfo(twist.linear.x)
		rospy.loginfo(twist.angular.z)

		print "HELLO"
		cmd_pub.publish(twist)
		pass


def main():
    data = 0
    try:
        rospy.init_node('motor')
	C = Camera()
        C.publisher_node()
    except rospy.ROSInterruptException:
        pass
    

if __name__ == '__main__':
    main()
