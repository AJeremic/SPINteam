# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 00:38:00 2023
    attempt 1 of creating spin energy level graph
@author: jerem
"""

import matplotlib as plt
import numpy as np


if __name__ == "__main__":
    
    
    """
    naming of variables
    
    """
    
    theta = 0 #angle between magnetisation and the applied field?
    K_u = 5       #uniaxial anisotropy coefficient
    r = 5 #magnitude of the applied field
    
    phi = 0  #angle between the applied field and the uniaxial anisotropy
  
    M = 1 # magintude of the magentisation of the sample
    Magn = np.array([M*np.cos(phi),M*np.sin(phi)]) # magnetisation as a vector
    H = np.array([r*np.cos(theta),r*np.sin(theta)])   #applied field, we will be either using this as a constant or sweeping it
    # possible theta/phi changing scenario  theta = np.linspace(0:360:5)
    
    """
    naming of equations / terms

    """
    
    
    E_1 = K_u*(np.sin(theta))**2
    E_2 = H*Magn*np.cos(phi)
    E_total = E_1 + E_2
    
    plt.plot(E_total, theta)
    plt.title("energy at value %d" , theta)
    plt.show()
    
    