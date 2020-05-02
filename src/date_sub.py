#!/usr/bin/env python

import rospy

from std_msgs.msg import String

#from datetime import datetime

def callback(msg):
    print msg.data


rospy.init_node('date_sub')

sub = rospy.Subscriber('datett', String, callback)

rospy.spin()