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
MODULE_name = 'DCs_X_Y_Theta_Phi_FP'

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
#print('We are working from here' + os.getcwd())

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
file_14_degrees = 'Analysis_14_file_DC_variables' #Without .hdf5 extension
file_21_degrees = 'Analysis_21_file_DC_variables' #Without .hdf5 extension
file_14_21_degrees = 'Analysis_14+21_file_DC_variables' #Without .hdf5 extension

data_14_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_14_degrees) #Array-matrix with our data
data_21_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_21_degrees) #Array-matrix with our data
data_14_21_degrees= RAS.Read_hdf5_file(hdf5_folder_path, file_14_21_degrees) #Array-matrix with our data

#Variables aka branches are: ['Pf', 'PhiL', 'Tf', 'ThetaL', 'Xf', 'Yf'] ---> data_14_degrees.keys()

Xf_14 = data_14_degrees['Xf']; Yf_14 = data_14_degrees['Yf'] #mm
Xf_21 = data_21_degrees['Xf']; Yf_21 = data_21_degrees['Yf'] #mm
Xf_14_21 = data_14_21_degrees['Xf']; Yf_14_21 = data_14_21_degrees['Yf'] #mm

Pf_14 = data_14_degrees['Pf']; Tf_14 = data_14_degrees['Tf'] #mrad
Pf_21 = data_21_degrees['Pf']; Tf_21 = data_21_degrees['Tf'] #mrad
Pf_14_21 = data_14_21_degrees['Pf']; Tf_14_21 = data_14_21_degrees['Tf'] #mrad

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
Yf_vs_Xf_14.SetFigTitle('Yf:Xf 14 degrees', 15)
Yf_vs_Xf_14.SetLabelX('Xf [mm]', 15)
Yf_vs_Xf_14.SetLabelY('Yf [mm]', 15)
Yf_vs_Xf_14.SetSizeTicksX(10)
Yf_vs_Xf_14.Histo_2D() #Draw it
######### Save and show the created figure
Yf_vs_Xf_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
Yf_vs_Xf_14.SaveFig('Yf_vs_Xf_14')
Yf_vs_Xf_14.Show(1) #show during 1 seconds, the close authomatically
Yf_vs_Xf_14.Close() #close all windows, axes and figures running backend
del Yf_vs_Xf_14 #erase Yf_vs_Xf_14 (is an object)


Pf_vs_Tf_14_mrad = Plotter([data_14_degrees['Tf'][condition_14], data_14_degrees['Pf'][condition_14]]) #Create the base with the variables in a object
Pf_vs_Tf_14_mrad.SetFigSize(10,7)
Pf_vs_Tf_14_mrad.SetBinX(500)
Pf_vs_Tf_14_mrad.SetBinY(500)
Pf_vs_Tf_14_mrad.SetFigTitle('Pf:Tf 14 degrees', 15)
Pf_vs_Tf_14_mrad.SetLabelX('Tf [mrad]', 15)
Pf_vs_Tf_14_mrad.SetLabelY('Pf [mrad]', 15)
Pf_vs_Tf_14_mrad.SetSizeTicksX(10)
Pf_vs_Tf_14_mrad.Histo_2D() #Draw it
######### Save and show the created figure
Pf_vs_Tf_14_mrad.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
Pf_vs_Tf_14_mrad.SaveFig('Pf_vs_Tf_14_mrad')
Pf_vs_Tf_14_mrad.Show(1) #show during 1 seconds, the close authomatically
Pf_vs_Tf_14_mrad.Close() #close all windows, axes and figures running backend
del Pf_vs_Tf_14_mrad #erase Pf_vs_Tf_14_mrad (is an object)

Pf_vs_Tf_14_deg = Plotter([data_14_degrees['Tf'][condition_14]*180./(1000.*np.pi), data_14_degrees['Pf'][condition_14]*180./(1000.*np.pi)]) #Create the base with the variables in a object
Pf_vs_Tf_14_deg.SetFigSize(10,7)
Pf_vs_Tf_14_deg.SetBinX(500)
Pf_vs_Tf_14_deg.SetBinY(500)
Pf_vs_Tf_14_deg.SetFigTitle('Pf:Tf 14 degrees', 15)
Pf_vs_Tf_14_deg.SetLabelX('Tf [degree]', 15)
Pf_vs_Tf_14_deg.SetLabelY('Pf [degree]', 15)
Pf_vs_Tf_14_deg.SetSizeTicksX(10)
Pf_vs_Tf_14_deg.Histo_2D() #Draw it
######### Save and show the created figure
Pf_vs_Tf_14_deg.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
Pf_vs_Tf_14_deg.SaveFig('Pf_vs_Tf_14_degrees')
Pf_vs_Tf_14_deg.Show(1) #show during 1 seconds, the close authomatically
Pf_vs_Tf_14_deg.Close() #close all windows, axes and figures running backend
del Pf_vs_Tf_14_deg #erase Pf_vs_Tf_14_deg (is an object)


