#!/usr/bin/env python

from gripper import Gripper

class RG2(Gripper):
    def __init__(self, service):
        Gripper.__init__(self, service)

    def open(self):
        self.set_io(1, 16, 0)

    def close(self):
        self.set_io(1, 16, 1)

    def set_strong_grip(self):
        self.set_io(1, 17, 0)

    def set_soft_grip(self):
        self.set_io(1, 17, 1)