#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np                         
import matplotlib.pyplot as plt            

m=6.6*10**(-27) # mass of alpha particle
q=3.3*10**(-19) # charge of alpha particle
R=10**(2)   # radius of cyclotron
t=0
B=np.array([0,0,-1])  # magnetic field vector

f=q*np.linalg.norm(B)/(2*np.pi*m) # frequency of the AC oscillator

v=np.array([0,0,0])   # velocity of particle
pos=np.array([0,0,0])  # position of particle
pos_x = []
pos_y = []
r=0         # particle's distance from origin(starting point)
dt =(1/f)/1000

def eb_acceleration(efield,bfield): # calculates the acceleration of the particle from the fields
  eforce = efield*q
  bforce = q*np.cross(v,bfield)
  acceleration = (eforce + bforce)/m
  return acceleration

while r<R:
  if pos[0] < 10**(-4) and pos[0] > -1*10**(-4):  # checks if the particle is between the "dees"
    E = np.array([1,0,0])                       # electric field vector
    if t%(1/f) >= 0 and t%(1/f) < (1/f)/2:   # if the it's the first half of the cycle E faces one way
      E = E
    elif t%(1/f) >= (1/f)/2 and t%(1/f) < (1/f): # if the it's the second half of the cycle E faces the other way
      E = -1*E
  if pos[0] > 1 and pos[0] < -1:
    E = np.array([0,0,0])
  v = v + eb_acceleration(E,B)*dt
  pos = pos + v*dt
  pos_x.append(pos[0])
  pos_y.append(pos[1])
  r=np.sqrt(pos[0]**2+pos[1]**2+pos[2]**2)
  t += dt
    
print(.5*m*np.linalg.norm(v)**2) # prints KE in joules 
print(.5*m*(np.linalg.norm(v)**2)*6241509000000000000) # prints KE in eV
print(t)
plt.plot(pos_x, pos_y)
plt.xlabel("X position", fontsize=16)
plt.ylabel("Y position", fontsize=16)


# In[ ]:




