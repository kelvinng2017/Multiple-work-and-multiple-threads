"""
30_19.py Test the self-defined execution sequence A and stat run()
The test results show that the self-defined execution sequemce B 
can be normally executed. Start() once, and the test results show
that the self-defined execution sequence B can be normally excuted
"""

import threading
class MyThread(threading.Thread): #This is a subclass of threading Thread
    def __init__(self):
        threading.Thread.__init__(self)#create thread
    def run(self):#The work of defining threads
        print(threading.Thread.getName(self))
        print("Happy Python")

a = MyThread() #create thread object A
a.run() #Start thread A
a.run()
b = MyThread() #create thread object B
b.start()
b.start()