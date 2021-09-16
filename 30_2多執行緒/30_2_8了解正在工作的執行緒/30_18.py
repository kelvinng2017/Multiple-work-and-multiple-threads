"""
30_18.py list the number of threads in work,and the names of those threads
"""

import threading
import time

def worker():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(5)
    print(threading.currentThread().getName(),'Exiting')

def manager():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(5)
    print(threading.currentThread().getName(),'Exiting')

w = threading.Thread(name='worker',target=worker)
w.start()
print('worker start join')
w.join(1.5) #wait 1.5 second for the worker thread to complete the work before proceeding
print('worker end join')
m = threading.Thread(name='mangager',target=worker)
m.start()
print('manager start join')
w.join(1.5) #wait 1,5 second for the manager thread to complete the work before proceeding
print("manager end join")
print("There are currently "+str(threading.active_count())+" threads working")
for thread in threading.enumerate():
    print("thread name:"+str(thread.name))