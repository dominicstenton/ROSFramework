#!/usr/bin/env python3
# a class that
# import math

import rospy
import actionlib

from my_robot_tutorial.msg import Navigate2DAction, Navigate2DFeedback, Navigate2DResult, Navigate2DGoal
from geometry_msgs.msg import Point

def feedback_callback(feedback):
    """feedback_callback summary.

    Parameters
    ----------
    feedback : type
        feedback prints distance_to_point.
    """
    print("Distance to Goal: " + str(feedback.distance_to_point))

def nav_client(user_coords):
    """nav_client summary.

    Parameters
    ----------
    user_coords : type
        User inputted start position coordinates.

    Returns
    -------
    type
        client returns get_result.
    """
    client = actionlib.SimpleActionClient("navigate_2D_action", Navigate2DAction)
    client.wait_for_server()
    point_msg = Point(x = user_coords[0], y = user_coords[1], z = user_coords[2])
    goal = Navigate2DGoal(point_msg)
    client.send_goal(goal, feedback_cb = feedback_callback)
    client.wait_for_result()

    return client.get_result

if __name__ == '__main__':
    try:
        rospy.init_node("navigate_2D_action_client_node")
        user_x = input("What is your desired x-coordinates?: ")
        user_y = input("What is your desired y-coordinates?: ")
        user_z = input("What is your desired z-coordinates?: ")

        user_coords = [float(user_x), float(user_y), float(user_z)]

        result = nav_client(user_coords)
        print(result)

    except rospy.ROSInterruptException:
        print("Program Interrutped")
