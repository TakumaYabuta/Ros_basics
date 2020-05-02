#!/usr/bin/env python

import rospy

from datetime import datetime

from std_msgs.msg import String

rospy.init_node('date_pub')
pub = rospy.Publisher('datett',String, queue_size=10)

rate = rospy.Rate(0.5)

while not rospy.is_shutdown():
    datet = datetime.now()
    #timestamp = np.array([datet.year,datett.])
    datett = "hello world %s-%s-%s-%s-%s-%s" % (str(datet.year),str(datet.month),str(datet.day),str(datet.hour),str(datet.minute),str(datet.second)) #timestamp
    pub.publish(datett)
    #rospy.loginfo(datett)
    print datett
    rate.sleep()