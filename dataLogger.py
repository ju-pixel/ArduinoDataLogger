# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:30:02 2021

@author: julia
"""

import serial
from datetime import datetime
import time

ser = serial.Serial('COM3', 9600, timeout=0)

text_file = open("variableDCmotor.txt", 'w')  

while 1:
    x=ser.readline()
    print(str(datetime.now()), x) 
    data = [str(datetime.now()),x]
    text_file.write("{}\n".format(data))
    text_file.flush()
    time.sleep(1)