"""
30_16.py  Extension design 30_16.py lists whether the child thread is still working when the master thread gains control
"""

import threading
import time 

def worker():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(),'Exiting')

w = threading.Thread(name='worker',target=worker)
w.start()
print('start join')
w.join(1.5) #wait 1.5 second for the worker execution sequence to complete the work before proceeding
print("Whether the working thread is still working?",w.isAlive())
time.sleep(2)
print("Whether the working thread is still working?",w.isAlive())
print('end join')