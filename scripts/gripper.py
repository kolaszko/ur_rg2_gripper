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
        return NotImplementedError('')

    def close(self):
        return NotImplementedError('')


