#!/usr/bin/env python3
# a class that

import rospy
from my_robot_tuorial.srv import TurnCamera, TurnCameraResponse
import numpy as np
import os
import cv2
from cv_bridge import CvBridge

def configure_request(angle):
    """configure_request summary.

    Parameters
    ----------
    angle : type
        Description of parameter `angle`.
    """
    rospy.wait_for_service("turn_camera")
    try:
        Service_proxy = rospy.ServiceProxy("turn_camera", TurnCamera)
        resp_msg = Service_proxy(angle)

        image_msg = resp_msg.image

        image = CvBridge().imgmsg_to_cv2(image_msg, desired_encoding="passthrough")
        cv2.imshow("Turn Camera Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except rospy.ServiceException as e:
        print("Service Request Failed \n")
        print(e)

if __name__ == '__main__':
    try:
        rospy.init_node("turn_camera_client_node")
        user_input = input("\n Enter an anglein degrees to move the robot Camera: ")

        while user_input != "q":
            try:
                configure_request(float(user_input))
                user_input = input("\n Enter an anglein degrees to move the robot Camera: ")

            except:
                print("Error trying to process request")


    except rospy.ROSInterruptException:
        pass
