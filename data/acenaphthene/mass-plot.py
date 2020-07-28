import numpy as np
import matplotlib.pyplot as plt

a,b,x1,y1 = np.loadtxt('nt116d_mass.dat',unpack=True)
a,b,x2,y2 = np.loadtxt('nt116b_mass.dat',unpack=True)
a,b,x3,y3 = np.loadtxt('nt116a_mass.dat',unpack=True)

plt.plot(x3,y3,'C0',label=r'Discharge On $\lambda$ Off')
plt.plot(x2,y2,'C3',label=r'Discharge On $\lambda$ 514.875nm')
plt.plot(x1,y1,'C2',label=r'Discharge Off $\lambda$ 514.875nm')
plt.xlim(162,175)
plt.ylim(-0.025,0.005)
plt.xlabel('mass (amu)')
plt.ylabel('ion intensity')
plt.legend()
plt.show()
