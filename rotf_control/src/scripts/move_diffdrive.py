#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher') # defining the ros node - publish_node
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate =rospy.Rate(2) # frequency at which publishing
move=Twist()
R=0
l=10
move.angular.x = 0.0
move.angular.y = 0.0
move.angular.z = 2.0

move.linear.x =(R+l/2)
move.linear.y = move.angular.y*(R+l/2)
# move.linear.y = 0.0
# move.linear.z = 0.0

  
while not rospy.is_shutdown():
	pub.publish(move)
	rate.sleep()
