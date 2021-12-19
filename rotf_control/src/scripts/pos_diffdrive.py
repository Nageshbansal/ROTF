#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Twist

x =0.0
y = 0.0
def cal_pos(msg):
    global x
    global y
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    print(x)

    

rospy.init_node('pos_diffdrive')
sub = rospy.Subscriber('/odom',Odometry,cal_pos)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate =rospy.Rate(2)

move = Twist()

v =0.5
d =5

move.angular.x = 0.0
move.angular.y = 0.0
move.angular.z = 0.0


while not rospy.is_shutdown():
    x_goal=d
    if x_goal-x >= 0:
        
        move.linear.x =(x_goal-x)/10
        move.linear.y = 0
        
    else:
        move.linear.x = 0
        move.linear.y =0

    pub.publish(move)
    rate.sleep()


    