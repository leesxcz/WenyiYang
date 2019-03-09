# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
This code is for plot heart curve for Wenyi Yang
The heart curve function is from http://mathworld.wolfram.com/HeartCurve.html
x=16sin^3(t);
y=13cos(t)-5cos(2t)-2cos(3t)-cos(4t);
t in -1,1
'''
import math
import numpy as np
import matplotlib.pyplot as plt

T=1        #time for running
nt=500      #time steps

t=np.linspace(0,T,nt+1) #time instance  
dt=t[1]-t[0]        #time step

plt.ion()
plt.figure()
eta = np.linspace(0, 2*np.pi,100 )
for n in range(0,nt+1):
    x = 16*n*dt*np.sin(eta)**3
    y=13*n*dt*np.cos(eta*n*dt)-5*n*dt*np.cos(2*eta*n*dt)-2*n*dt*np.cos(3*eta*n*dt)-n*dt*np.cos(4*eta*n*dt)

    plt.clf()
    plt.plot(x,y,label='heart')
    plt.axis('equal')
    plt.title("Heart Plot For Wenyi")
    plt.legend()
    plt.pause(0.01)
    print(n*dt)
