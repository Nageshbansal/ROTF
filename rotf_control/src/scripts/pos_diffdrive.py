#!/usr/bin/env python

from logging import error
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Twist
import math

x =0.0
y = 0.0
v_x = 0.0 
v_y = 0.0
w_z = 0
err = 0.0

tim = 0.0
kp , kd ,ki = 2 , 0.0 , 0.0 
prev_time = 0.0 
dt = 0.0 



def cal_pos(msg):
    global x
    global y
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    # print(x)

    
def cal_vel(msg):
    global v_x
    global v_y
    global w_z
    v_x = msg.twist.twist.linear.x
    v_y = msg.twist.twist.linear.y
    w_z =  msg.twist.twist.angular.z
  
    

def pid(v_x,v_y):
   global err
   corr = 0.0
   global tim
   tim = rospy.Time.now()
   err = v_x - 0.1
   prev_error =0.0
   d_error = err - prev_error
  
   corr = kp*(err) 
   prev_error = err
   return (corr)


rospy.init_node('pos_diffdrive')
sub1 = rospy.Subscriber('/odom',Odometry,cal_pos)
sub2 = rospy.Subscriber('/odom',Odometry,cal_vel)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate =rospy.Rate(2)

move = Twist()

v =0.5
d =5




while not rospy.is_shutdown():
    x_goal=d
    if x_goal-x <= 0:
        
        move.linear.x = 0
        move.linear.y =0 
        move.angular.z = 0
        print("stopped")
        
    else:
        # move.linear.x =(x_goal-x)
        # move.linear.y = 0
        corr = pid(v_x,v_y)
        move.linear.x =corr*-10
        move.linear.y =0.0
        print(move.linear.x)

        
    pub.publish(move)
    rate.sleep()


    