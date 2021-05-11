# a class that is on contact with the publisher class to collect data

import rospy
from std_msgs.msg import String

def process_hello_world_msg(data):
    """process_hello_world_msg summary.

    Parameters
    ----------
    data : type
        srt returns data.
    """
    print("message received: " + str(data))
def create_subscriber():
    """create_subscriber summary.
        this method creates a simple subscriber node
    """
    rospy.init_node("hello_world_sub_node")
    rospy.Subscriber("hello_world", String, process_hello_world_msg)


if __name__ == '__main__':
    create_subscriber()
    rospy.spin()
