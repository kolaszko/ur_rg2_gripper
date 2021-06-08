#!/usr/bin/env python

import rospy
from gripper_erc import GripperErc
from std_msgs.msg import String


class GripperErcNode:

    def __init__(self, service='/ur_hardware_interface/set_io'):
        self.gripper = GripperErc(service)
        rospy.init_node('gripper_node', anonymous=True)
        self.subscriber = rospy.Subscriber('/gripper/command', String, self.callback, queue_size=1)
        self.time_wait = 0
        print('Created gripper_node')
        rospy.spin()

    def callback(self, data):
        if data.data == 'open':
            self.gripper.open()
        elif data.data == 'semi_open':
            self.gripper.semi_open()
        elif data.data == 'semi_close':
            self.gripper.semi_close()
        elif data.data == 'close':
            self.gripper.close()


if __name__ == '__main__':
    node = GripperErcNode()