################################################################# 21 degrees
Yf_vs_Xf_21 = Plotter([data_21_degrees['Xf'][condition_21], data_21_degrees['Yf'][condition_21]]) #Create the base with the variables in a Histo2D_object
Yf_vs_Xf_21.SetFigSize(10,7)
Yf_vs_Xf_21.SetBinX(500)
Yf_vs_Xf_21.SetBinY(500)
Yf_vs_Xf_21.SetFigTitle('Yf:Xf 21 degrees', 15)
Yf_vs_Xf_21.SetLabelX('Xf [mm]', 15)
Yf_vs_Xf_21.SetLabelY('Yf [mm]', 15)
Yf_vs_Xf_21.SetSizeTicksX(10)
Yf_vs_Xf_21.Histo_2D() #Draw it
######### Save and show the created figure
Yf_vs_Xf_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
Yf_vs_Xf_21.SaveFig('Yf_vs_Xf_21')
Yf_vs_Xf_21.Show(1) #show during 1 seconds, the close authomatically
Yf_vs_Xf_21.Close() #close all windows, axes and figures running backend
del Yf_vs_Xf_21 #erase Yf_vs_Xf_21 (is an object)


Pf_vs_Tf_21_mrad = Plotter([data_21_degrees['Tf'][condition_21], data_21_degrees['Pf'][condition_21]]) #Create the base with the variables in a object
Pf_vs_Tf_21_mrad.SetFigSize(10,7)
Pf_vs_Tf_21_mrad.SetBinX(500)
Pf_vs_Tf_21_mrad.SetBinY(500)
Pf_vs_Tf_21_mrad.SetFigTitle('Pf:Tf 21 degrees', 15)
Pf_vs_Tf_21_mrad.SetLabelX('Tf [mrad]', 15)
Pf_vs_Tf_21_mrad.SetLabelY('Pf [mrad]', 15)
Pf_vs_Tf_21_mrad.SetSizeTicksX(10)
Pf_vs_Tf_21_mrad.Histo_2D() #Draw it
######### Save and show the created figure
Pf_vs_Tf_21_mrad.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
Pf_vs_Tf_21_mrad.SaveFig('Pf_vs_Tf_21_mrad')
Pf_vs_Tf_21_mrad.Show(1) #show during 1 seconds, the close authomatically
Pf_vs_Tf_21_mrad.Close() #close all windows, axes and figures running backend
del Pf_vs_Tf_21_mrad #erase Pf_vs_Tf_21_mrad (is an object)


Pf_vs_Tf_21_deg = Plotter([data_21_degrees['Tf'][condition_21]*180./(1000.*np.pi), data_21_degrees['Pf'][condition_21]*180./(1000.*np.pi)]) #Create the base with the variables in a object
Pf_vs_Tf_21_deg.SetFigSize(10,7)
Pf_vs_Tf_21_deg.SetBinX(500)
Pf_vs_Tf_21_deg.SetBinY(500)
Pf_vs_Tf_21_deg.SetFigTitle('Pf:Tf 21 degrees', 15)
Pf_vs_Tf_21_deg.SetLabelX('Tf [degree]', 15)
Pf_vs_Tf_21_deg.SetLabelY('Pf [degree]', 15)
Pf_vs_Tf_21_deg.SetSizeTicksX(10)
Pf_vs_Tf_21_deg.Histo_2D() #Draw it
######### Save and show the created figure
Pf_vs_Tf_21_deg.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
Pf_vs_Tf_21_deg.SaveFig('Pf_vs_Tf_21_degree')
Pf_vs_Tf_21_deg.Show(1) #show during 1 seconds, the close authomatically
Pf_vs_Tf_21_deg.Close() #close all windows, axes and figures running backend
del Pf_vs_Tf_21_deg #erase Pf_vs_Tf_21_deg (is an object)


