"""
print the number of days,seconds and millionths of a second for a period of time
"""
import datetime

deltaTime = datetime.timedelta(days=3,hours=5,minutes=8,seconds=10)
print(deltaTime.days,deltaTime.seconds,deltaTime.microseconds)