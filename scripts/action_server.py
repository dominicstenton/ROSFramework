#!/usr/bin/env python3
# a class that

import math
import rospy
import actionlib

from my_robot_tutorial.msg import Navigate2DAction, Navigate2DFeedback, Navigate2DResult
from geometry_msgs.msg import Point

class Navigate2DClass:
    """Navigate2DClass summary.

    Attributes within this class
    ----------
    action_server : type
    navigate_cb : type
    robot_point_sub : type
    update_robot_position : type
    robot_current_point : type
    robot_goal_point : type
    distance_threshold : type
    feedback_rate : type
    """
    def __init__(self):
        """__init__ summary.

        Returns
        -------
        type
            self calls action_server, actionlib calls SimpleActionServer, SimpleActionServer prints navigate_2D_action
        """
        self.action_server = actionlib.SimpleActionServer("navigate_2D_action",
         Navigate2DAction, self.navigate_cb)

        self.robot_point_sub = rospy.Subscriber("robot/point", Point, self.update_robot_position)
        self.robot_current_point = None
        self.robot_goal_point = None
        self.distance_threshold = 0.35
        self.feedback_rate = rospy.Rate(1)

    def navigate_cb(self, goal):
        """navigate_cb summary.

        Parameters
        ----------
        goal : type
            User inputted goal position, specified between x, y and z coordinates.

        Returns
        -------
        type
            goal prints point.x, point.y and point.z
        """
        navigate_start_time = rospy.get_time()
        self.robot_goal_point = [goal.point.x, goal.point.y, goal.point.z]

        while self.robot_current_point == None:
            print("Robot Point Not Detected")
            rospy.sleep(5)

        print("Robot Point Detected")

        distance_to_goal = math.dist(self.robot_current_point, self.robot_goal_point)

        while distance_to_goal > self.distance_threshold:
            self.action_server.publish_feedback(Navigate2DFeedback(distance_to_point = distance_to_goal))
            self.feedback_rate.sleep()
            distance_to_goal = math.dist(self.robot_current_point, self.robot_goal_point)

        navigate_end_time = rospy.get_time()
        elasped_time = navigate_end_time - navigate_start_time
        rospy.loginfo("Navigation Successful, Elapsed Time: " + str(elasped_time) + "secs")
        self.action_server.set_succeeded(Navigate2DResult(elasped_time))

    def update_robot_position(self, point):
        """update_robot_position summary.

        Parameters
        ----------
        point : type
            self calls robot_current_point.

        Returns
        -------
        type
            robot_current_point returns point.x, point.y and point.z.
        """
        self.robot_current_point = [point.x, point.y, point.z]



if __name__ == '__main__':
    rospy.init_node("navigate_2D_action_server_node")
    server = Navigate2DClass()
    rospy.spin()
