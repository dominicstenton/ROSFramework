# a class that prints hello world
# this class has no methods

import rospy


if __name__ == '__main__':
    rospy.init_node('my_first_python_node')
    rospy.loginfo('node is running')

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo('hello world')
        rate.sleep()
