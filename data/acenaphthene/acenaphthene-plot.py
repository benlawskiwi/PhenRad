import numpy as np
import matplotlib.pyplot as plt

x1,y1 = np.loadtxt('nt112a_165.dat',usecols=(1,2),unpack=True)
x2,y2 = np.loadtxt('nt112b_165.dat',usecols=(1,2),unpack=True)
x3,y3 = np.loadtxt('nt112c_165.dat',usecols=(1,2),unpack=True)
x4,y4 = np.loadtxt('nt113a_165.dat',usecols=(1,2),unpack=True)
x5,y5 = np.loadtxt('nt113b_165.dat',usecols=(1,2),unpack=True)
x6,y6 = np.loadtxt('nt114g_165.dat',usecols=(1,2),unpack=True)
x7,y7 = np.loadtxt('nt114g_171.dat',usecols=(1,2),unpack=True)
x8,y8 = np.loadtxt('nt114g_171.dat',usecols=(1,2),unpack=True)
x9,y9 = np.loadtxt('nt114h_171.dat',usecols=(1,2),unpack=True)
x10,y10 = np.loadtxt('nt115b_171.dat',usecols=(1,2),unpack=True)

x1 = x1[:-1]
x2 = x2[:-1]
x2 = x2[:-1]
x3 = x3[:-1]
x4 = x4[:-1]
x5 = x5[:-1]
x6 = x6[:-1]
x7 = x7[:-1]
x10 = x10[:-1]
y10 = y10[:-1]

y1 = y1[:-1]
y2 = y2[:-1]
y2 = y2[:-1]
y3 = y3[:-1]
y4 = y4[:-1]
y5 = y5[:-1]
y6 = y6[:-1]
y7 = y7[:-1]

#Stitching them together
ofs = np.mean(y4)-np.mean(y3)
print(ofs)
y4 -= ofs
y5 -=ofs/2

subr = np.logical_and(x4<600,x4>531.18)
x4 = x4[subr]
y4 = y4[subr]
subr = np.logical_and(x3<531.18,x3>500)
x3 = x3[subr]
y3 = y3[subr]
subr = np.logical_and(x5>516.1,x5<519.45)
x5 = x5[subr]
y5 = y5[subr]
subr = np.logical_and(x2>500,x2<516.1)
x6 = x2[subr]
y6 = y2[subr]
subr = np.logical_and(x2>519.45,x2<600)
x2 = x2[subr]
y2 = y2[subr]
subr = np.logical_and(x7<512.1,x7>500)
x7 = x7[subr]
y7 = y7[subr]
subr=np.logical_and(x9>512.1,x9<600)
x9 = x9[subr]
y9 = y9[subr]


plt.plot(x1,-y1,'C0',label='mass 165')
plt.plot(x2,-y2,'C0')
plt.plot(x3,-y3,'C0')
plt.plot(x4,-y4,'C0')
plt.plot(x5,-y5,'C0')
plt.plot(x6,-y6,'C0')

y7 *=-3
y7 += 400
plt.plot(x7,y7,'C2')

y9 *=-3
y9 +=400
plt.plot(x9,y9,'C2')

y10 *=-3
y10 +=500
plt.plot(x10,y10,'C2',label='mass 171')

plt.legend()
plt.xlabel('wavelength (nm)')
plt.ylabel('intensity (arb. u.)')
plt.show()

plt.plot(x1,-y1,'C0',label='112a')
plt.plot(x2,-y2,'C1',label='112b')
plt.plot(x3,-y3,'C2',label='112c')
plt.plot(x4,-y4,'C3',label='113a')
plt.plot(x5,-y5,'C4',label='113b')
plt.plot(x6,-y6,'C1')

plt.legend()
plt.xlabel('wavelength (nm)')
plt.ylabel('intensity (arb. u.)')
#plt.show()
