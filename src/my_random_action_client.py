#! /usr/bin/env python
# BEGIN ALL
#! /usr/bin/env python
import rospy

import time
import sys
import actionlib
# the name of action file becomes the name of msg type automatically.
from basics.msg import mytimerGoal, mytimerResult, mytimerFeedback, mytimerAction

def feedback_mytimer(feedback):
    print('[Feedback time] Time elapsed: %f'%(feedback.time_elapsed.to_sec()))
    print('[Feedback number] Recent number: %d'%(feedback.recent_number))
    print('[Feedback evenNo.] Even number appearance: %d'%(feedback.even_number))

rospy.init_node('my_timer_action_client')
client = actionlib.SimpleActionClient('timer',mytimerAction)
client.wait_for_server()

goal = mytimerGoal()
numb_get = sys.argv[1:]
goal.end_number = int(''.join(numb_get))

client.send_goal(goal, feedback_mytimer=feedback_mytimer)

client.wait_for_result()

print('[Result] State: %d'%(client.get_state())) # state is identified by No.１〜４
print('[Result] Status: %s'%(client.get_goal_status_text()))# status is defined by server.
print('[Result time] Time elapsed: %f'%(client.get_result().time_elapsed.to_sec()))
sent_updates = client.get_result().updates_sent
print('[Result updates] Updates sent: %d'%(sent_updates))
number_even = client.get_result.even_number
print('[Result evenNo.] Even number appearance: %d'%(number_even))

if sent_updates == 0:
    ratio_even = 0
else:
    ratio_even = float(number_even) / float(sent_updates)

print('[Result ratio] Ratio of even number: %f'%(ratio_even*100.0))