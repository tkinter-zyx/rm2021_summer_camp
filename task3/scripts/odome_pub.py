#!/usr/bin/env python3

def reader():
    import csv
    import os
    path = os.path.abspath(__file__)
    path = path[:-12]
    path += "data.csv"
    print(path)
    data = []
    csvf = open(path, 'r')
    with csvf:
        original_data = csv.reader(csvf)
        for row in original_data:
            try:
                data.append([float(row[5]), float(row[7]), float(row[9]), float(row[11])])
            except ValueError:
                data.append([row[5], row[7], row[9], row[11]])
    data = data[1:465]
    data[0] = data[1] = [0, 0, 0, 0]
    return data

def speed(sensor_angular):
    vx = (-sensor_angular[0] + sensor_angular[1] + sensor_angular[2] - sensor_angular[3]) / 4.0
    vy = (-sensor_angular[0] - sensor_angular[1] + sensor_angular[2] + sensor_angular[3]) / 4.0
    angular = (-sensor_angular[0] - sensor_angular[1] - sensor_angular[2] - sensor_angular[3]) / 0.8
    return vx, vy, angular

import rospy
import roslib
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import math
data = reader()
rospy.init_node("odome_pub")
odom_pub = rospy.Publisher("odome", Odometry)
tf_broadcaster = tf.TransformBroadcaster()
x = 0.0
y = 0.0
th = 0.0
vx = 0
vy = 0
vth = 0
rate = rospy.Rate(100)
while 1:
    for i in range(len(data)):
        current_time = rospy.Time.now()
        vx, vy, vth = speed(data[i])
        x += (vx * math.cos(th) - vy * math.sin(th)) * 0.01
        y += (vx * math.sin(th) + vy * math.cos(th)) * 0.01
        th += vth * 0.01

        odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)
        tf_broadcaster.sendTransform([x, y, 0.0], odom_quat, current_time, "base_link", "odom")

        odom = Odometry()
        odom.header.stamp = current_time
        odom.header.frame_id = "odom"

        odom.pose.pose.position.x = x
        odom.pose.pose.position.y = y
        odom.pose.pose.position.z = 0.0
        odom.pose.pose.orientation.x = odom_quat[0]
        odom.pose.pose.orientation.y = odom_quat[1]
        odom.pose.pose.orientation.z = odom_quat[2]
        odom.pose.pose.orientation.w = odom_quat[3]

        odom.child_frame_id = "base_link"
        odom.twist.twist.linear.x = vx
        odom.twist.twist.linear.y = vy
        odom.twist.twist.angular.z = vth
    
        odom_pub.publish(odom)
        rate.sleep()