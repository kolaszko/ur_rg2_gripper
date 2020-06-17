#!/usr/bin/env python

import rospy
from gripper import Gripper
from std_msgs.msg import String


class GripperNode:

    def __init__(self, service='/ur_driver/set_io'):
        self.gripper = Gripper(service)
        rospy.init_node('gripper_node', anonymous=True)
        self.subscriber = rospy.Subscriber('/gripper/command', String, self.callback, queue_size=1)
        self.time_wait = 0
        print('Created gripper_node')
        rospy.spin()


    def callback(self, data):
        if data.data == 'open':
            self.gripper.open()
        elif data.data == 'close':
            self.gripper.close()
        elif data.data == 'softGrip':
            self.gripper.set_soft_grip()
        elif data.data == 'strongGrip':
            self.gripper.set_strong_grip()


if __name__ == '__main__':
    node = GripperNode()
        
