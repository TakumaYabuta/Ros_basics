#!/usr/bin/env python

import rospy

from basics.srv import odd_even

import sys

rospy.init_node('odd_even_client')

rospy.wait_for_service('judge_oddeven')

jud_odd_even = rospy.ServiceProxy('judge_oddeven',odd_even)
whattext = sys.argv[1:]
print whattext
print type(whattext)
numb_get = ''.join(whattext)
print numb_get
print type(numb_get)

numb = int(numb_get)#sys.argc[1:] #''.join(sys.argv[1:])

#judge_oddeven = jud_odd_even(numb)

print numb
print type(numb)
print '->'
#print judge_oddeven