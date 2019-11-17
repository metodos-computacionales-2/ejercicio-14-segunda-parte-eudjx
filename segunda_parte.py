import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(20,8))
data = np.loadtxt("segunda_parte.dat")
t=data[:,0][0:1001]
uno=data[:,1][0:1001]
dos=data[:,2][0:1001]
tres=data[:,1][1001:2002]
cuatro=data[:,2][1001:2002]
plt.subplot(1,2,1)
plt.plot(t,uno, label="y0")
plt.plot(t,dos, label="y1")
plt.xlabel('t')
plt.ylabel('Y')
plt.title("RK4")
plt.legend()
plt.subplot(1,2,2)
plt.plot(t,tres,label="y0")
plt.plot(t,cuatro, label="y1")
plt.xlabel('t')
plt.ylabel('Y')
plt.title("Euler")
plt.legend()
plt.savefig("rk4.png")