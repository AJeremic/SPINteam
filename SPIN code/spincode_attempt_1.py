# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 00:38:00 2023
    attempt 1 of creating spin energy level graph
@author: jerem
"""

from matplotlib import pyplot as plt
import numpy as np


if __name__ == "__main__":
    
    
    """
    naming of variables
    
    """
    i = 0
    theta = [0.]
    for j in range(72): 
        i +=5
        theta.append(i) #angle between magnetisation and the applied field?
    theta_r = np.array(theta)
    theta_r *= np.pi/180
   
    K_u = 1100000       #uniaxial anisotropy coefficient
    r = 5 #magnitude of the applied field
    print(theta_r)
    phi = 0  #angle between the applied field and the uniaxial anisotropy
  
    M = 1 # magintude of the magentisation of the sample
    Magn = np.array([M*np.cos(phi*np.pi/180),M*np.sin(phi*np.pi/180)]) # magnetisation as a vector
    H = np.array([r*np.cos(theta_r),r*np.sin(theta_r)])   #applied field, we will be either using this as a constant or sweeping it
    # possible theta/phi changing scenario  theta = np.linspace(0:360:5)
    E_total = []
    """
    naming of equations / terms

    """
    for i in range(len(theta)):
        #print(i)
        if ((theta_r[i])%(np.pi/2) == 0 and theta_r[i] - 180 < 0):
            phi = 90
            desc = 1
        if ((theta_r[i])%(np.pi/2) == 0 and theta_r[i] - 180 == 0):
            phi = 0
            desc = 0
    
        E_1 = K_u*(np.sin(theta_r[i]))**2
        E_2 = r*M*np.cos(phi*np.pi/180)
        
        E_total.append(int(E_1 + E_2))
        print(theta_r[i])
        if desc:
            phi-=5
        else:
            phi+=5
    plt.plot(theta_r,E_total)
    plt.title("energy")
    plt.show()
    
    
    