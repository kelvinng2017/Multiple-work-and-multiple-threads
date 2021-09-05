"""
30_11.py The thread is created and the thread name is exhausted
"""

import threading
import time

def worker():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(),'Exiting')

def manager():
    print(threading.current_thread().getName(),'Starting')
    time.sleep(3)
    print(threading.current_thread().getName(),'Exiting')

m = threading.Thread(target=manager)
w = threading.Thread(target=worker)
m.start()
w.start()