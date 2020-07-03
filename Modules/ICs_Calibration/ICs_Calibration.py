#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 12:13:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

ICs_Calibration MODULE -- The Ionization Chambers Calibration Module

The code generates:
-- Outputfiles/Figures/

"""
MODULE_name = 'ICs_Calibration'

'''
----------------------------------------------------------------- Protected part ----------------------------------------------------------------------------------------------------------------
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
file_14_degrees = 'Analysis_14_file_ICs_Calibration_variables' #Without .hdf5 extension
file_21_degrees = 'Analysis_21_file_ICs_Calibration_variables' #Without .hdf5 extension
file_14_21_degrees = 'Analysis_14+21_file_ICs_Calibration_variables' #Without .hdf5 extension

data_14_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_14_degrees) #Array-matrix with our data
data_21_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_21_degrees) #Array-matrix with our data
data_14_21_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_14_21_degrees) #Array-matrix with our data
