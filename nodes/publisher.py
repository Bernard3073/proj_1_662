#!/usr/bin/env python
import rospy
import sys
from geometry_msgs.msg import Twist
from std_msgs.msg import String

def publish_vel():
    vel = rospy.Publisher('/my_robot/mobile_base_controller/cmd_vel', Twist, queue_size=10)
    rospy.init_node('my_robot_move', anonymous=True)
    msg = Twist()
    msg.linear.x = 0.1
    msg.linear.y = 0
    msg.linear.z = 0
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        vel.publish(msg)
        rate.sleep()
    

if __name__ == '__main__':
    try:
        publish_vel()
    except rospy.ROSInterruptException:
        pass
