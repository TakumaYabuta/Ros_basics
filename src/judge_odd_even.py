#!/usr/bin/env python

import rospy

from basics.srv import odd_even

def jud_odd_even(request):
    if request%2 == 0 :
        oddeven = 'even'
    else:
        oddeven = 'odd'
    return oddeven


rospy.init_node('judge_odd_even')

judge = rospy.Service('judge_oddeven',odd_even,jud_odd_even)

rospy.spin()