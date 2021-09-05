"""
30_5.py redesign 30_4.py to convert a period of time into a second book
"""
import datetime

deltaTime = datetime.timedelta(days=3,hours=5,minutes=8,seconds=10)
print(deltaTime.days,deltaTime.seconds,deltaTime.microseconds)