"""
test_time.py
"""

import  time
import  msvcrt
import  os

def getInput( timeout = 5):
    start_time = time.time()
    input = ''
    while True:
        if msvcrt.kbhit():
            input = msvcrt.getche()
        if len(input) != 0 or (time.time() - start_time) > timeout:
            break
    if len(input) > 0:
        return ord(input)
    else:
        return ord('\0')
        
print(getInput(5))
os.system("pause")
