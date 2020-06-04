#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:40:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

Charge_states MODULE -- The Charge States module (A/q), (Ameasured) and (Areconstructed)

The code generates:
-- Outputfiles/Figures/

"""
MODULE_name = 'Charge_states'

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
from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition, mark_inset)

'''
---------------------------------------------- Open and read .hdf5 original file like a hdf5 object ----------------------------------------------------------------------------------
'''
hdf5_folder_path = basepath + 'Data_hdf5/' + MODULE_name + '_run/' #The folder with files after the calibrations comming from RootA transformed in hdf5
file_14_degrees = 'Analysis_14_file_ChargeStates_variables' #Without .hdf5 extension
file_21_degrees = 'Analysis_21_file_ChargeStates_variables' #Without .hdf5 extension
file_14_21_degrees = 'Analysis_14+21_file_ChargeStates_variables' #Without .hdf5 extension

data_14_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_14_degrees) #Array-matrix with our data
data_21_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_21_degrees) #Array-matrix with our data
data_14_21_degrees= RAS.Read_hdf5_file(hdf5_folder_path, file_14_21_degrees) #Array-matrix with our data

#Variables aka branches are: ['Z', 'Zi', 'M', 'M_Q', 'Mri', 'Mr', 'Q', 'Qi'] ---> data_14_degrees.keys()

M_14 = data_14_degrees['M']; M_Q_14 = data_14_degrees['M_Q']; Z_14 = data_14_degrees['Z']; Zi_Q_14 = data_14_degrees['Zi']
M_21 = data_21_degrees['M']; M_Q_21 = data_21_degrees['M_Q']; Z_14 = data_14_degrees['Z']; Zi_Q_14 = data_14_degrees['Zi']
M_14_21 = data_14_21_degrees['M']; M_Q_14_21 = data_14_21_degrees['M_Q']; Z_14 = data_14_degrees['Z']; Zi_Q_14 = data_14_degrees['Zi']

Mri_14 = data_14_degrees['Mri']; Mr_Q_14 = data_14_degrees['Mr']; Q_14 = data_14_degrees['Q']; Qi_Q_14 = data_14_degrees['Qi']
Mri_21 = data_21_degrees['Mri']; Mr_Q_21 = data_21_degrees['Mr']; Q_14 = data_14_degrees['Q']; Qi_Q_14 = data_14_degrees['Qi']
Mri_14_21 = data_14_21_degrees['Mri']; Mr_Q_14_21 = data_14_21_degrees['Mr']; Q_14 = data_14_degrees['Q']; Qi_Q_14 = data_14_degrees['Qi']

###################################### conditions #########################################
############################# original conditions: Z>0, Zi>0, M>0 #########################
#this conditions are comming from DCs_X_Y_Theta_Phi_FP inspection module
condition_14 = ((data_14_degrees['Xf'][:] > -1500) & (data_14_degrees['Yf'][:] > -1500)
                & (data_14_degrees['Yf'][:] > -110) & (data_14_degrees['Yf'][:] < 50)
                & (data_14_degrees['Pf'][:] > -100) & (data_14_degrees['Pf'][:] < 100))

condition_21 = ((data_21_degrees['Xf'][:] > -1500) & (data_21_degrees['Yf'][:] > -1500)
                & (data_21_degrees['Yf'][:] > -110) & (data_21_degrees['Yf'][:] < 50)
                & (data_21_degrees['Pf'][:] > -100) & (data_21_degrees['Pf'][:] < 100))

condition_14_21 = ((data_14_21_degrees['Xf'][:] > -1500) & (data_14_21_degrees['Yf'][:] > -1500)
                & (data_14_21_degrees['Yf'][:] > -110) & (data_14_21_degrees['Yf'][:] < 50)
                & (data_14_21_degrees['Pf'][:] > -100) & (data_14_21_degrees['Pf'][:] < 100))


'''
----------------------------------------------------------------- Plot variables ------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------- Using "Plotter" Class ---------------------------------------------------------------------------------------------------------------
'''

################################################################## 14 degrees
M_vs_M_Q_14 = Plotter([data_14_degrees['M_Q'][condition_14], data_14_degrees['M'][condition_14]]) #Create the base with the variables in a object
M_vs_M_Q_14.SetFigSize(12,7)
M_vs_M_Q_14.SetBinX(500)
M_vs_M_Q_14.SetBinY(500)
M_vs_M_Q_14.SetFigTitle(r'M:M_Q 14$\degree$', 20)
M_vs_M_Q_14.SetLabelX('M_Q', 20)
M_vs_M_Q_14.SetLabelY('M', 20)
M_vs_M_Q_14.SetSizeTicksX(10)
M_vs_M_Q_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n M>0 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_vs_M_Q_14.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Raw_figures/')
M_vs_M_Q_14.SaveFig('M_vs_M_Q_14')
M_vs_M_Q_14.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_14.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_14 #erase M_vs_M_Q_14 (is an object)


################################################################## 21 degrees
M_vs_M_Q_21 = Plotter([data_21_degrees['M_Q'][condition_21], data_21_degrees['M'][condition_21]]) #Create the base with the variables in a object
M_vs_M_Q_21.SetFigSize(12,7)
M_vs_M_Q_21.SetBinX(500)
M_vs_M_Q_21.SetBinY(500)
M_vs_M_Q_21.SetFigTitle(r'M:M_Q 21$\degree$', 20)
M_vs_M_Q_21.SetLabelX('M_Q', 20)
M_vs_M_Q_21.SetLabelY('M', 20)
M_vs_M_Q_21.SetSizeTicksX(10)
M_vs_M_Q_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n M>0 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_vs_M_Q_21.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Raw_figures/')
M_vs_M_Q_21.SaveFig('M_vs_M_Q_21')
M_vs_M_Q_21.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_21.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_21 #erase M_vs_M_Q_21 (is an object)


################################################################## 14+21 degrees
M_vs_M_Q_14_21 = Plotter([data_14_21_degrees['M_Q'][condition_14_21], data_14_21_degrees['M'][condition_14_21]]) #Create the base with the variables in a object
M_vs_M_Q_14_21.SetFigSize(12,7)
M_vs_M_Q_14_21.SetBinX(500)
M_vs_M_Q_14_21.SetBinY(500)
M_vs_M_Q_14_21.SetFigTitle(r'M:M_Q 14$\degree$+21$\degree$', 20)
M_vs_M_Q_14_21.SetLabelX('M_Q', 20)
M_vs_M_Q_14_21.SetLabelY('M', 20)
M_vs_M_Q_14_21.SetSizeTicksX(10)
M_vs_M_Q_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n M>0 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_vs_M_Q_14_21.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Raw_figures/')
M_vs_M_Q_14_21.SaveFig('M_vs_M_Q_14_21')
M_vs_M_Q_14_21.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_14_21.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_14_21 #erase M_vs_M_Q_14_21 (is an object)


'''
------------------------------------------------------------------ Apply new conditions ------------------------------------------------------------------
'''

#adding a new condition over the mass
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


################################################################## 14 degrees
M_vs_M_Q_14 = Plotter([data_14_degrees['M_Q'][condition_mass_14], data_14_degrees['M'][condition_mass_14]]) #Create the base with the variables in a object
M_vs_M_Q_14.SetFigSize(12,7)
M_vs_M_Q_14.SetBinX(500)
M_vs_M_Q_14.SetBinY(500)
M_vs_M_Q_14.SetFigTitle(r'M:M_Q 14$\degree$', 20)
M_vs_M_Q_14.SetLabelX('M_Q', 20)
M_vs_M_Q_14.SetLabelY('M', 20)
M_vs_M_Q_14.SetSizeTicksX(10)
M_vs_M_Q_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_vs_M_Q_14.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Corrected_figures/')
M_vs_M_Q_14.SaveFig('M_vs_M_Q_14_corrected')
M_vs_M_Q_14.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_14.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_14 #erase M_vs_M_Q_14 (is an object)


################################################################## 21 degrees
M_vs_M_Q_21 = Plotter([data_21_degrees['M_Q'][condition_mass_21], data_21_degrees['M'][condition_mass_21]]) #Create the base with the variables in a object
M_vs_M_Q_21.SetFigSize(12,7)
M_vs_M_Q_21.SetBinX(500)
M_vs_M_Q_21.SetBinY(500)
M_vs_M_Q_21.SetFigTitle(r'M:M_Q 21$\degree$', 20)
M_vs_M_Q_21.SetLabelX('M_Q', 20)
M_vs_M_Q_21.SetLabelY('M', 20)
M_vs_M_Q_21.SetSizeTicksX(10)
M_vs_M_Q_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_vs_M_Q_21.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Corrected_figures/')
M_vs_M_Q_21.SaveFig('M_vs_M_Q_21_corrected')
M_vs_M_Q_21.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_21.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_21 #erase M_vs_M_Q_21 (is an object)


################################################################## 14+21 degrees
M_vs_M_Q_14_21 = Plotter([data_14_21_degrees['M_Q'][condition_mass_14_21], data_14_21_degrees['M'][condition_mass_14_21]]) #Create the base with the variables in a object
M_vs_M_Q_14_21.SetFigSize(12,7)
M_vs_M_Q_14_21.SetBinX(500)
M_vs_M_Q_14_21.SetBinY(500)
M_vs_M_Q_14_21.SetFigTitle(r'M:M_Q 14$\degree$+21$\degree$', 20)
M_vs_M_Q_14_21.SetLabelX('M_Q', 20)
M_vs_M_Q_14_21.SetLabelY('M', 20)
M_vs_M_Q_14_21.SetSizeTicksX(10)
M_vs_M_Q_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_vs_M_Q_14_21.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Corrected_figures/')
M_vs_M_Q_14_21.SaveFig('M_vs_M_Q_14_21_corrected')
M_vs_M_Q_14_21.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_14_21.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_14_21 #erase M_vs_M_Q_14_21 (is an object)


'''
---------------------------------------------------------------- Analysis over charge --------------------------------------------------------------------------
'''

###################################### Testing if Q variable is Q measured ##############################################
Q_measured = (data_14_21_degrees['M'][condition_mass_14_21]/data_14_21_degrees['M_Q'][condition_mass_14_21])

################################################################## 14+21 degrees
Q_vs_M_Q_14_21 = Plotter([data_14_21_degrees['M_Q'][condition_mass_14_21], Q_measured]) #Create the base with the variables in a object
Q_vs_M_Q_14_21.SetFigSize(12,7)
Q_vs_M_Q_14_21.SetBinX(500)
Q_vs_M_Q_14_21.SetBinY(500)
Q_vs_M_Q_14_21.SetFigTitle(r'Q:M_Q 14$\degree$+21$\degree$', 20)
Q_vs_M_Q_14_21.SetLabelX(r'M_Q $\equiv (A/Q)$', 20)
Q_vs_M_Q_14_21.SetLabelY(r'Q_measured', 20)
Q_vs_M_Q_14_21.SetSizeTicksX(10)
Q_vs_M_Q_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
Q_vs_M_Q_14_21.Histo_2D() #Draw it
######### Save and show the created figure
Q_vs_M_Q_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Q_analysis/')
Q_vs_M_Q_14_21.SaveFig('Q_variable_is_Q_measured')
Q_vs_M_Q_14_21.Show(1) #show during 1 seconds, the close authomatically
Q_vs_M_Q_14_21.Close() #close all windows, axes and figures running backend
del Q_vs_M_Q_14_21 #erase Q_vs_M_Q_14_21 (is an object)


#################################################### Now, we can use Q #####################################################
################################################################## 14+21 degrees
Q_vs_M_Q_14_21 = Plotter([data_14_21_degrees['M_Q'][condition_mass_14_21], data_14_21_degrees['Q'][condition_mass_14_21]]) #Create the base with the variables in a object
Q_vs_M_Q_14_21.SetFigSize(12,7)
Q_vs_M_Q_14_21.SetBinX(500)
Q_vs_M_Q_14_21.SetBinY(500)
Q_vs_M_Q_14_21.SetFigTitle(r'Q:M_Q 14$\degree$+21$\degree$', 20)
Q_vs_M_Q_14_21.SetLabelX(r'M_Q $\equiv (A/Q)$', 20)
Q_vs_M_Q_14_21.SetLabelY(r'Q $\equiv Q^m = \frac{A^m}{(A/Q)}$', 20)
Q_vs_M_Q_14_21.SetSizeTicksX(10)
Q_vs_M_Q_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
Q_vs_M_Q_14_21.Histo_2D() #Draw it
######### Save and show the created figure
Q_vs_M_Q_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Q_analysis/')
Q_vs_M_Q_14_21.SaveFig('Q_vs_M_Q_14_21')
Q_vs_M_Q_14_21.Show(1) #show during 1 seconds, the close authomatically
Q_vs_M_Q_14_21.Close() #close all windows, axes and figures running backend
del Q_vs_M_Q_14_21 #erase Q_vs_M_Q_14_21 (is an object)


############################################################### Q measured histograms #########################################
################################################################## 14 degrees
Q_measured_14 = Plotter([data_14_degrees['Q'][condition_mass_14]]) #Create the base with the variables in a object
Q_measured_14.SetFigSize(12,7)
Q_measured_14.SetBinX(400)
Q_measured_14.SetFigTitle(r'$Q^{m}$ $\equiv$ Q = $\frac{A}{(A/Q)}$        14$\degree$', 20)
Q_measured_14.SetLabelX('Q', 20)
Q_measured_14.SetLabelY('counts', 20)
Q_measured_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
Q_measured_14.Histo_1D() #Draw it
######### Save and show the created figure
Q_measured_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Q_analysis/')
Q_measured_14.SaveFig('Q_measured_14')
Q_measured_14.Show(1) #show during 1 seconds, the close authomatically
Q_measured_14.Close() #close all windows, axes and figures running backend
del Q_measured_14 #erase Q_measured_14 (is an object)


################################################################## 21 degrees
Q_measured_21 = Plotter([data_21_degrees['Q'][condition_mass_21]]) #Create the base with the variables in a object
Q_measured_21.SetFigSize(12,7)
Q_measured_21.SetBinX(400)
Q_measured_21.SetFigTitle(r'$Q^{m}$ $\equiv$ Q = $\frac{A}{(A/Q)}$        21$\degree$', 20)
Q_measured_21.SetLabelX('Q', 20)
Q_measured_21.SetLabelY('counts', 20)
Q_measured_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
Q_measured_21.Histo_1D() #Draw it
######### Save and show the created figure
Q_measured_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Q_analysis/')
Q_measured_21.SaveFig('Q_measured_21')
Q_measured_21.Show(1) #show during 1 seconds, the close authomatically
Q_measured_21.Close() #close all windows, axes and figures running backend
del Q_measured_21 #erase Q_measured_21 (is an object)


################################################################## 14+21 degrees
Q_measured_14_21 = Plotter([data_14_21_degrees['Q'][condition_mass_14_21]]) #Create the base with the variables in a object
Q_measured_14_21.SetFigSize(12,7)
Q_measured_14_21.SetBinX(400)
Q_measured_14_21.SetFigTitle(r'$Q^{m}$ $\equiv$ Q = $\frac{A}{(A/Q)}$        14$\degree$+21$\degree$', 20)
Q_measured_14_21.SetLabelX('Q', 20)
Q_measured_14_21.SetLabelY('counts', 20)
Q_measured_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
Q_measured_14_21.Histo_1D() #Draw it
######### Save and show the created figure
Q_measured_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Q_analysis/')
Q_measured_14_21.SaveFig('Q_measured_14_21')
Q_measured_14_21.Show(1) #show during 1 seconds, the close authomatically
Q_measured_14_21.Close() #close all windows, axes and figures running backend
del Q_measured_14_21 #erase Q_measured_14_21 (is an object)



########################################### Q int histograms #########################################

###################################### Testing if Qi variable is Q integer ##############################################

Q_integer_14 = data_14_degrees['M'][condition_mass_14]/data_14_degrees['M_Q'][condition_mass_14] + 0.5
Q_integer_14 = Q_integer_14.astype(int)

################################################################## 14 degrees
Q_int_14 = Plotter([Q_integer_14]) #Create the base with the variables in a object
Q_int_14.SetFigSize(12,7)
Q_int_14.SetBinX(300)
Q_int_14.SetFigTitle(r'Q integer $\equiv Qi = int\left(\frac{A}{(A/M)} + 0.5\right)$        14$\degree$', 20)
Q_int_14.SetLabelX('Qi', 20)
Q_int_14.SetLabelY('counts', 20)
Q_int_14.SetSizeTicksX(10)
Q_int_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
Q_int_14.Histo_1D() #Draw it
######### Save and show the created figure
Q_int_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Q_analysis/')
Q_int_14.SaveFig('Qi_variable_is_Q_integer_14')
Q_int_14.Show(1) #show during 1 seconds, the close authomatically
Q_int_14.Close() #close all windows, axes and figures running backend
del Q_int_14 #erase Q_int_14 (is an object)

#################################################### Now, we can use Qi #####################################################

################################################################## 14 degrees
Qi_14 = Plotter([data_14_degrees['Qi'][condition_mass_14]]) #Create the base with the variables in a object
Qi_14.SetFigSize(12,7)
Qi_14.SetBinX(300)
Qi_14.SetFigTitle(r'$Qi = int\left(\frac{A}{(A/M)} + 0.5\right)$        14$\degree$', 20)
Qi_14.SetLabelX('Qi', 20)
Qi_14.SetLabelY('counts', 20)
Qi_14.SetSizeTicksX(10)
Qi_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
Qi_14.Histo_1D() #Draw it
######### Save and show the created figure
Qi_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Q_analysis/')
Qi_14.SaveFig('Qi_14')
Qi_14.Show(1) #show during 1 seconds, the close authomatically
Qi_14.Close() #close all windows, axes and figures running backend
del Qi_14 #erase Qi_14 (is an object)


################################################################## 21 degrees
Qi_21 = Plotter([data_21_degrees['Qi'][condition_mass_21]]) #Create the base with the variables in a object
Qi_21.SetFigSize(12,7)
Qi_21.SetBinX(300)
Qi_21.SetFigTitle(r'$Qi = int\left(\frac{A}{(A/M)} + 0.5\right)$        21$\degree$', 20)
Qi_21.SetLabelX('Qi', 20)
Qi_21.SetLabelY('counts', 20)
Qi_21.SetSizeTicksX(10)
Qi_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
Qi_21.Histo_1D() #Draw it
######### Save and show the created figure
Qi_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Q_analysis/')
Qi_21.SaveFig('Qi_21')
Qi_21.Show(1) #show during 1 seconds, the close authomatically
Qi_21.Close() #close all windows, axes and figures running backend
del Qi_21 #erase Qi_21 (is an object)


################################################################## 14 degrees
Qi_14_21 = Plotter([data_14_21_degrees['Qi'][condition_mass_14_21]]) #Create the base with the variables in a object
Qi_14_21.SetFigSize(12,7)
Qi_14_21.SetBinX(300)
Qi_14_21.SetFigTitle(r'$Qi = int\left(\frac{A}{(A/M)} + 0.5\right)$        14$\degree$+21$\degree$', 20)
Qi_14_21.SetLabelX('Qi', 20)
Qi_14_21.SetLabelY('counts', 20)
Qi_14_21.SetSizeTicksX(10)
Qi_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
Qi_14_21.Histo_1D() #Draw it
######### Save and show the created figure
Qi_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Q_analysis/')
Qi_14_21.SaveFig('Qi_14_21')
Qi_14_21.Show(1) #show during 1 seconds, the close authomatically
Qi_14_21.Close() #close all windows, axes and figures running backend
del Qi_14_21 #erase Qi_14_21 (is an object)



########################################### M measured and M reconstructed histograms #########################################

################################################################## 14 degrees
A_meas_14 = Plotter([data_14_degrees['M'][condition_mass_14]]) #Create the base with the variables in a object
A_meas_14.SetFigSize(12,7)
A_meas_14.SetBinX(1000)
A_meas_14.SetFigTitle(r'M measured $\equiv A^{m}$        14$\degree$', 20)
A_meas_14.SetLabelX('M', 20)
A_meas_14.SetLabelY('counts', 20)
A_meas_14.SetSizeTicksX(10)
A_meas_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
A_meas_14.Histo_1D() #Draw it
######### Save and show the created figure
A_meas_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/')
A_meas_14.SaveFig('M_measured_14')
A_meas_14.Show(1) #show during 1 seconds, the close authomatically
A_meas_14.Close() #close all windows, axes and figures running backend
del A_meas_14 #erase A_meas_14 (is an object)


################################################################## 21 degrees
A_meas_21 = Plotter([data_21_degrees['M'][condition_mass_21]]) #Create the base with the variables in a object
A_meas_21.SetFigSize(12,7)
A_meas_21.SetBinX(1000)
A_meas_21.SetFigTitle(r'M measured $\equiv A^{m}$        21$\degree$', 20)
A_meas_21.SetLabelX('M', 20)
A_meas_21.SetLabelY('counts', 20)
A_meas_21.SetSizeTicksX(10)
A_meas_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
A_meas_21.Histo_1D() #Draw it
######### Save and show the created figure
A_meas_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/')
A_meas_21.SaveFig('M_measured_21')
A_meas_21.Show(1) #show during 1 seconds, the close authomatically
A_meas_21.Close() #close all windows, axes and figures running backend
del A_meas_21 #erase A_meas_21 (is an object)


################################################################## 14+21 degrees
A_meas_14_21 = Plotter([data_14_21_degrees['M'][condition_mass_14_21]]) #Create the base with the variables in a object
A_meas_14_21.SetFigSize(12,7)
A_meas_14_21.SetBinX(1000)
A_meas_14_21.SetFigTitle(r'M measured $\equiv A^{m}$        14$\degree$+21$\degree$', 20)
A_meas_14_21.SetLabelX('M', 20)
A_meas_14_21.SetLabelY('counts', 20)
A_meas_14_21.SetSizeTicksX(10)
A_meas_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
A_meas_14_21.Histo_1D() #Draw it
######### Save and show the created figure
A_meas_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/')
A_meas_14_21.SaveFig('M_measured_14_21')
A_meas_14_21.Show(1) #show during 1 seconds, the close authomatically
A_meas_14_21.Close() #close all windows, axes and figures running backend
del A_meas_14_21 #erase A_meas_14_21 (is an object)


########################################## M reconstructed = Qi * M_Q = int(M/M_Q + 0.5)*M_Q
M_recons_14 = data_14_degrees['Qi'][condition_mass_14] * data_14_degrees['M_Q'][condition_mass_14]
M_recons_21 = data_21_degrees['Qi'][condition_mass_21] * data_21_degrees['M_Q'][condition_mass_21]
M_recons_14_21 = data_14_21_degrees['Qi'][condition_mass_14_21] * data_14_21_degrees['M_Q'][condition_mass_14_21]

################################################################## 14 degrees
A_reco_14 = Plotter([M_recons_14]) #Create the base with the variables in a object
A_reco_14.SetFigSize(12,7)
A_reco_14.SetBinX(1000)
A_reco_14.SetFigTitle(r'M reconstructed $\equiv A^{r}$        14$\degree$', 20)
A_reco_14.SetLabelX('M', 20)
A_reco_14.SetLabelY('counts', 20)
A_reco_14.SetSizeTicksX(10)
A_reco_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
A_reco_14.Histo_1D() #Draw it
######### Save and show the created figure
A_reco_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/')
A_reco_14.SaveFig('M_reconstructed_14')
A_reco_14.Show(1) #show during 1 seconds, the close authomatically
A_reco_14.Close() #close all windows, axes and figures running backend
del A_reco_14 #erase A_reco_14 (is an object)


################################################################## 21 degrees
A_reco_21 = Plotter([M_recons_21]) #Create the base with the variables in a object
A_reco_21.SetFigSize(12,7)
A_reco_21.SetBinX(1000)
A_reco_21.SetFigTitle(r'M reconstructed $\equiv A^{r}$        21$\degree$', 20)
A_reco_21.SetLabelX('M', 20)
A_reco_21.SetLabelY('counts', 20)
A_reco_21.SetSizeTicksX(10)
A_reco_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
A_reco_21.Histo_1D() #Draw it
######### Save and show the created figure
A_reco_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/')
A_reco_21.SaveFig('M_reconstructed_21')
A_reco_21.Show(1) #show during 1 seconds, the close authomatically
A_reco_21.Close() #close all windows, axes and figures running backend
del A_reco_21 #erase A_reco_21 (is an object)


################################################################## 14+21 degrees
A_reco_14_21 = Plotter([M_recons_14_21]) #Create the base with the variables in a object
A_reco_14_21.SetFigSize(12,7)
A_reco_14_21.SetBinX(1000)
A_reco_14_21.SetFigTitle(r'M reconstructed $\equiv A^{r}$        14$\degree$+21$\degree$', 20)
A_reco_14_21.SetLabelX('M', 20)
A_reco_14_21.SetLabelY('counts', 20)
A_reco_14_21.SetSizeTicksX(10)
A_reco_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
A_reco_14_21.Histo_1D() #Draw it
######### Save and show the created figure
A_reco_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/')
A_reco_14_21.SaveFig('M_reconstructed_14_21')
A_reco_14_21.Show(1) #show during 1 seconds, the close authomatically
A_reco_14_21.Close() #close all windows, axes and figures running backend
del A_reco_14_21 #erase A_reco_14_21 (is an object)



###################################### Testing if Mri variable is M reconstructed integer ##############################################

M_reco_int_14 = M_recons_14 + 0.5
M_reco_int_14 = M_reco_int_14.astype(int)

################################################################## 14 degrees
A_ri_14 = Plotter([M_reco_int_14]) #Create the base with the variables in a object
A_ri_14.SetFigSize(12,7)
A_ri_14.SetBinX(500)
A_ri_14.SetFigTitle(r'M reconstructed integer $\equiv Mri = int(Mr + 0.5)$        14$\degree$', 20)
A_ri_14.SetLabelX('M reconstructed integer', 20)
A_ri_14.SetLabelY('counts', 20)
A_ri_14.SetSizeTicksX(10)
A_ri_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
A_ri_14.Histo_1D() #Draw it
######### Save and show the created figure
A_ri_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/')
A_ri_14.SaveFig('Mri_variable_is_M_reco_int_14')
A_ri_14.Show(1) #show during 1 seconds, the close authomatically
A_ri_14.Close() #close all windows, axes and figures running backend
del A_ri_14 #erase A_ri_14 (is an object)


#################################################### Now, we can use Mri #####################################################

################################################################## 14 degrees
Mri_14 = Plotter([data_14_degrees['Mri'][condition_mass_14]]) #Create the base with the variables in a object
Mri_14.SetFigSize(12,7)
Mri_14.SetBinX(500)
Mri_14.SetFigTitle(r'M reconstructed integer $\equiv Mri = int(Mr + 0.5)$        14$\degree$', 20)
Mri_14.SetLabelX('Qi', 20)
Mri_14.SetLabelY('counts', 20)
Mri_14.SetSizeTicksX(10)
Mri_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
Mri_14.Histo_1D() #Draw it
######### Save and show the created figure
Mri_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/')
Mri_14.SaveFig('Mri_14')
Mri_14.Show(1) #show during 1 seconds, the close authomatically
Mri_14.Close() #close all windows, axes and figures running backend
del Mri_14 #erase Mri_14 (is an object)


################################################################## 21 degrees
Mri_21 = Plotter([data_21_degrees['Mri'][condition_mass_21]]) #Create the base with the variables in a object
Mri_21.SetFigSize(12,7)
Mri_21.SetBinX(500)
Mri_21.SetFigTitle(r'M reconstructed integer $\equiv Mri = int(Mr + 0.5)$        21$\degree$', 20)
Mri_21.SetLabelX('Qi', 20)
Mri_21.SetLabelY('counts', 20)
Mri_21.SetSizeTicksX(10)
Mri_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
Mri_21.Histo_1D() #Draw it
######### Save and show the created figure
Mri_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/')
Mri_21.SaveFig('Mri_21')
Mri_21.Show(1) #show during 1 seconds, the close authomatically
Mri_21.Close() #close all windows, axes and figures running backend
del Mri_21 #erase Mri_21 (is an object)


################################################################## 14+21 degrees
Mri_14_21 = Plotter([data_14_21_degrees['Mri'][condition_mass_14_21]]) #Create the base with the variables in a object
Mri_14_21.SetFigSize(12,7)
Mri_14_21.SetBinX(500)
Mri_14_21.SetFigTitle(r'M reconstructed integer $\equiv Mri = int(Mr + 0.5)$        14$\degree$+21$\degree$', 18)
Mri_14_21.SetLabelX('Qi', 20)
Mri_14_21.SetLabelY('counts', 20)
Mri_14_21.SetSizeTicksX(10)
Mri_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
Mri_14_21.Histo_1D() #Draw it
######### Save and show the created figure
Mri_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/')
Mri_14_21.SaveFig('Mri_14_21')
Mri_14_21.Show(1) #show during 1 seconds, the close authomatically
Mri_14_21.Close() #close all windows, axes and figures running backend
del Mri_14_21 #erase Mri_14_21 (is an object)



################################################### M measured and M reconstructed special plots ##########################################################

################################################### 14 degrees
fig = plt.figure(figsize=(12,7))

ax1 = fig.add_subplot(111)
ax1.hist(data_14_degrees['M'][condition_mass_14], bins=1000, weights=None, histtype='step', align='mid', orientation='vertical', color='r', label = 'M measured')
ax1.hist(data_14_degrees['Qi'][condition_mass_14] * data_14_degrees['M_Q'][condition_mass_14], bins=1000, weights=None, histtype='step', align='mid', orientation='vertical', color='b', label = 'M reconstructed')

ax1.set_ylabel(r'counts', fontsize=20)
ax1.set_xlabel(r'Fragment mass [uma]', fontsize=20)
ax1.grid(True)

plt.suptitle(r'M reconstructed and M measured        14$\degree$', fontsize=18, x=0.4, y=0.94)

plt.gca().set_xticks(np.arange(70.0, 180.0, 10.0), minor=True)
ax1.set_xlim([70.0, 180.0])
ax1.set_ylim([0.0, 28000])
ax1.xaxis.grid(True)
ax1.legend(loc=2, fontsize = 12)
plt.text(0.9, 0.3, 'Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500', fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='blue', pad=8.0), ha='center', va='center')

# Create a set of inset Axes: these should fill the bounding box allocated to
# them.
ax2 = plt.axes([0,0,1,1])
# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax1, [0.75,0.7,0.3,0.4])
ax2.set_axes_locator(ip)
# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
mark_inset(ax1, ax2, loc1=2, loc2=4, fc="none", ec='0.5')

# The data into the ax2
ax2.hist(data_14_degrees['M'][condition_mass_14], bins=1000, weights=None, histtype='step', align='mid', orientation='vertical', color='r', label = 'M measured')
ax2.hist(data_14_degrees['Qi'][condition_mass_14] * data_14_degrees['M_Q'][condition_mass_14], bins=1000, weights=None, histtype='step', align='mid', orientation='vertical', color='b', label = 'M reconstructed')

ax2.set_xlim([115.0, 125.0])
ax2.set_xticks([115, 120, 125])
ax2.set_ylim([7000, 18500])
ax2.grid(True, which='both')

print('Saving figure as:' + basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/' + 'M_and_Mr_14' + '.png')
print('\n')
plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/' + 'M_and_Mr_14' + '.png', format='png')



################################################### 21 degrees
fig = plt.figure(figsize=(12,7))

ax1 = fig.add_subplot(111)
ax1.hist(data_21_degrees['M'][condition_mass_21], bins=1000, weights=None, histtype='step', align='mid', orientation='vertical', color='r', label = 'M measured')
ax1.hist(data_21_degrees['Qi'][condition_mass_21] * data_21_degrees['M_Q'][condition_mass_21], bins=1000, weights=None, histtype='step', align='mid', orientation='vertical', color='b', label = 'M reconstructed')

ax1.set_ylabel(r'counts', fontsize=20)
ax1.set_xlabel(r'Fragment mass [uma]', fontsize=20)
ax1.grid(True)

plt.suptitle(r'M reconstructed and M measured        21$\degree$', fontsize=18, x=0.4, y=0.94)

plt.gca().set_xticks(np.arange(70.0, 180.0, 10.0), minor=True)
ax1.set_xlim([70.0, 180.0])
ax1.set_ylim([0.0, 45000])
ax1.xaxis.grid(True)
ax1.legend(loc=2, fontsize = 12)
plt.text(0.9, 0.3, 'Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500', fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='blue', pad=8.0), ha='center', va='center')

# Create a set of inset Axes: these should fill the bounding box allocated to
# them.
ax2 = plt.axes([0,0,1,1])
# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax1, [0.75,0.7,0.3,0.4])
ax2.set_axes_locator(ip)
# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
mark_inset(ax1, ax2, loc1=2, loc2=4, fc="none", ec='0.5')

# The data into the ax2
ax2.hist(data_21_degrees['M'][condition_mass_21], bins=1000, weights=None, histtype='step', align='mid', orientation='vertical', color='r', label = 'M measured')
ax2.hist(data_21_degrees['Qi'][condition_mass_21] * data_21_degrees['M_Q'][condition_mass_21], bins=1000, weights=None, histtype='step', align='mid', orientation='vertical', color='b', label = 'M reconstructed')

ax2.set_xlim([115.0, 125.0])
ax2.set_xticks([115, 120, 125])
ax2.set_ylim([18000, 37000])
ax2.grid(True, which='both')

print('Saving figure as:' + basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/' + 'M_and_Mr_21' + '.png')
print('\n')
plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/' + 'M_and_Mr_21' + '.png', format='png')



################################################### 14+21 degrees
fig = plt.figure(figsize=(12,7))

ax1 = fig.add_subplot(111)
ax1.hist(data_14_21_degrees['M'][condition_mass_14_21], bins=1000, weights=None, histtype='step', align='mid', orientation='vertical', color='r', label = 'M measured')
ax1.hist(data_14_21_degrees['Qi'][condition_mass_14_21] * data_14_21_degrees['M_Q'][condition_mass_14_21], bins=1000, weights=None, histtype='step', align='mid', orientation='vertical', color='b', label = 'M reconstructed')

ax1.set_ylabel(r'counts', fontsize=20)
ax1.set_xlabel(r'Fragment mass [uma]', fontsize=20)
ax1.grid(True)

plt.suptitle(r'M reconstructed and M measured        14$\degree$+21$\degree$', fontsize=18, x=0.4, y=0.94)

plt.gca().set_xticks(np.arange(70.0, 180.0, 10.0), minor=True)
ax1.set_xlim([70.0, 180.0])
ax1.set_ylim([0.0, 60000])
ax1.xaxis.grid(True)
ax1.legend(loc=2, fontsize = 12)
plt.text(0.9, 0.3, 'Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500', fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='blue', pad=8.0), ha='center', va='center')

# Create a set of inset Axes: these should fill the bounding box allocated to
# them.
ax2 = plt.axes([0,0,1,1])
# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax1, [0.75,0.7,0.3,0.4])
ax2.set_axes_locator(ip)
# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
mark_inset(ax1, ax2, loc1=2, loc2=4, fc="none", ec='0.5')

# The data into the ax2
ax2.hist(data_14_21_degrees['M'][condition_mass_14_21], bins=1000, weights=None, histtype='step', align='mid', orientation='vertical', color='r', label = 'M measured')
ax2.hist(data_14_21_degrees['Qi'][condition_mass_14_21] * data_14_21_degrees['M_Q'][condition_mass_14_21], bins=1000, weights=None, histtype='step', align='mid', orientation='vertical', color='b', label = 'M reconstructed')

ax2.set_xlim([115.0, 125.0])
ax2.set_xticks([115, 120, 125])
ax2.set_ylim([27000, 52000])
ax2.grid(True, which='both')

print('Saving figure as:' + basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/' + 'M_and_Mr_14_21' + '.png')
print('\n')
plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_analysis/' + 'M_and_Mr_14_21' + '.png', format='png')
