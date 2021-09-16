"""
30_16.py  The redesigned 30_15.py design has a wait time of 1.5 seconds
at which point the master thread will revert to work,so you'll see 
in the result of execution that the End Point string is printed first and worker No longer printed

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
w.join(1.5) #Worker thread executes until the job is complete
print('end join')