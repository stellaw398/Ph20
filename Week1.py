#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:17:43 2018

@author: apple
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
### Version using numpy arrays

fx = float(sys.argv[1])
fy = float(sys.argv[2])
Ax = float(sys.argv[3])
Ay = float(sys.argv[4])
phi = float(sys.argv[5])*np.pi
dt= float(sys.argv[6])
N = float(sys.argv[7])
t = np.linspace(0, dt*N, num=N+1)
X = Ax * np.cos(2 * np.pi * fx * t)
Y = Ay * np.sin((2 * np.pi * fy * t) + phi)
Z = X + Y
np.savetxt('functions.txt',np.c_[X,Y,Z,t]) ## saves text file with the X,Y,Z,t function values organized into columns
plt.plot(Y,X)
plt.title('fx= %2.1f fy= %2.1f Ax= %2.1f Ay= %2.1f phi= %2.2f dt= %2.1f N= %2.1f' %(fx,fy,Ax,Ay,phi,dt,N)) ##title of figure shows variable values
#plt.savefig('Lissajous_%2.2f_%2.2f.pdf'%(fx/fy,phi)) ##plots are named by the fx/fy ratio and phi
plt.show()
plt.plot(t,Z)
plt.title('fx= %3.1f fy= %3.1f Ax= %2.1f Ay= %2.1f phi= %2.2f dt= %2.1f N= %2.1f' %(fx,fy,Ax,Ay,phi,dt,N))
plt.savefig('Beats_%3.f_%3.f.pdf'%(fx*2*np.pi,fy*2*np.pi))##plots named by frequencies of oscillation
plt.show()


### Version using for loops and lists 
'''
fx = float(sys.argv[1])
fy = float(sys.argv[2])
Ax = float(sys.argv[3])
Ay = float(sys.argv[4])
phi = float(sys.argv[5])*np.pi
dt= float(sys.argv[6])
N = int(sys.argv[7])
t=[]
X=[]
Y=[]
Z=[]
for it in range(N):
    tempt= dt * it
    tempX=Ax * np.cos(2 * np.pi * fx * tempt)
    tempY=Ay * np.sin((2 * np.pi * fy * tempt) + phi)
    t.append(tempt)
    X.append(tempX)
    Y.append(tempY)
    Z.append(tempX + tempY)
plt.plot(X,Y)
plt.show()
plt.plot(Z,t)
plt.show()
'''

