#!/usr/bin/env python3
# a class that imlements the odd even client class  by returning it from another class

import rospy
from my_robot_tutorial.srv import OddEvenCheck, OddEvenCheckResponse

def check_number(req):
    """check_number summary.

    Parameters
    ----------
    req : type
        User inputted required number.

    Returns
    -------
    type
        OddEvenCheckResponse returns check.
    """
    if (req.number % 2) == 0:
        check = "even"
    else:
        check = "odd"

    return OddEvenCheckResponse(check)


if __name__ == '__main__':
    try:
        rospy.init_node("odd_even_service_node")
        rospy.Service("odd_even_check", OddEvenCheck, check_number)
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
