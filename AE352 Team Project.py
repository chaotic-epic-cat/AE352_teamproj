#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from sympy import *


# In[2]:


m = 509 #g
g = 9.8 #m/s^2
Ixx = ???
Iyy = Ixx
Izz = ???
theta = Symbol('theta')
phi = Symbol('phi')

J = Matrix([[Ixx, 0, -Ixx*sin(theta)],
            [0, Iyy**2*(cos(phi))**2 + Izz*(sin(phi))**2, (Iyy-Izz)*cos(phi)*sin(phi)*cos(theta)],
            [-Ixx*sin(theta), (Iyy-Izz)*cos(phi)*sin(phi)*cos(theta), Ixx(sin(theta))**2 + Iyy*(sin(phi))**2*(cos(theta))**2 + Izz*(cos(phi))**2*(cos(theta))**2]])
n_dot = Matrix([[1, sin(phi)*tan(theta), cos(phi)*tan(theta)],
                [0, cos(phi), -sin(phi)],
                [0, sin(phi)/cos(theta), cos(phi)/cos(theta)]])
n_dotdot = diff(n_dot, t)


f = m*x_dotdot + Matrix([0, 0, m*g])
T = J*n_dotdot + diff(J, t)*n_dot - 1/2*diff(n_dot.T*J*n_dot, n)


# In[18]:


#Perfomance Requirement 1
y = 1

plt.plot([0, 20, 40, 60, 120], [1, 1, 1, 1, 1])
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.title('Maintaing Altitude')
plt.axis([0, 120, 0, 1.5])
plt.grid(True)
plt.show()


# In[24]:


#Performance Requirement 2
v_x = []
v_y = []
v_z = []

h = 1 #m
v = .5 #m/s (constant)
r = 2 #m
T = 18.3 #s
w = 2*np.pi/T
t = Symbol('t')

q = Matrix([r*cos(w*t), r*sin(w*t), (h)])

for n in range(100):
    v_x.append(q[0].subs(t, n))
    v_y.append(q[1].subs(t, n))
    v_z.append(q[2].subs(t, n))
    
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot3D(v_x, v_y, v_z, 'blue')
ax.set(xlabel='X-Direction (m)')
ax.set(ylabel='Y-Direction (m)')
ax.set(zlabel='Alttidude (m)')
ax.set_title('Circle of the Drone')
plt.show


# In[28]:


#Peformance Requirement 3 (2 graphs - 1 Position & 1 Velocity)
x = [0, 0, 0, -5, -5]
y = [0, 0, 5, 5, 5]
z = [0, 1, 1, 1, 0]

fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot3D(x, y, z, 'blue')
ax.set(xlabel='X-Direction (m)')
ax.set(ylabel='Y-Direction (m)')
ax.set(zlabel='Alttidude (m)')
ax.set_title('Position of the Drone')
plt.show


# In[41]:


#Peformance Requirement 3 Part 2 (Velocity)

t =   [0, .01, .1, .5, .9, .99, 1,
      1.01, 5, 5.1, 5.3,
      5.5, 9.5, 9.7, 10,
      10.11, 10.12, 10.22, 10.72, 11.12, 11.13, 11.14]
v_x = [0, 0, 0, 0, 0, 0, 0, 
      0, 0, 0, 0,
      1, 1, 0, 0,
      0, 0, 0, 0, 0, 0, 0]
v_y = [0, 0, 0, 0, 0, 0, 0,
      1, 1, 0, 0,
      0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0]
v_z = [0, .01, .1, .5, .1, .01, 0,
      0, 0, 0, 0,
      0, 0, 0, 0,
      0, .01, .1, .5, .1, .01, 0]
plt.plot(t, v_x, 'r', t, v_y, 'b', t, v_z, 'g', label='Inline label')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity for Position of Drone')
plt.show()


# In[ ]:




