#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from math import *
rospy.init_node('move_diffdrive') # defining the ros node - publish_node
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
pub_r=rospy.Publisher('/m2wr/link_right_wheel_controller',Float64, queue_size=1 )
pub_l=rospy.Publisher('/m2wr/link_left_wheel_controller',Float64, queue_size=1)
rate =rospy.Rate(2) # frequency at which publishing
move=Twist()
l=0.4
move.linear.x = 0.5
move.angular.z = 0.5
omega=move.angular.z

velocity_l=move.linear.x+omega*l/2
velocity_r=-(move.linear.x-omega*l/2)


  
while not rospy.is_shutdown():
	pub.publish(move)
	print(move)
	pub_r.publish(velocity_r)
	pub_l.publish(velocity_l)
	rate.sleep()
