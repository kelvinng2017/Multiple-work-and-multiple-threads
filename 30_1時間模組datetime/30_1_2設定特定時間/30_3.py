"""
30_3.py setting program loopback to run until 10:30am 09/04/2021 will stop
print program is sleeping while printing wake up
"""
from __future__ import print_function
import datetime

timeStop = datetime.datetime(2021,9,4,10,26,0)
while datetime.datetime.now() <timeStop:
    print ("program is sleeping,",end="")
print ("Wake up")    

