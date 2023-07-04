# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:25:24 2023
Double Spin attempt
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
        theta.append(i) 
    theta_r = np.array(theta)
    theta_r *= np.pi/180 #angle from spin 1 and 
   
    K_u = 1100000       #uniaxial anisotropy coefficient
    r = 50000 #magnitude of the applied field
    #print(theta_r)
    phi = 0  #angle between the applied field and the uniaxial anisotropy
  
    M = 1 # magintude of the magentisation of the sample
    Magn = np.array([M*np.cos(phi*np.pi/180),M*np.sin(phi*np.pi/180)]) # magnetisation as a vector
    H = np.array([r*np.cos(theta_r),r*np.sin(theta_r)])   #applied field, we will be either using this as a constant or sweeping it
    # possible theta/phi changing scenario  theta = np.linspace(0:360:5)
    E_total = []
    desc = 0
    """
    naming of equations / terms

    """
    #print(theta_r)
    
    for i in range(len(theta)):
        #print(i)
        if ((theta_r[i])%(np.pi/2) == 0 and theta_r[i] - np.pi != 0 and theta_r[i] != 0):
            desc = 1
        if ((theta_r[i])%(np.pi/2) == 0 and theta_r[i] - np.pi == 0):

            desc = 0
        #print(phi)
        E_1 = K_u*(np.sin(phi*np.pi/180))**2
        E_2 = r*M*np.cos(theta_r[i])
        print(phi)
        
        E_total.append(int(E_1 + E_2))
        #print(theta_r[i])
        if desc:
            phi-=5
        else:
            phi+=5
            
            
    """
    plotting
    
    """
    
    plt.plot(theta_r,E_total)
    plt.title("energy")
    plt.xlabel("Radians")
    plt.ylabel("energy in J/m^3")
    plt.show()
    
    
    
