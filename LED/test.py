#!/usr/bin/env python

# TM1638 playground

import TM1638
import time

# These are the pins the display is connected to. Adjust accordingly.
# In addition to these you need to connect to 5V and ground.

DIO = 20
CLK = 21
STB = 26

display = TM1638.TM1638(DIO, CLK, STB)

display.enable(1)

#def display_text(text):
#    j=0
#    for i in range(len(text)):
#        if j==8:
#            break
#        if text[i]=='.':
#            continue
#        display.send_char(j, display.FONT[text[i]]
#                          , i<len(text)-1 and text[i+1]=='.')
#        j=j+1
    

count = 0
while True:
    count += 1
    for i in range(8):
        #display.send_char(i, count)
        #display.send_char(0, display.FONT["8"], False)
#        display_text(" 1.2  5.6 ")
#        display.set_text2("0.1.2.3.4.5.6.7.8")
        display.set_text2(" 1.2  5.6 ")
        display.set_led(i,1)
        #display.set_text("01234567");
#        for i in range(len(count)):
#            display.set_digit(8-len(text)+i, int(text[i]), i==dotpos)
        time.sleep(1)
        display.set_led(i,0)

