"""
30_15.py This program executes because the worker thread joins(line 13), and the master thread waits for the worker thread to finish berforee
starting work
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
w.join() #Worker thread executes until the job is complete
print('end join')