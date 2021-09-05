"""
30_2.py list the idndividual contents of the time
"""
import datetime
timeNow = datetime.datetime.now()
print(type(timeNow))
print("list time now:",timeNow)
print("year:",timeNow.year)
print("month:",timeNow.month)
print("day:",timeNow.day)
print("hour:",timeNow.hour)
print("minute:",timeNow.minute)
print("second:",timeNow.second)