################################################################ 14 + 21 degrees
Yf_vs_Xf_14_21 = Plotter([data_14_21_degrees['Xf'][condition_14_21], data_14_21_degrees['Yf'][condition_14_21]]) #Create the base with the variables in a Histo2D_object
Yf_vs_Xf_14_21.SetFigSize(10,7)
Yf_vs_Xf_14_21.SetBinX(500)
Yf_vs_Xf_14_21.SetBinY(500)
Yf_vs_Xf_14_21.SetFigTitle('Yf:Xf 14+21 degrees', 15)
Yf_vs_Xf_14_21.SetLabelX('Xf [mm]', 15)
Yf_vs_Xf_14_21.SetLabelY('Yf [mm]', 15)
Yf_vs_Xf_14_21.SetSizeTicksX(10)
Yf_vs_Xf_14_21.Histo_2D() #Draw it
######### Save and show the created figure
Yf_vs_Xf_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
Yf_vs_Xf_14_21.SaveFig('Yf_vs_Xf_14_21')
Yf_vs_Xf_14_21.Show(1) #show during 1 seconds, the close authomatically
Yf_vs_Xf_14_21.Close() #close all windows, axes and figures running backend
del Yf_vs_Xf_14_21 #erase Yf_vs_Xf_14_21 (is an object)


Pf_vs_Tf_14_21_mrad = Plotter([data_14_21_degrees['Tf'][condition_14_21], data_14_21_degrees['Pf'][condition_14_21]]) #Create the base with the variables in a Histo2D_object
Pf_vs_Tf_14_21_mrad.SetFigSize(10,7)
Pf_vs_Tf_14_21_mrad.SetBinX(500)
Pf_vs_Tf_14_21_mrad.SetBinY(500)
Pf_vs_Tf_14_21_mrad.SetFigTitle('Pf:Tf 14+21 degrees', 15)
Pf_vs_Tf_14_21_mrad.SetLabelX('Tf [mrad]', 15)
Pf_vs_Tf_14_21_mrad.SetLabelY('Pf [mrad]', 15)
Pf_vs_Tf_14_21_mrad.SetSizeTicksX(10)
Pf_vs_Tf_14_21_mrad.Histo_2D() #Draw it
######### Save and show the created figure
Pf_vs_Tf_14_21_mrad.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
Pf_vs_Tf_14_21_mrad.SaveFig('Pf_vs_Tf_14_21_mrad')
Pf_vs_Tf_14_21_mrad.Show(1) #show during 1 seconds, the close authomatically
Pf_vs_Tf_14_21_mrad.Close() #close all windows, axes and figures running backend
del Pf_vs_Tf_14_21_mrad #erase Pf_vs_Tf_14_21_mrad (is an object)


Pf_vs_Tf_14_21_deg = Plotter([data_14_21_degrees['Tf'][condition_14_21]*180./(1000.*np.pi), data_14_21_degrees['Pf'][condition_14_21]*180./(1000.*np.pi)]) #Create the base with the variables in a Histo2D_object
Pf_vs_Tf_14_21_deg.SetFigSize(10,7)
Pf_vs_Tf_14_21_deg.SetBinX(500)
Pf_vs_Tf_14_21_deg.SetBinY(500)
Pf_vs_Tf_14_21_deg.SetFigTitle('Pf:Tf 14+21 degrees', 15)
Pf_vs_Tf_14_21_deg.SetLabelX('Tf [degree]', 15)
Pf_vs_Tf_14_21_deg.SetLabelY('Pf [degree]', 15)
Pf_vs_Tf_14_21_deg.SetSizeTicksX(10)
Pf_vs_Tf_14_21_deg.Histo_2D() #Draw it
######### Save and show the created figure
Pf_vs_Tf_14_21_deg.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
Pf_vs_Tf_14_21_deg.SaveFig('Pf_vs_Tf_14_21_degree')
Pf_vs_Tf_14_21_deg.Show(1) #show during 1 seconds, the close authomatically
Pf_vs_Tf_14_21_deg.Close() #close all windows, axes and figures running backend
del Pf_vs_Tf_14_21_deg #erase Pf_vs_Tf_14_21_deg (is an object)
