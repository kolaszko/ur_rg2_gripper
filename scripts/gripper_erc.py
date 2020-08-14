#!/usr/bin/env python

from gripper import Gripper


class GripperErc(Gripper):
    def __init__(self, service):
        Gripper.__init__(self, service)

    def open(self):
        self.set_io(1, 16, 0)
        self.set_io(1, 17, 0)

    def semi_open(self):
        self.set_io(1, 16, 0)
        self.set_io(1, 17, 0)

    def semi_close(self):
        self.set_io(1, 16, 0)
        self.set_io(1, 17, 0)

    def close(self):
        self.set_io(1, 16, 1)
        self.set_io(1, 17, 1)

