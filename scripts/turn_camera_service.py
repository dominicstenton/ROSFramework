#!/usr/bin/env python3
# a class that

import rospy
from my_robot_tutorial.srv import TurnCamera, TurnCameraResponse
import numpy as np
import os
import cv2
from cv_bridge import CvBridge

class TurnCameraClass:
    """TurnCameraClass ummary.

    Attributes
    ----------
    available_angles : type
        Description of attribute `available_angles`.
    ros_service : type
        Description of attribute `ros_service`.
    send_image : type
        Description of attribute `send_image`.

    """
    def __init__(self):
        """__init__ summary.
        Initialising the avaialable parameters for the camera
        """
        self.available_angles = [-30, -15, 0, 15, 30]
        self.ros_service = rospy.Service("turn_camera", TurnCamera, self.send_image)

    def read_in_image_by_file_name(self, file_name):
        """read_in_image_by_file_name summary.

        Parameters
        ----------
        file_name : type
            Description of parameter `file_name`.

        Returns
        -------
        type
            Description of returned object.

        """
        dir_name = os.path.dirname(__file__)
        file_location = dir_name + "/Images/" + file_name
        image = cv2.imread(file_location)
        return image

    def get_image(self, angle):
        """get_image summary.

        Parameters
        ----------
        angle : type
            Description of parameter `angle`.

        Returns
        -------
        type
            Description of returned object.

        """
        closest_angle = min(self.available_angles, key=lambda x:abs(x-angle))
        return self.read_in_image_by_file_name(str(closest_angle) + ".png")

    def send_image(self, req):
        """send_image summary.

        Parameters
        ----------
        req : type
            Description of parameter `req`.

        Returns
        -------
        type
            Description of returned object.

        """
        image = self.get_image(req.turn_degrees)
        image_msg = CvBridge().cv2_to_imgmsg(image)
        return TurnCameraResponse(image_msg)


if __name__ == '__main__':
    try:
        rospy.init_node("turn_camera_service_node")
        TurnCameraClass()
        print("Turn Camera Service is Running")
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
