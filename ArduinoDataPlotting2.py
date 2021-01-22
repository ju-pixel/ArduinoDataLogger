# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:37:59 2021

@author: julia
"""
import re

with open("lightSensorData.txt") as f:
    content = f.readlines()[2:]
    
stringLists = []
numLists = []#index 6 is voltage and will be plotted vs time in steps of 0.5sec

for ii in content:
    reading = re.findall(r'[\d\.\d]+', ii)
    if len(reading) == 8:
       stringLists.append(reading)
        
for yy in stringLists:
   yy = [float(item[0:4]) for item in yy]
   numLists.append(yy)
 
voltages = []
for aa in numLists:
    voltages.append(aa[6])

import numpy as np
time = list(np.arange(len(numLists)))  
 
import matplotlib.pyplot as plt
plt.figure(1)                 
plt.plot(time,voltages)
plt.xlabel('time points')
plt.ylabel('voltage')                     

             