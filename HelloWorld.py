#!/usr/bin/python

import sys
import platform
if platform.platform().find('armv7l')<0: # if it is not a raspberry, use the fake RPi
        segments = ['a','b','c','d','e','f','g','h']
else:
    from rpi_TM1638 import TMBoards
    sys.path.append(r'/home/pi/proj/python/pysrc')
    import pydevd
    #pydevd.settrace('192.168.86.194')


i = 3
p = 'Hello!' * i
print(p)