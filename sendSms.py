#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time
from curses import ascii

def uni_byte(uni):
	byteStr = ''
	for i in range(len(uni)):
	    	if ord(uni[i]) < 127:
			hexByte = hex(ord(uni[i]))[2:]
			for h in range(0,4-len(hexByte)):
				hexByte = '0'+hexByte
			byteStr+=hexByte
	     	else:
		    	byteStr += uni[i].encode('unicode-escape')[2:]
	print byteStr
	return byteStr.upper()

def readline(a_serial, eol=b'\n\n'):
    leneol = len(eol)
    line = bytearray()
    while True:
        c = a_serial.read(1)
        if c:
            line += c
            if line[-leneol:] == eol:
                break
        else:
            break
    return bytes(line)

num = 'Insert Phone Number'
msg = 'Insert Message'
ser = serial.Serial('/dev/ttyUSB0')
ser.write('AT\r')
ser.write('AT+CMGF=1\r')
time.sleep(0.5)
ser.write('AT+CSMP=17,167,0,8\r')
time.sleep(0.5)
ser.write('AT+CSCS="UCS2"\r')
time.sleep(1)
ser.write("AT+CMGS=\""+uni_byte(num.decode('utf-8'))+"\"\r")
time.sleep(2)
ser.write(uni_byte(msg.decode('utf-8')))
ser.write('\x1A')
time.sleep(0.5)
ser.write('AT\r')
