"""
30_6.py The date 100 days later is listed
"""
import datetime

deltaTime = datetime.timedelta(days=100)
timeNow = datetime.datetime.now()
print("now time:",timeNow)
print("Afther 100 days",timeNow + deltaTime)
