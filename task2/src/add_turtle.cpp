#include <ros/ros.h>
#include <turtlesim/Spawn.h>


int main(int argc, char **argv)
{
    ros::init(argc, argv, "round_publisher");
    ros::NodeHandle node;
    ros::service::waitForService("spawn");
    ros::ServiceClient add_turtle = node.serviceClient<turtlesim::Spawn>("spawn");
    turtlesim::Spawn srv;
    add_turtle.call(srv);
    return 0;
}