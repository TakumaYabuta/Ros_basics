#! /usr/bin/env python
# BEGIN ALL
#! /usr/bin/env python
import rospy

import time
import actionlib
#自分の作ったアクションファイル名がメッセージの型として自動生成される
from basics.msg import mytimerAction, mytimerGoal, mytimerResult, mytimerFeedback