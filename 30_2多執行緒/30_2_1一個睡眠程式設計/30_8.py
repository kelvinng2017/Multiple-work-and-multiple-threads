"""
30_8.py Let's say it's September 4,2021, and we care so much that our girlfriend wants our program to remind us of the gift on her birthday
January 1 2022 Maybe you program could do that
"""
import datetime

timeStop = datetime.datetime(2022,1,1,8,0,0)
while datetime.datetime.now() < timeStop:
    pass
print("girlfriend's birthday")