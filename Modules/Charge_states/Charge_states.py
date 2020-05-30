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
M_vs_M_Q_14.SetFigSize(10,7)
M_vs_M_Q_14.SetBinX(500)
M_vs_M_Q_14.SetBinY(500)
M_vs_M_Q_14.SetFigTitle('M:M_Q 14 degrees', 20)
M_vs_M_Q_14.SetLabelX('M_Q', 20)
M_vs_M_Q_14.SetLabelY('M', 20)
M_vs_M_Q_14.SetSizeTicksX(10)
M_vs_M_Q_14.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Raw_figures/')
M_vs_M_Q_14.SaveFig('M_vs_M_Q_14')
M_vs_M_Q_14.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_14.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_14 #erase M_vs_M_Q_14 (is an object)


################################################################## 21 degrees
M_vs_M_Q_21 = Plotter([data_21_degrees['M_Q'][condition_21], data_21_degrees['M'][condition_21]]) #Create the base with the variables in a object
M_vs_M_Q_21.SetFigSize(10,7)
M_vs_M_Q_21.SetBinX(500)
M_vs_M_Q_21.SetBinY(500)
M_vs_M_Q_21.SetFigTitle('M:M_Q 21 degrees', 20)
M_vs_M_Q_21.SetLabelX('M_Q', 20)
M_vs_M_Q_21.SetLabelY('M', 20)
M_vs_M_Q_21.SetSizeTicksX(10)
M_vs_M_Q_21.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Raw_figures/')
M_vs_M_Q_21.SaveFig('M_vs_M_Q_21')
M_vs_M_Q_21.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_21.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_21 #erase M_vs_M_Q_21 (is an object)


################################################################## 14+21 degrees
M_vs_M_Q_14_21 = Plotter([data_14_21_degrees['M_Q'][condition_14_21], data_14_21_degrees['M'][condition_14_21]]) #Create the base with the variables in a object
M_vs_M_Q_14_21.SetFigSize(10,7)
M_vs_M_Q_14_21.SetBinX(500)
M_vs_M_Q_14_21.SetBinY(500)
M_vs_M_Q_14_21.SetFigTitle('M:M_Q 14+21 degrees', 20)
M_vs_M_Q_14_21.SetLabelX('M_Q', 20)
M_vs_M_Q_14_21.SetLabelY('M', 20)
M_vs_M_Q_14_21.SetSizeTicksX(10)
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
M_vs_M_Q_14.SetFigSize(10,7)
M_vs_M_Q_14.SetBinX(500)
M_vs_M_Q_14.SetBinY(500)
M_vs_M_Q_14.SetFigTitle('M:M_Q 14 degrees', 20)
M_vs_M_Q_14.SetLabelX('M_Q', 20)
M_vs_M_Q_14.SetLabelY('M', 20)
M_vs_M_Q_14.SetSizeTicksX(10)
M_vs_M_Q_14.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Corrected_figures/')
M_vs_M_Q_14.SaveFig('M_vs_M_Q_14_corrected')
M_vs_M_Q_14.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_14.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_14 #erase M_vs_M_Q_14 (is an object)


################################################################## 21 degrees
M_vs_M_Q_21 = Plotter([data_21_degrees['M_Q'][condition_mass_21], data_21_degrees['M'][condition_mass_21]]) #Create the base with the variables in a object
M_vs_M_Q_21.SetFigSize(10,7)
M_vs_M_Q_21.SetBinX(500)
M_vs_M_Q_21.SetBinY(500)
M_vs_M_Q_21.SetFigTitle('M:M_Q 21 degrees', 20)
M_vs_M_Q_21.SetLabelX('M_Q', 20)
M_vs_M_Q_21.SetLabelY('M', 20)
M_vs_M_Q_21.SetSizeTicksX(10)
M_vs_M_Q_21.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Corrected_figures/')
M_vs_M_Q_21.SaveFig('M_vs_M_Q_21_corrected')
M_vs_M_Q_21.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_21.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_21 #erase M_vs_M_Q_21 (is an object)


################################################################## 14+21 degrees
M_vs_M_Q_14_21 = Plotter([data_14_21_degrees['M_Q'][condition_mass_14_21], data_14_21_degrees['M'][condition_mass_14_21]]) #Create the base with the variables in a object
M_vs_M_Q_14_21.SetFigSize(10,7)
M_vs_M_Q_14_21.SetBinX(500)
M_vs_M_Q_14_21.SetBinY(500)
M_vs_M_Q_14_21.SetFigTitle('M:M_Q 14+21 degrees', 20)
M_vs_M_Q_14_21.SetLabelX('M_Q', 20)
M_vs_M_Q_14_21.SetLabelY('M', 20)
M_vs_M_Q_14_21.SetSizeTicksX(10)
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
Q_vs_M_Q_14_21.SetFigSize(10,7)
Q_vs_M_Q_14_21.SetBinX(500)
Q_vs_M_Q_14_21.SetBinY(500)
Q_vs_M_Q_14_21.SetFigTitle('Q:M_Q 14+21 degrees', 20)
Q_vs_M_Q_14_21.SetLabelX(r'M_Q $\equiv (A/Q)$', 20)
Q_vs_M_Q_14_21.SetLabelY(r'Q_measured', 20)
Q_vs_M_Q_14_21.SetSizeTicksX(10)
Q_vs_M_Q_14_21.Histo_2D() #Draw it
######### Save and show the created figure
Q_vs_M_Q_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Q_Comprobation/')
Q_vs_M_Q_14_21.SaveFig('Q_variable_is_Q_measured')
Q_vs_M_Q_14_21.Show(1) #show during 1 seconds, the close authomatically
Q_vs_M_Q_14_21.Close() #close all windows, axes and figures running backend
del Q_vs_M_Q_14_21 #erase Q_vs_M_Q_14_21 (is an object)


#################################################### Now, we can use Q #####################################################
################################################################## 14+21 degrees
Q_vs_M_Q_14_21 = Plotter([data_14_21_degrees['M_Q'][condition_mass_14_21], data_14_21_degrees['Q'][condition_mass_14_21]]) #Create the base with the variables in a object
Q_vs_M_Q_14_21.SetFigSize(10,7)
Q_vs_M_Q_14_21.SetBinX(500)
Q_vs_M_Q_14_21.SetBinY(500)
Q_vs_M_Q_14_21.SetFigTitle('Q:M_Q 14+21 degrees', 20)
Q_vs_M_Q_14_21.SetLabelX(r'M_Q $\equiv (A/Q)$', 20)
Q_vs_M_Q_14_21.SetLabelY(r'Q $\equiv Q^m = \frac{A^m}{(A/Q)}$', 20)
Q_vs_M_Q_14_21.SetSizeTicksX(10)
Q_vs_M_Q_14_21.Histo_2D() #Draw it
######### Save and show the created figure
Q_vs_M_Q_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/Q_Comprobation/')
Q_vs_M_Q_14_21.SaveFig('Q_vs_M_Q_14_21')
Q_vs_M_Q_14_21.Show(1) #show during 1 seconds, the close authomatically
Q_vs_M_Q_14_21.Close() #close all windows, axes and figures running backend
del Q_vs_M_Q_14_21 #erase Q_vs_M_Q_14_21 (is an object)
