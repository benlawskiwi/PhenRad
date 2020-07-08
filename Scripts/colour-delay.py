import numpy as np

import matplotlib.pyplot as plt
from scipy.integrate import simps

width = 3.487
height = width/1.4
one_col = (3.5*width, 3*height)

fig = plt.figure(figsize=one_col)

let = ['a','b','c','d','e','f','g','h','i','j']
d = ['300','250','200','350','400']
p = []

for i in range (0,np.size(let),2):
    #Read in 2 laser + 3 laser files
    fn = 'nt107'+let[i]+'.dat'
    fn2 = 'nt107'+let[i+1]+'.dat'
    a,b,x,y = np.loadtxt(fn,unpack=True)
    a,b,x2,y2 = np.loadtxt(fn2,unpack=True)
    y *=-1
    y2 *=-1
    #Adjust the baseline
    subrb = np.logical_and(x>158,x<162)
    yb = y[subrb]
    y -= np.mean(yb)
    yb = y2[subrb]
    y2 -= np.mean(yb)
    #Look at mass 165
    subr = np.logical_and(x>164.5,x<165.4)
    xx = x[subr]
    yy = y[subr]
    xx2 = x2[subr]
    yy2 = y2[subr]
    #Integrate 2 laser v 3 laser
    int1 = simps(yy,xx)
    int2 = simps(yy2,xx2)
    delay = d[int(i/2)]+' ns'
    print(delay)
    ratio = 100-int1/int2*100
    print('depletion ratio '+str(ratio)+'%')
    p.append(ratio)
    #plots
    ax = plt.subplot(2,3,int(i/2+1))
    ax.plot(xx2,yy2,label='2 laser')
    ax.plot(xx,yy,label='3 laser')
    ax.legend()
    ax.set_xlabel(d[int(i/2)]+' ns')
    ax.set_xticks([])
    ax.set_yticks([])

ax = plt.subplot(2,3,6)
ax.plot(d,p,'C2*',markersize=14)
ax.set_xlabel('delay (ns)',fontsize=14)
ax.set_ylabel('% depletion',fontsize=14)
plt.savefig('colour-delay.pdf',dpi=300,bb0x_inches='tight')
plt.show()
    
