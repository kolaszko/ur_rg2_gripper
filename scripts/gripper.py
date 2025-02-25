#!/usr/bin/env python

import rospy
from ur_msgs.srv import *

class Gripper:

    def __init__(self, service='/ur_driver/set_io'):
        rospy.wait_for_service(service)
        try:
            self.set_io = rospy.ServiceProxy(service, SetIO)
            print('Connected with service')
        except rospy.ServiceException as e:
            print('Service unavailable: %s'%e)

    def open(self):
        self.set_io(1, 16, 0)

    def close(self):
        self.set_io(1, 16, 1)

    def set_strong_grip(self):
        self.set_io(1, 17, 0)

    def set_soft_grip(self):
        self.set_io(1, 17, 1)


