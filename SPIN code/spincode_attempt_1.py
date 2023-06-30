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
    
    
    K_u = 5       #uniaxial anisotropy coefficient
    H = 5   #applied field, we will be either using this as a constant or sweeping it
    theta_u = 0  #angle between the applied field and the uniaxial anisotropy
    theta_m = 0 #angle between magnetisation and the applied field?
    M =  # magentisation of the sample
    """
    naming of equations / terms

    """
    
    
    E_1 = K_u*(np.sin(theta_u))**2
    E_2 = H*M*np.cos(theta_m)
    E_total = E_1 + E_2
    
    plt.plot(E_total, theta_u)
    plt.title("energy at value %d" , theta_u)
    plt.show()
    
    