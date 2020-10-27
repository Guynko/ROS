#!/usr/bin/env python

import rospy
from moveit_commander.move_group import MoveGroupCommander

rospy.init_node('ros4pro_custom_node')
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    commander = MoveGroupCommander("arm_and_finger")
    commander.set_pose_target([0.00, 0.079, 0.220] + [0.871, -0.014, 0.079, 0.484])
    commander.go()
    commander.set_joint_value_target([0, 0, 0, 0, 0, 0])
    commander.go()
    rate.sleep()
