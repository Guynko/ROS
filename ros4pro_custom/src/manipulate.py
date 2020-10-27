#!/usr/bin/env python

import rospy
from moveit_commander.move_group import MoveGroupCommander
rospy.init_node('ros4pro_custom_node')
rate = rospy.Rate(1)
from geometry_msgs.msg import PoseStamped
from moveit_commander.planning_scene_interface import PlanningSceneInterface

scene = PlanningSceneInterface()
rospy.sleep(1)

ps = PoseStamped()
ps.header.frame_id = "base_link"
ps.pose.position.x = 0
ps.pose.position.y = -0.25
ps.pose.position.z = 0.15
ps.pose.orientation.w = 1
scene.add_box("boite_de_cereales", ps, (0.08, 0.24, 0.3))

rospy.sleep(1)

while not rospy.is_shutdown():
    rospy.loginfo("Hello world from our new node!")
    commander = MoveGroupCommander("arm_and_finger")
    commander.set_pose_target([0.00, 0.079, 0.220] + [0.871, -0.014, 0.079, 0.484])
    commander.go()
    commander.set_joint_value_target([0, 0, 0, 0, 0, 0])
    commander.go()
    rate.sleep()
