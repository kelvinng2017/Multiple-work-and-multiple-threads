#/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
30_22.py 重新設計ch30_21.py,但是取消第9和12行
"""

import threading

class MyThread(threading.Thread): #這是threading.Thread的子類別
    def __init__(self):
        threading.Thread.__init__(self) #建立執行緒
    def run(self):
        global data #定義全域資料
        #datalock.acquire() #鎖定
        data += 5
        print("data="+str(data))
        #datalock.release() #解鎖

data = 10 #全域最初值
datalock = threading.Lock() #建立物件
ts =[] #建立執行緒串列

for t in range(10):
    t = MyThread() #將執行緒加入執行緒串列
    ts.append(t)

for t in ts: #啓動所有執行緒
    t.start()

for t in ts: #等待所有執行緒推出
    t.join()