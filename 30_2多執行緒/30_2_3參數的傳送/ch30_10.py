"""
30_10.py the appliaction of a thread calling function to pass parameters
"""
import threading,time

def wakeup(name,blessingWord):
    print("ThreadObj execution sequence starts") 
    time.sleep(10) #ThereadObj Actuator rests for 10 seconds
    print(name," ",blessingWord)
    print("ThreadObj execution sequence stop")

print("program stahe 1")
threadObj = threading.Thread(target=wakeup,args=["NaNa","HappyBrithday"])
threadObj.start() # ThereadObj Thread starts working
time.sleep(1) # The main thread rests for 1 second
print("program stahe 2")
