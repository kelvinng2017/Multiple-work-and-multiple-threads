"""
30_9.py Design a thread to perform work alone,and the program itself to perform work
"""

import threading,time

def wakeup():
    print("ThreadObj execution sequence starts") 
    time.sleep(10) #ThereadObj Actuator rests for 10 seconds
    print("girlfriend birthday")
    print("ThreadObj execution sequence stop")

print("program stahe 1")
threadObj = threading.Thread(target=wakeup)
threadObj.start() # ThereadObj Thread starts working
time.sleep(1) # The main thread rests for 1 second
print("program stahe 2")
