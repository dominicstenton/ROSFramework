#!/usr/bin/env python3
# a class used to calculate the speed of rpm

import rospy
from std_msgs.msg import Float32

rpm_num = 10

def rpm_pub():
    """rpm_pub summary.
    rpm_num begins with the value of 10 and increments in 5's until required
    """
    rospy.init_node("rpm_pub_node")
    pub = rospy.Publisher("rpm", Float32, queue_size=10)

    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        pub.publish(rpm_num)
        rate.sleep()

if __name__ == '__main__':
    try:
        rpm_pub()
    except rospy.ROSInterruptException:
        pass
