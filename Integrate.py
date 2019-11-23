#!/usr/bin/env python
# coding: utf-8

# In[67]:


import numpy as np
import matplotlib.pyplot as plt


# In[131]:


def fu(u):
    return u

def fv(v):
    return v
    
def dphi_dR(R,z):
    q = 0.9
    L = 0.2
    v = 1
    return -((v**2*q**2*R)/(q**2*R**2+z**2) - (L**2)/(R**3))

def dphi_dz(R,z):
    q = 0.9
    L = 0.2
    v = 1
    return -((v**2*z)/(R**2*q**2+z**2))


# In[147]:


t0 = 0
tf = 500
u0 = 0
v0 = 1
R0 = 1
z0 = 1
n  = 10000001
h  = (tf-t0)/(n-1)

t      = np.linspace(t0,tf,n)
sol_u    = np.zeros([n])
sol_u[0] = u0
sol_v    = np.zeros([n])
sol_v[0] = v0
sol_R    = np.zeros([n])
sol_R[0] = R0
sol_z    = np.zeros([n])
sol_z[0] = z0


# In[148]:


for i in range(1,n):
    sol_u[i] = h*dphi_dR(sol_R[i-1],sol_z[i-1]) + sol_u[i-1]
    sol_v[i] = h*dphi_dz(sol_R[i-1],sol_z[i-1]) + sol_v[i-1]
    sol_R[i] = h*fu(sol_u[i-1]) + sol_R[i-1]
    sol_z[i] = h*fv(sol_v[i-1]) + sol_z[i-1]


# In[149]:


plt.plot(sol_R,sol_z, label = "Orbits")
plt.legend()
plt.savefig("o.png")


# In[ ]:




