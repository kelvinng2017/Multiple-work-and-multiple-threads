"""
30_13.py This program will execute without waiting for Daemon threads to end and will terminate work on its own,since,
we no longer see Daemon outputs pertaining to other instances of execution
"""

import threading
import time

def daemonFun(): # define Daemon
    print(threading.currentThread().getName(),'Starting')
    time.sleep(5)
    print(threading.currentThread().getName(),'Exiting')
def non_daemon(): # define no Daemon
    print(threading.currentThread().getName(),'Starting')
    print(threading.current_thread().getName(),'Exiting')

d = threading.Thread(name='daemon',target=daemonFun) #createDaemon
d.setDaemon(True) #set to True
nd = threading.Thread(name='non-daemon',target=non_daemon) #creeate not Daemon

d.start()
nd.start()