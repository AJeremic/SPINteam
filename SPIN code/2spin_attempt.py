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
import scipy.signal as sig

def peaksandtroughs(array):
    peaks, _ = sig.find_peaks(E_total)
    countmax = 0
    countmin = 0
    locationmin = np.array([])
    locationmax = np.array([])
    for peak in peaks:
        countmax += 1
        locationmax = np.append(locationmax,peak)
    troughs = sig.argrelmin(E_total)
    for relmin in troughs:
        countmin += 1
        locationmin = np.append(locationmin, relmin)
    locationmax *= 5
    locationmin *= 5
    return locationmax, locationmin, countmax, countmin

if __name__ == "__main__":
    
    x = int(input("what starting angle do you want"))
    """
    naming of variables
    
    """
    locationmax = np.array([])
    locationmin = np.array([])
    countmax = 0
    countmin = 0
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
    graphing_t.append(2*np.pi)
    
    K_u_1 = 110000       #uniaxial anisotropy coefficient of 1st spin
    K_u_2 = 110000       #uniaxial anisotropy coefficient of 2nd spin
    r = 50000 #magnitude of the applied field
    #print(theta_r)
    phi = x%90  #angle between the applied field and the uniaxial anisotropy
    M_2 = 5 
    M_1 = 1 # magintude of the magentisation of the sample
    Magn_spin_1 = np.array([M_1*np.cos(phi*np.pi/180),M_1*np.sin(phi*np.pi/180)]) # magnetisation as a vector
    Magn_spin_2 = np.array([M_2*np.cos(phi*np.pi/180),M_2*np.sin(phi*np.pi/180)]) # magnetisation as a vector
    H = np.array([r*np.cos(theta_r),r*np.sin(theta_r)])   #applied field, we will be either using this as a constant or sweeping it
    # possible theta/phi changing scenario  theta = np.linspace(0:360:5)
    E_total = np.array([])
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
    for i in range(len(theta_r)):
        #print(i)
        if ((theta_r[i])%(np.pi/2) == 0 and (theta_r[i]) != np.pi and (theta_r[i]) != 0):
            desc = 1
        elif (theta_r[i]%(np.pi/2) == 0 and ((theta_r[i])  == np.pi or theta_r[i] == 0)):
            desc = 0
        #print(phi)
        E_uni_1 = K_u_1*(np.sin((phi*np.pi/180)))**2
        #E_uni_2 = K_u_2*(np.sin((phi*np.pi/180)))**2

        #print(E_1)
       # print("next line is phi")
       # print(phi)
      #  print(theta_r[i]*180/np.pi)
       # print("theta")
       # print(theta_r[i]*180/np.pi)
        #print(phi*np.pi/180)
        #print(np.gradient(theta)
        #print("                                                                ")
        E_spin_1 = r*M_1*np.cos(theta_r[i])
        E_spin_2 = r*M_2*np.cos(np.pi-theta_r[i])
        #print(phi)

        E_total = np.append(E_total,int(E_spin_1+E_spin_2+E_uni_1))
        #print(E_total)
        #print(theta_r[i])
        if desc:
            phi-=5
        else:
            phi+=5
            
            
    """
    plotting
    
    """

    locationmax, locationmin, countmax, countmin = peaksandtroughs(E_total)
    
    print(locationmax)
    print(locationmin)
    

    plt.plot(graphing_t,E_total)
    plt.title("energy")
    plt.xlabel("Radians")
    plt.ylabel("energy in J/m^3")
    plt.show()
    



    