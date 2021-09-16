#/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
30_25.py 生產這和消費者的設計，這個程式有producer()方法敘述生產者運作的方式，基本上是需要生產5筆資料
(在data 串列)才讓自己進入睡眠模式，然後通知其它執行緒再解鎖。consumer方法則是當data串列沒有資料時，
才讓自己進入睡眠狀態，然後通知其它執行緒，再解鎖。這個程式首先建立threadingCondition(),然後設定資源串列
data是空行的程式接著是建立執行緒與啓動執行緒。由producer和consumer方法皆是一個無限迴圈所以程式將繼續執行
"""
import threading,time,random
def producer():#生產者狀況
    while True:
        condition.acquire() #鎖定
        if len(data) >=5: #如果產品滿了
            print("生產線是waiting...")
            condition.wait() #生產者等待
        else:
            data.append(random.randint(1,100)) #將產品放入庫存
            print("生產線庫存        ",data) #列印庫存
            time.sleep(1)
        condition.notify()#通知
        condition.release()#解鎖

def consumer():#消費者狀況
    while True:
        condition.acquire() #鎖定
        if not data: #如果沒有產品
            print("消費者是  waiting...")
            condition.wait() #消費者等待
        else:
            print("消費者取走商品:",data.pop(0))
            print("目前庫存     ",data) #列印庫存
            time.sleep(1)
        condition.notify()#通知
        condition.release()#解鎖

condition = threading.Condition() #建立Condition物件
data = [] #最初始化庫存

p = threading.Thread(name='producer',target=producer) #建立producer執行緒
c = threading.Thread(name='consumer',target=consumer) #建立consumer執行緒

p.start()
c.start()

p.join()
c.join()

