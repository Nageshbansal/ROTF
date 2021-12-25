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
kp , kd ,ki = 2.5 , 0.0 , 0.0 
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
    # print(v_x,v_y,w_z)
    

def pid(v_x,v_y):
   global err
   corr = 0.0
   global tim
   tim = rospy.Time.now()
   err_1 = v_x - 0.1
   err_2 =  v_y - 0.0 
   prev_error_1 =0.0
   prev_error_2 =0.0

  
   corr_1 = kp*(err_1)
   corr_2 = kp*err_2 
   prev_error = err
   return (corr_1,corr_2)


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
    move.angular.z= 0
    if x_goal-x <= 0:
        
        move.linear.x = 0
        move.linear.y =0 
        move.angular.z = 0
        print("stopped")
        
    else:
        # move.linear.x =(x_goal-x)
        # move.linear.y = 0
        corr_1 , corr_2 = pid(v_x,v_y)
        move.linear.x =corr_1*-10
        move.linear.y =corr_2*-10
       
        # print(move.linear.x)

    move.angular.z = 0.0   
    pub.publish(move)
    rate.sleep()


    