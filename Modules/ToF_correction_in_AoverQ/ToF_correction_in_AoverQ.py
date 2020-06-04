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

#CONDITIONS FOR 14, 21 AND 14+21 (after seeing Charge_states module variables):
condition_mass_14 = ((data_14_degrees['Xf'][:] > -1500) & (data_14_degrees['Yf'][:] > -1500)
                & (data_14_degrees['Yf'][:] > -110) & (data_14_degrees['Yf'][:] < 50)
                & (data_14_degrees['Pf'][:] > -100) & (data_14_degrees['Pf'][:] < 100)
                & (data_14_degrees['M'][:] < 180) & (data_14_degrees['M'][:] > 70)
                & (data_14_degrees['M_Q'][:] < 4) & (data_14_degrees['M_Q'][:] > 2.25))

condition_mass_21 = ((data_21_degrees['Xf'][:] > -1500) & (data_21_degrees['Yf'][:] > -1500)
                & (data_21_degrees['Yf'][:] > -110) & (data_21_degrees['Yf'][:] < 50)
                & (data_21_degrees['Pf'][:] > -100) & (data_21_degrees['Pf'][:] < 100)
                & (data_21_degrees['M'][:] < 180) & (data_21_degrees['M'][:] > 70)
                & (data_21_degrees['M_Q'][:] < 4) & (data_21_degrees['M_Q'][:] > 2.25))

condition_mass_14_21 = ((data_14_21_degrees['Xf'][:] > -1500) & (data_14_21_degrees['Yf'][:] > -1500)
                & (data_14_21_degrees['Yf'][:] > -110) & (data_14_21_degrees['Yf'][:] < 50)
                & (data_14_21_degrees['Pf'][:] > -100) & (data_14_21_degrees['Pf'][:] < 100)
                & (data_14_21_degrees['M'][:] < 180) & (data_14_21_degrees['M'][:] > 70)
                & (data_14_21_degrees['M_Q'][:] < 4) & (data_14_21_degrees['M_Q'][:] > 2.25))

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


'''
---------------------------------------------------------- M_Q pre-corrections -------------------------------------------------------------
'''

################################################################## 14 degrees
M_Q_14 = Plotter([data_14_degrees['M_Q'][condition_mass_14]]) #Create the base with the variables in a object
M_Q_14.SetFigSize(12,7)
M_Q_14.SetBinX(10000)
M_Q_14.SetFigTitle(r'M_Q        14$\degree$', 20)
M_Q_14.SetLabelX('M_Q [uma]', 20)
M_Q_14.SetLabelY('counts', 20)
M_Q_14.SetSizeTicksX(10)
M_Q_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_Q_14.SetLimX((2.6,3.6))
M_Q_14.Histo_1D() #Draw it

######### Save and show the created figure
M_Q_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_Q_14.SaveFig('M_Q_14_histogram')
M_Q_14.Show(1) #show during 1 seconds, the close authomatically
M_Q_14.Close() #close all windows, axes and figures running backend
del M_Q_14 #erase M_Q_14 (is an object)


################################################################## 21 degrees
M_Q_21 = Plotter([data_21_degrees['M_Q'][condition_mass_21]]) #Create the base with the variables in a object
M_Q_21.SetFigSize(12,7)
M_Q_21.SetBinX(10000)
M_Q_21.SetFigTitle(r'M_Q        21$\degree$', 20)
M_Q_21.SetLabelX('M_Q [uma]', 20)
M_Q_21.SetLabelY('counts', 20)
M_Q_21.SetSizeTicksX(10)
M_Q_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_Q_21.SetLimX((2.6,3.6))
M_Q_21.Histo_1D() #Draw it

######### Save and show the created figure
M_Q_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_Q_21.SaveFig('M_Q_21_histogram')
M_Q_21.Show(1) #show during 1 seconds, the close authomatically
M_Q_21.Close() #close all windows, axes and figures running backend
del M_Q_21 #erase M_Q_21 (is an object)


################################################################## 14+21 degrees
M_Q_14_21 = Plotter([data_14_21_degrees['M_Q'][condition_mass_14_21]]) #Create the base with the variables in a object
M_Q_14_21.SetFigSize(12,7)
M_Q_14_21.SetBinX(10000)
M_Q_14_21.SetFigTitle(r'M_Q        14$\degree$+21$\degree$', 20)
M_Q_14_21.SetLabelX('M_Q [uma]', 20)
M_Q_14_21.SetLabelY('counts', 20)
M_Q_14_21.SetSizeTicksX(10)
M_Q_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_Q_14_21.SetLimX((2.6,3.6))
M_Q_14_21.Histo_1D() #Draw it

######### Save and show the created figure
M_Q_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_Q_14_21.SaveFig('M_Q_14_21_histogram')
M_Q_14_21.Show(1) #show during 1 seconds, the close authomatically
M_Q_14_21.Close() #close all windows, axes and figures running backend
del M_Q_14_21 #erase M_Q_14_21 (is an object)
