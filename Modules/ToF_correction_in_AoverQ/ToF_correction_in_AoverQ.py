#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu 4 June 16:40:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

ToF_correction_in_AoverQ MODULE -- The module to correct the ToF (time of flight) in A/Q

The code generates:
-- Outputfiles/Figures/

"""
MODULE_name = 'ToF_correction_in_AoverQ'

'''
----------------------------------------------------------------- Protected part (Don't touch nothing) ----------------------------------------------------------------------------------------------------------------
'''
import os, sys
sys.path.append('.')
sys.path.append('..')
basepath = os.path.abspath(__file__).rsplit('/Fission_Analysis_VAMOS/',1)[0]+'/Fission_Analysis_VAMOS/'
sys.path.append(basepath)
Module_path = basepath + '/Modules/' + MODULE_name + '/'
sys.path.append(Module_path)

'''
---------------------------------------------------- Import packages and Framework functions ----------------------------------------------------------------------------------------------------
'''
import numpy as np
import Framework.read_and_save.read_and_save as RAS
from Plotter.Plotter import Plotter
import matplotlib.pyplot as plt

'''
---------------------------------------------- Open and read .hdf5 original file like a hdf5 object ----------------------------------------------------------------------------------
'''
hdf5_folder_path = basepath + 'Data_hdf5/' + MODULE_name + '_run/' #The folder with files after the calibrations comming from RootA transformed in hdf5
file_14_degrees = 'Analysis_14_file_ToF_correction_in_AoverQ_variables' #Without .hdf5 extension
file_21_degrees = 'Analysis_21_file_ToF_correction_in_AoverQ_variables' #Without .hdf5 extension
file_14_21_degrees = 'Analysis_14+21_file_ToF_correction_in_AoverQ_variables' #Without .hdf5 extension

data_14_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_14_degrees) #Array-matrix with our data
data_21_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_21_degrees) #Array-matrix with our data
data_14_21_degrees= RAS.Read_hdf5_file(hdf5_folder_path, file_14_21_degrees) #Array-matrix with our data


'''
------------------------------------------------------ Pattern A vs A/Q simulated -----------------------------------------------------------
'''

fig = plt.figure(figsize=(10,7))

ax1 = fig.add_subplot(111)

Q_simulated = np.linspace(30,60,60-30+1)
A_simulated = np.linspace(80,190,190-80+1)

Q,A=np.meshgrid(Q_simulated, A_simulated)

A_Q = A/Q

plt.plot(A_Q,A, '.k')
plt.xlim(2.5,3.5)
plt.ylim(80,190)

#charge q = 40 in blue
q_40_x = np.array([])
q_40_y = np.array([])
for j in range(0, len(Q)):
    for i in range(0, len(Q[j])):
        if Q[j][i] == 40.0:
            q_40_x = np.append(q_40_x, A_Q[j][i])
            q_40_y = np.append(q_40_y, A[j][i])
plt.plot(q_40_x, q_40_y, '.-b', label='q = 40')

#charge q = 50 in green
q_50_x = np.array([])
q_50_y = np.array([])
for j in range(0, len(Q)):
    for i in range(0, len(Q[j])):
        if Q[j][i] == 50.0:
            q_50_x = np.append(q_50_x, A_Q[j][i])
            q_50_y = np.append(q_50_y, A[j][i])
plt.plot(q_50_x, q_50_y, '.-g', label='q = 50')

#A/Q = 3 in red
AQ_x = np.array([])
AQ_y = np.array([])
for j in range(0, len(A_Q)):
    for i in range(0, len(A_Q[j])):
        if A_Q[j][i] == 3.0:
            AQ_x = np.append(AQ_x, A_Q[j][i])
            AQ_y = np.append(AQ_y, A[j][i])
plt.plot(AQ_x, AQ_y, '.-r', label='A/Q = 3.0')

plt.legend()

ax1.set_ylabel(r'A', fontsize=20)
ax1.set_xlabel(r'A/Q', fontsize=20)

print('Saving figure as:' + basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/' + 'A_vs_A_Q_pattern' + '.png')
print('\n')
plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/' + 'A_vs_A_Q_pattern' + '.png', format='png')
plt.show()
