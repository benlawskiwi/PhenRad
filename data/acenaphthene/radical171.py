import numpy as np
import matplotlib.pyplot as plt

x1,y1 = np.loadtxt('nt114g_171.dat',usecols=(1,2),unpack=True)
x2,y2 = np.loadtxt('nt114h_171.dat',usecols=(1,2),unpack=True)
x3,y3 = np.loadtxt('nt115b_171.dat',usecols=(1,2),unpack=True)
x4,y4 = np.loadtxt('nt116e_171.dat',usecols=(1,2),unpack=True)
x5,y5 = np.loadtxt('nt117a_171.dat',usecols=(1,2),unpack=True)

x1 = x1[:-1]
x2 = x2[:-1]
x2 = x2[:-1]
x3 = x3[:-1]
x4 = x4[:-1]
x5 = x5[:-1]

y1 = y1[:-1]
y2 = y2[:-1]
y2 = y2[:-1]
y3 = y3[:-1]
y4 = y4[:-1]
y5 = y5[:-1]

subr = np.logical_and(x1<512.1,x1>500)
x1 = x1[subr]
y1 = y1[subr]
subr=np.logical_and(x2>512.1,x2<600)
x2 = x2[subr]
y2 = y2[subr]


y1 *=-1
y2 *=-1
y3 *=-1
y4 *=-1
y5 *=-1

y3 +=30
y4 +=50
y5 +=75

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(x5,y5)
plt.show()
