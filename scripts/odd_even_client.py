#!/usr/bin/env python3
# a class that identifies odd and even numbers
# this class has no methods

import rospy
from my_robot_tutorial.srv import OddEvenCheck, OddEvenCheckResponse

if __name__ == '__main__':
        rospy.init_node("odd_even_client_node")
        srv_proxy = rospy.ServiceProxy("odd_even_check", OddEvenCheck)
        user_input = input("\nEnter a whole number: ")
        resp_obj = srv_proxy(int(user_input))
        answer = resp_obj.answer
        print(answer)
