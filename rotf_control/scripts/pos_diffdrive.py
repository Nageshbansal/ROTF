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
<<<<<<< HEAD:rotf_control/src/scripts/pos_diffdrive.py
kp , kd ,ki = 2.5 , 0.0 , 0.0 
=======
kp_x , kp_y ,kp_z = 2 , 1.0 , 1.0 
>>>>>>> 011e42d7bdcc9d3278b68972cb812411205b3967:rotf_control/scripts/pos_diffdrive.py
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
    

def pid(v_x,v_y,w_z):
   global err_x
   global err_y
   global err_z
   corr_x = 0.0
   corr_y=0.0
   corr_z=0.0
   global tim
   tim = rospy.Time.now()
<<<<<<< HEAD:rotf_control/src/scripts/pos_diffdrive.py
   err_1 = v_x - 0.1
   err_2 =  v_y - 0.0 
   prev_error_1 =0.0
   prev_error_2 =0.0

  
   corr_1 = kp*(err_1)
   corr_2 = kp*err_2 
   prev_error = err
   return (corr_1,corr_2)
=======
   err_x = v_x - 0.1
   err_y=v_y
   err_z=w_z
   
   prev_error_x =0.0
   prev_error_y=0.0
   prev_error_z=0.0
   #d_error_x = err_x - prev_error_x
   #d_error_y=err_y-prev_error_y
   #d_error_z=err_z-prev_error_z
  
   corr_x = kp_x*(err_x) 
   corr_y=kp_y*(err_y)
   corr_z=kp_z*(err_z)
   correction=[corr_x,corr_y,corr_z]
   prev_error_x= err_x
   prev_error_y=err_y
   prev_error_z=err_z
   return (correction)
>>>>>>> 011e42d7bdcc9d3278b68972cb812411205b3967:rotf_control/scripts/pos_diffdrive.py


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
<<<<<<< HEAD:rotf_control/src/scripts/pos_diffdrive.py
        corr_1 , corr_2 = pid(v_x,v_y)
        move.linear.x =corr_1*-10
        move.linear.y =corr_2*-10
       
        # print(move.linear.x)
=======
        corr = pid(v_x,v_y,w_z)
        move.linear.x =corr[0]*(-10)
        move.linear.y=corr[1]*(-10)
        move.angular.z=corr[2]*(0.01)
        move.linear.y =0.0
        print(move.linear.x)
>>>>>>> 011e42d7bdcc9d3278b68972cb812411205b3967:rotf_control/scripts/pos_diffdrive.py

    move.angular.z = 0.0   
    pub.publish(move)
    rate.sleep()


    