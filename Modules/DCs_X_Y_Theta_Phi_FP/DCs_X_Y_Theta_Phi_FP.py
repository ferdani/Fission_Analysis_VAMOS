#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:38:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

DCs_X_Y_Theta_Phi_FP_MODULE -- The DC's variables checking module (FP indicates Focal-Plane)

The code generates:
-- Outputfiles/Figures/     All the plots resulting from this module are saved here

"""
'''
----------------------------------------------------------------- Protected part ----------------------------------------------------------------------------------------------------------------
'''
import os, sys
sys.path.append('.')
sys.path.append('..')
basepath = os.path.abspath(__file__).rsplit('/Fission_Analysis_VAMOS/',1)[0]+'/Fission_Analysis_VAMOS/'
sys.path.append(basepath)
Module_path = basepath + '/Modules/DCs_X_Y_Theta_Phi_FP/'
sys.path.append(Module_path)
#print('We are working from here' + os.getcwd())

'''
---------------------------------------------------- Import packages and Framework functions ----------------------------------------------------------------------------------------------------
'''
import numpy as np
import root_numpy as rn
import Framework.read_and_save.read_and_save as RAS
from Plotter.Plotter import Plotter

'''
---------------------------------------------- Open and read .hdf5 original file like a hdf5 object ----------------------------------------------------------------------------------
'''
hdf5_folder_path = basepath + 'Data_hdf5/DCs_X_Y_Theta_Phi_FP/' #The folder with files after the calibrations comming from RootA transformed in hdf5
file_14_degrees = 'Analysis_14_file_DC_variables' #Without .hdf5 extension
file_21_degrees = 'Analysis_21_file_DC_variables' #Without .hdf5 extension
file_14_21_degrees = 'Analysis_14+21_file_DC_variables' #Without .hdf5 extension

data_14_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_14_degrees) #Array-matrix with our data
data_21_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_21_degrees) #Array-matrix with our data
data_14_21_degrees= RAS.Read_hdf5_file(hdf5_folder_path, file_14_21_degrees) #Array-matrix with our data

#Variables aka branches are: ['Pf', 'PhiL', 'Tf', 'ThetaL', 'Xf', 'Yf'] ---> data_14_degrees.keys()

Xf_14 = data_14_degrees['Xf']; Yf_14 = data_14_degrees['Yf']
Xf_21 = data_21_degrees['Xf']; Yf_21 = data_21_degrees['Yf']
Xf_14_21 = data_14_21_degrees['Xf']; Yf_14_21 = data_14_21_degrees['Yf']

Pf_14 = data_14_degrees['Pf']; Tf_14 = data_14_degrees['Tf']
Pf_21 = data_21_degrees['Pf']; Tf_21 = data_21_degrees['Tf']
Pf_14_21 = data_14_21_degrees['Pf']; Tf_14_21 = data_14_21_degrees['Tf']

PhiL_14 = data_14_degrees['PhiL']; ThetaL_14 = data_14_degrees['ThetaL']
PhiL_21 = data_21_degrees['PhiL']; ThetaL_21 = data_21_degrees['ThetaL']
PhiL_14_21 = data_14_21_degrees['PhiL']; ThetaL_14_21 = data_14_21_degrees['ThetaL']

###################################### conditions #########################################
############################# original conditions: Z>0, Zi>0, M>0 #########################
condition_14 = (data_14_degrees['Xf'][:] > -1500) & (data_14_degrees['Yf'][:] > -1500) #it is a boolean index to apply in a dataset
condition_21 = (data_21_degrees['Xf'][:] > -1500) & (data_21_degrees['Yf'][:] > -1500) #it is a boolean index to apply in a dataset
condition_14_21 = (data_14_21_degrees['Xf'][:] > -1500) & (data_14_21_degrees['Yf'][:] > -1500) #it is a boolean index to apply in a dataset

'''
----------------------------------------------------------------- Plot variables ------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------- Using "Plotter" Class ---------------------------------------------------------------------------------------------------------------
'''
################################################################## 14 degrees
Yf_vs_Xf_14 = Plotter([data_14_degrees['Xf'][condition_14], data_14_degrees['Yf'][condition_14]]) #Create the base with the variables in a object
Yf_vs_Xf_14.SetFigSize(10,7)
Yf_vs_Xf_14.SetBinX(500)
Yf_vs_Xf_14.SetBinY(500)
Yf_vs_Xf_14.SetFigTitle('Xf:Yf 14 degrees', 15)
Yf_vs_Xf_14.SetLabelX('Xf', 15)
Yf_vs_Xf_14.SetLabelY('Yf', 15)
Yf_vs_Xf_14.SetSizeTicksX(10)
Yf_vs_Xf_14.Histo_2D() #Draw it
######### Save and show the created figure
Yf_vs_Xf_14.SetOutDir(basepath + 'Modules/DCs_X_Y_Theta_Phi_FP/Outputfiles/Figures/')
Yf_vs_Xf_14.SaveFig('Yf_vs_Xf_14')
Yf_vs_Xf_14.Show(1) #show during 1 seconds, the close authomatically
Yf_vs_Xf_14.Close() #close all windows, axes and figures running backend
del Yf_vs_Xf_14 #erase Yf_vs_Xf_14 (is an object)


Pf_vs_Tf_14 = Plotter([data_14_degrees['Tf'][condition_14], data_14_degrees['Pf'][condition_14]]) #Create the base with the variables in a object
Pf_vs_Tf_14.SetFigSize(10,7)
Pf_vs_Tf_14.SetBinX(500)
Pf_vs_Tf_14.SetBinY(500)
Pf_vs_Tf_14.SetFigTitle('Tf:Pf 14 degrees', 15)
Pf_vs_Tf_14.SetLabelX('Tf', 15)
Pf_vs_Tf_14.SetLabelY('Pf', 15)
Pf_vs_Tf_14.SetSizeTicksX(10)
Pf_vs_Tf_14.Histo_2D() #Draw it
######### Save and show the created figure
Pf_vs_Tf_14.SetOutDir(basepath + 'Modules/DCs_X_Y_Theta_Phi_FP/Outputfiles/Figures/')
Pf_vs_Tf_14.SaveFig('Pf_vs_Tf_14')
Pf_vs_Tf_14.Show(1) #show during 1 seconds, the close authomatically
Pf_vs_Tf_14.Close() #close all windows, axes and figures running backend
del Pf_vs_Tf_14 #erase Pf_vs_Tf_14 (is an object)



################################################################# 21 degrees
Yf_vs_Xf_21 = Plotter([data_21_degrees['Xf'][condition_21], data_21_degrees['Yf'][condition_21]]) #Create the base with the variables in a Histo2D_object
Yf_vs_Xf_21.SetFigSize(10,7)
Yf_vs_Xf_21.SetBinX(500)
Yf_vs_Xf_21.SetBinY(500)
Yf_vs_Xf_21.SetFigTitle('Xf:Yf 21 degrees', 15)
Yf_vs_Xf_21.SetLabelX('Xf', 15)
Yf_vs_Xf_21.SetLabelY('Yf', 15)
Yf_vs_Xf_21.SetSizeTicksX(10)
Yf_vs_Xf_21.Histo_2D() #Draw it
######### Save and show the created figure
Yf_vs_Xf_21.SetOutDir(basepath + 'Modules/DCs_X_Y_Theta_Phi_FP/Outputfiles/Figures/')
Yf_vs_Xf_21.SaveFig('Yf_vs_Xf_21')
Yf_vs_Xf_21.Show(1) #show during 1 seconds, the close authomatically
Yf_vs_Xf_21.Close() #close all windows, axes and figures running backend
del Yf_vs_Xf_21 #erase Yf_vs_Xf_21 (is an object)


Pf_vs_Tf_21 = Plotter([data_21_degrees['Tf'][condition_21], data_21_degrees['Pf'][condition_21]]) #Create the base with the variables in a object
Pf_vs_Tf_21.SetFigSize(10,7)
Pf_vs_Tf_21.SetBinX(500)
Pf_vs_Tf_21.SetBinY(500)
Pf_vs_Tf_21.SetFigTitle('Tf:Pf 21 degrees', 15)
Pf_vs_Tf_21.SetLabelX('Tf', 15)
Pf_vs_Tf_21.SetLabelY('Pf', 15)
Pf_vs_Tf_21.SetSizeTicksX(10)
Pf_vs_Tf_21.Histo_2D() #Draw it
######### Save and show the created figure
Pf_vs_Tf_21.SetOutDir(basepath + 'Modules/DCs_X_Y_Theta_Phi_FP/Outputfiles/Figures/')
Pf_vs_Tf_21.SaveFig('Pf_vs_Tf_21')
Pf_vs_Tf_21.Show(1) #show during 1 seconds, the close authomatically
Pf_vs_Tf_21.Close() #close all windows, axes and figures running backend
del Pf_vs_Tf_21 #erase Pf_vs_Tf_21 (is an object)



################################################################ 14 + 21 degrees
Yf_vs_Xf_14_21 = Plotter([data_14_21_degrees['Xf'][condition_14_21], data_14_21_degrees['Yf'][condition_14_21]]) #Create the base with the variables in a Histo2D_object
Yf_vs_Xf_14_21.SetFigSize(10,7)
Yf_vs_Xf_14_21.SetBinX(500)
Yf_vs_Xf_14_21.SetBinY(500)
Yf_vs_Xf_14_21.SetFigTitle('Xf:Yf 14+21 degrees', 15)
Yf_vs_Xf_14_21.SetLabelX('Xf', 15)
Yf_vs_Xf_14_21.SetLabelY('Yf', 15)
Yf_vs_Xf_14_21.SetSizeTicksX(10)
Yf_vs_Xf_14_21.Histo_2D() #Draw it
######### Save and show the created figure
Yf_vs_Xf_14_21.SetOutDir(basepath + 'Modules/DCs_X_Y_Theta_Phi_FP/Outputfiles/Figures/')
Yf_vs_Xf_14_21.SaveFig('Yf_vs_Xf_14_21')
Yf_vs_Xf_14_21.Show(1) #show during 1 seconds, the close authomatically
Yf_vs_Xf_14_21.Close() #close all windows, axes and figures running backend
del Yf_vs_Xf_14_21 #erase Yf_vs_Xf_14_21 (is an object)


Pf_vs_Tf_14_21 = Plotter([data_14_21_degrees['Tf'][condition_14_21], data_14_21_degrees['Pf'][condition_14_21]]) #Create the base with the variables in a Histo2D_object
Pf_vs_Tf_14_21.SetFigSize(10,7)
Pf_vs_Tf_14_21.SetBinX(500)
Pf_vs_Tf_14_21.SetBinY(500)
Pf_vs_Tf_14_21.SetFigTitle('Tf:Pf 14+21 degrees', 15)
Pf_vs_Tf_14_21.SetLabelX('Tf', 15)
Pf_vs_Tf_14_21.SetLabelY('Pf', 15)
Pf_vs_Tf_14_21.SetSizeTicksX(10)
Pf_vs_Tf_14_21.Histo_2D() #Draw it
######### Save and show the created figure
Pf_vs_Tf_14_21.SetOutDir(basepath + 'Modules/DCs_X_Y_Theta_Phi_FP/Outputfiles/Figures/')
Pf_vs_Tf_14_21.SaveFig('Pf_vs_Tf_14_21')
Pf_vs_Tf_14_21.Show() #show during 1 seconds, the close authomatically
Pf_vs_Tf_14_21.Close() #close all windows, axes and figures running backend
del Pf_vs_Tf_14_21 #erase Pf_vs_Tf_14_21 (is an object)