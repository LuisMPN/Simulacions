import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand
        
#Plot the form of the cantilever
L=100
w=10
T=10
f=np.linspace(0,L,11)
E=160
pos=np.linspace(0,L,101)
mov=[]
for i in range(len(pos)):
   eq=-f[10]*12/(E*w*T**3)*(L*pos[i]**2/2-pos[i]**3/6)
   mov.append(eq)

plt.plot(pos,mov)
plt.show()


