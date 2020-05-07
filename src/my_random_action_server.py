#! /usr/bin/env python
# BEGIN ALL
#! /usr/bin/env python
import rospy
from random import random, randint
import time
import actionlib
# the name of action file becomes the name of msg type automatically.
from basics.msg import mytimerGoal, mytimerResult, mytimerFeedback, mytimerAction

def do_timer(goal):
    start_time = time.time()
    update_count = 0
    even_count = 0

    rand_number = 0

    if goal.end_number > 10:
        if goal.end_number < 1:
            result = mytimerResult()
            result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
            result.updates_sent = update_count
            result.even_number = even_count
            server.set_aborted(result,"Action aborted due to too small or large number")
            return
        
    while rand_number != goal.end_number:
            
        rand_number = randint(1,10) #random.randint made error
        if rand_number%2 == 0:
            even_count += 1

        if server.is_preempt_requested():
            result = mytimerResult()
            result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
            result.updates_sent = update_count
            result.even_number = even_count
            server.set_preempted(result, "Action preempted")
        return

        feedback = mytimerFeedback()
        feedback.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        feedback.recent_number = rand_number
        feedback.even_number = even_count
        server.publish_feedback(feedback)
        
        update_count += 1

        time.sleep(1.0)

    result = mytimerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = update_count
    result.even_number = even_count
    server.set_succeeded(result,"Action completed successfully")

rospy.init_node('my_timer_action_server')
server = actionlib.SimpleActionServer('timer',mytimerAction,do_timer,False)
server.start()
rospy.spin()