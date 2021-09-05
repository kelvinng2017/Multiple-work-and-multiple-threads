"""
30_7.py convert the current date to a string format and display it in a different format
"""
import datetime

timeNow = datetime.datetime.now()
print(timeNow.strftime("%Y/%m/%d %H:%M:%S"))
print(timeNow.strftime("%y-%b-%d %H-%M-%S"))