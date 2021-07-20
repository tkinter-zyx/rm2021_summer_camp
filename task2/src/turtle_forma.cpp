#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <geometry_msgs/Vector3.h>
#include <turtlesim/Pose.h>
#include <turtlesim/Spawn.h>
#include <cmath>
#include <sstream>
#include <iostream>

geometry_msgs::Vector3 linear[3];

void find_center(turtlesim::Pose A, turtlesim::Pose B, turtlesim::Pose C)
{
    float c = pow((A.x - B.x) * (A.x - B.x) + (A.y - B.y) * (A.y - B.y), 0.5);
    float a = pow((C.x - B.x) * (C.x - B.x) + (C.y - B.y) * (C.y - B.y), 0.5);
    float b = pow((A.x - C.x) * (A.x - C.x) + (A.y - C.y) * (A.y - C.y), 0.5);
    turtlesim::Pose M;
    M.x = (A.x * a + B.x * b + C.x * c) / (a + b + c);
    M.y = (A.y * a + B.y * b + C.y * c) / (a + b + c);
    linear[0].x = 1;
    linear[1].x = 1;
    linear[2].x = 1;
    linear[0].y = (M.y - A.y) / (M.x - A.x);
    linear[1].y = (M.y - B.y) / (M.x - B.x);
    linear[2].y = (M.y - C.y) / (M.x - C.x);
}

turtlesim::Pose find_turtle(int num)
{
    std::stringstream topic;
    topic << "/turtle" << num << "/pose";
    boost::shared_ptr<const turtlesim::Pose_<std::allocator<void>>> pose_now;
    pose_now = ros::topic::waitForMessage<turtlesim::Pose>(topic.str().c_str(), ros::Duration(3));
    turtlesim::Pose res;
    res.x = pose_now->x;
    res.y = pose_now->y;
    return res;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "round_publisher");
    ros::NodeHandle node;
    ros::service::waitForService("spawn");
    ros::ServiceClient add_turtle = node.serviceClient<turtlesim::Spawn>("spawn");
    turtlesim::Spawn srv;
    srv.request.x = 7.5;
    srv.request.y = 7.5;
    add_turtle.call(srv);
    srv.request.x = 3.0;
    srv.request.y = 7.5;
    add_turtle.call(srv);

    turtlesim::Pose pose1 = find_turtle(1);
    turtlesim::Pose pose2 = find_turtle(2);
    turtlesim::Pose pose3 = find_turtle(3);
    ros::Publisher turtle1_vel = node.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);
    ros::Publisher turtle2_vel = node.advertise<geometry_msgs::Twist>("/turtle2/cmd_vel", 10);
    ros::Publisher turtle3_vel = node.advertise<geometry_msgs::Twist>("/turtle3/cmd_vel", 10);
    geometry_msgs::Twist vel_msg;
    vel_msg.angular.z = 0;

    ros::Rate loop_rate(20);
    while(ros::ok())
    {
        find_center(pose1, pose2, pose3);
        vel_msg.linear = linear[0];
        turtle1_vel.publish(vel_msg);
        vel_msg.linear = linear[1];
        turtle2_vel.publish(vel_msg);
        vel_msg.linear = linear[2];
        turtle3_vel.publish(vel_msg);
        loop_rate.sleep();
    }
    return 0;
}