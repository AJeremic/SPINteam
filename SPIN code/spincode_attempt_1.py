# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 00:38:00 2023
    attempt 1 of creating spin energy level graph
    one spin energy
@author: jerem
"""
from collections import deque
from matplotlib import pyplot as plt
import numpy as np


if __name__ == "__main__":
    
    x = int(input("what starting angle do you want"))
    """
    naming of variables
    
    """
    i = x
    splice_const = int(i/5)+1
    theta = [0.]
    for j in range(72): 
        i +=5
        theta.append(i) #angle between magnetisation and the applied field?
    theta_t = np.array(theta)
    theta_t *= np.pi/180
    theta_r = np.mod(theta_t, 2*np.pi)

    graphing_t = deque(theta_r)

    graphing_t.popleft()

    graphing_t.rotate(splice_const)
    
    K_u = 110000       #uniaxial anisotropy coefficient
    r = 0 #magnitude of the applied field
    #print(theta_r)
    phi = x%90  #angle between the applied field and the uniaxial anisotropy
  
    M = 1 # magintude of the magentisation of the sample
    Magn = np.array([M*np.cos(phi*np.pi/180),M*np.sin(phi*np.pi/180)]) # magnetisation as a vector
    H = np.array([r*np.cos(theta_r),r*np.sin(theta_r)])   #applied field, we will be either using this as a constant or sweeping it
    # possible theta/phi changing scenario  theta = np.linspace(0:360:5)
    E_total = []
    desc = 0
    #print(theta_t)
    #print("                                                         ")
    #print(graphing_t)
    """
    naming of equations / terms

    """
    #print(theta_r)
    """
    cubic anisotropy code
    K_1 = xx
    if ((theta_r[i])%(np.pi/4) == 0 and theta_r[i] - np.pi/2 != 0 and theta_r[i] != 0):
        desc = 1
    if ((theta_r[i])%(np.pi/4) == 0 and theta_r[i] - np.pi/2 == 0):
        desc = 0
        
        E_2 = 1/8*K_1*np.sin(2*phi*np.pi/180)**2
    
    """
    for i in range(len(theta_r)-1):
        #print(i)
        if ((theta_r[i])%(np.pi/2) == 0 and (theta_r[i]) != np.pi and (theta_r[i]) != 0):
            desc = 1
        elif (theta_r[i]%(np.pi/2) == 0 and ((theta_r[i])  == np.pi or theta_r[i] == 0)):
            desc = 0
        #print(phi)
        E_1 = K_u*(np.sin((phi*np.pi/180)))**2


        #print(E_1)
       # print("next line is phi")
       # print(phi)
      #  print(theta_r[i]*180/np.pi)
       # print("theta")
       # print(theta_r[i]*180/np.pi)
        #print(phi*np.pi/180)
        #print(np.gradient(theta)
        #print("                                                                ")
        E_2 = r*M*np.cos(theta_r[i])
        #print(phi)
        
        E_total.append(int(E_1 + E_2))
        
        #print(theta_r[i])
        if desc:
            phi-=5
        else:
            phi+=5
            
            
    """
    plotting
    
    """
    
    a = np.amin(E_total)
    #print(a)
    plt.plot(graphing_t,E_total)
    plt.title("energy")
    plt.xlabel("Radians")
    plt.ylabel("energy in J/m^3")
    plt.show()
    
    
    