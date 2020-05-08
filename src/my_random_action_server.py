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
    print('do_timer starts')
    start_time = time.time()
    update_count = 0
    even_count = 0

    rand_number = 0

    if goal.end_number > 10:
        print('action aborted')
        result = mytimerResult()
        result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        result.updates_sent = update_count
        result.even_number = even_count
        server.set_aborted(result,"Action aborted due to too large number")
        return
    
    if goal.end_number < 1:
        print('action aborted')
        result = mytimerResult()
        result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        result.updates_sent = update_count
        result.even_number = even_count
        server.set_aborted(result,"Action aborted due to too small number")
        return        
    
    print('action continues')

    while rand_number != goal.end_number:
            
        rand_number = randint(1,10) #random.randint made error
        print('random number: %d'%rand_number)

        if rand_number%2 == 0:
            even_count += 1
            print('even_count: %d'%even_count)

        print('before preempt')
        if server.is_preempt_requested():
            print('action preempt')
            result = mytimerResult()
            result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
            result.updates_sent = update_count
            result.even_number = even_count
            server.set_preempted(result, "Action preempted")
            return

        print('feedback sent')
        feedback = mytimerFeedback()
        feedback.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        feedback.recent_number = rand_number
        feedback.even_number = even_count
        server.publish_feedback(feedback)
        
        update_count += 1

        time.sleep(1.0)

    print('result sent')
    result = mytimerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = update_count
    result.even_number = even_count
    server.set_succeeded(result,"Action completed successfully")

rospy.init_node('my_timer_action_server')
server = actionlib.SimpleActionServer('my_action',mytimerAction,do_timer,False)
server.start()
rospy.spin()