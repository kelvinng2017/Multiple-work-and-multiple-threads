#/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
30_24.py 使用Threading.Rlock重新設計30_23.py 程式不會產生死結(dead lock)測試
"""

import threading,logging
logging.basicConfig(level=logging.DEBUG)
datalock = threading.Rlock() #Rlock物件
datalock.acquire() #進入鎖定
logging.debug("Enter locked mode")
datalock.acquire() #不會進入死結
logging.debug("Trying to locked again")
datalock.release()
datalock.release()