#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np                         
import matplotlib.pyplot as plt            

m=6.6*10**(-27)
q=3.3*10**(-19)
R=10**(-3)
t=0
B=np.array([0,0,-1])

f=q*np.linalg.norm(B)/(2*np.pi*m)

v=np.array([0,0,0])
pos=np.array([0,0,0])
pos_x = []
pos_y = []
r=0
dt =(1/f)/1000

def eb_acceleration(efield,bfield):
  eforce = efield*q
  bforce = q*np.cross(v,bfield)
  acceleration = (eforce + bforce)/m
  return acceleration

while r<R:
  if pos[0] < 10**(-4) and pos[0] > -1*10**(-4):
    E = np.array([1,0,0])
    if t%(1/f) >= 0 and t%(1/f) < (1/f)/2:
      E = E
    elif t%(1/f) >= (1/f)/2 and t%(1/f) < (1/f):
      E = -1*E
  if pos[0] > 1 and pos[0] < -1:
    E = np.array([0,0,0])
  v = v + eb_acceleration(E,B)*dt
  pos = pos + v*dt
  pos_x.append(pos[0])
  pos_y.append(pos[1])
  r=np.sqrt(pos[0]**2+pos[1]**2+pos[2]**2)
  t += dt
    
print(.5*m*np.linalg.norm(v)**2)
print(.5*m*(np.linalg.norm(v)**2)*6241509000000000000)
plt.plot(pos_x, pos_y)
plt.xlabel("X position", fontsize=16)
plt.ylabel("Y position", fontsize=16)


# In[ ]:




