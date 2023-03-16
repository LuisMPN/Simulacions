# -------------------------------------------------------
# NUMERICAL SOLUTION NEWTON EQUATIONS OF MOTION
# VELOCITY VERLET METHOD
# April 2020 Python3 version 
# 
# Very simple example with Harmonic oscillator
# Units (nanoSI): nm, ns, ng, ...
# By Jordi Faraudo 2018
# -------------------------------------------------------

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt

#Introduce the parameters of the lever
m=1
w=float(input('\n width in nm:\n>'))
T=float(input('\n thcikness in nm:\n>' ))
L=float(input('\n length in nm:\n>'))
Yo=float(input('Young modulus in GPa:\n>'))

#Force constant from flexor moment deduction divided by 100 for units conservation
k=Yo*w*T**3/(4*L**3)


#Initial condition (position and velocity)
x0=0.1
v0=0.0
# initial Energy
E0=(m/2.0)*v0*v0+(k/2)*x0*x0

#Show data of the program

print('\n--------------------------------------------------------')
print('SIMPLE MD SIMULATION OF A SINGLE PARTICLE IN HARMONIC TRAP')
print('----------------------------------------------------------')
print('Force constant:',k,' N/m')
print('Particle of mass:',m,' ng')
print('Period according to analytical solution of harmonic oscillator:',T,' ns')

# input time step
dt = float(input("\n Time step dt (in ns):\n>"))
# Final time
ntot = int(input("\n Number of time steps:\n>"))
print('Simulation time will be',dt*ntot,' ns')

# create empty array starting at zero with time, position, velocity
x = np.zeros(ntot+1)
v = np.zeros(ntot+1)
t = np.zeros(ntot+1)

#Initial conditions
x[0] = x0
v[0] = v0
   
# Time evolution
print('\n Calculating time evolution...')
#Make a list with all the computed forces
force=[]
for i in range(0, ntot):
    print(i)
    #Calculate Force over the particle with damping proportional to the velocity
    f = -k*x[i]-0.01*v[i]
    force.append(f)
    #Calculate acceleration from 2nd Law
    a = f/m 
    # New velocity after time dt/2 (half kick)
    v_m = v[i]+a*dt/2.0
    # New position
    x[i+1] = x[i]+v_m*dt
    # Force at new position
    f=-k*x[i+1]
    # Acceleration
    a= f/m
    #Velocity from t+dt/2 to t+dt (remaining half kick)
    v[i+1]= v_m+a*dt/2.0
    #Update time
    t[i+1] = t[i]+dt

# plot output
print('Calculation finished. Showing plot with results')

#
# Create a plot with x(t) and v(t)
# 
#plt.plot(t,x, 'ro', t, v, 'bv')
plt.figure(1)

plt.subplot(211)
plt.plot(t,x)
plt.ylabel('x (nm)')

plt.subplot(212)
plt.plot(t,v)
plt.ylabel(' v (nm/ns)')
plt.xlabel('time (ns)')

#create axis
#plt.axhline(0, color='black')
#plt.axvline(0, color='black')
#Show plot in screen
plt.show()
#Show plot of phase space
plt.plot(x,v,'k')
plt.xlabel('x (nm)')
plt.ylabel('v (nm/ns)')
#Show plot in screen
plt.show()
#Also plot energy
#energy at all steps
E=(m/2.0)*v*v+(k/2)*x*x
#Relative value (E/E0)
RE=E/E0
plt.plot(t,RE,'k')
plt.xlabel('time (ns)')
plt.ylabel('E/E0')
#Show plot in screen
plt.show()
#Define a function to represent the movement
def movement(Fap,young,width,thick,leng):
    pos=np.linspace(0,L,101)
    mov=[]
    #Compute the movement of the cantilever
    for i in range(len(pos)):
       eq=-Fap*12/(young*width*thick**3)*(leng*pos[i]**2/2-pos[i]**3/6)
       mov.append(eq)
    return pos,mov
for i in range(ntot):
    Res=movement(force[i],Yo,w,T,L)
    posi=Res[0]
    movi=Res[1]
    if i%20==0:
        plt.ion()
        plt.plot(posi,movi)
        plt.title('Cantilever movement')
        plt.xlabel('Position of the cantilever (nm)')
        plt.ylabel('Deformation of the cantilever (nm)')
        plt.show()
        plt.pause(0.1)
