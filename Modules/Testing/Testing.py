#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 15:46:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

TESTING MODULE -- A generic Module to test new things and is a template for the others
"""
'''
----------------------------------------------------------------- Protected part ----------------------------------------------------------------------------------------------------------------
'''
import os, sys
sys.path.append('.')
sys.path.append('..')
basepath = os.path.abspath(__file__).rsplit('/Fission_Analysis_VAMOS/',1)[0]+'/Fission_Analysis_VAMOS/'
sys.path.append(basepath)
#print('We are working from here' + os.getcwd())

'''
---------------------------------------------------- Import packages and Framework functions ----------------------------------------------------------------------------------------------------
'''
import numpy as np
import root_numpy as rn
import Framework.read_and_save.read_and_save as RAS


'''
---------------------------------------------- (Option 1) Open and read .hdf5 original file like a hdf5 object ----------------------------------------------------------------------------------
'''
hdf5_folder_path = basepath + 'Data_hdf5/' #The folder with files after the calibrations comming from RootA transformed in hdf5
hdf5_file_name = 'Analysis_TEST_file' #Without .hdf5 extension
Testing_data_hdf5 = RAS.Read_hdf5_file(hdf5_folder_path, hdf5_file_name) #Array-matrix with our data

'''
---------------------------------------------- (Option 2) Open and read .root original file like ndarray object ---------------------------------------------------------------------------------
'''
################################## One can work directly with the root files converting it to ndarray object. This is an example:
#Path_to_tree = '/Users/dani/Dani/FISICA/INVESTIGACION/DOCTORADO/TESIS_NUCLEAR/e753/Analysis_Dani/RootA/'
Tree_name = ['r0092_000a'] #More than one tree is allowed
Branches = 'All' #Or do a selection over concrete braches
Testing_data_ndarray = RAS.Read_Root_file(Path_to_tree, Tree_name, Branches, Tree_selection = None)


'''
----------------------------------------------------------- Do some analysis here ---------------------------------------------------------------------------------------------------------------
'''
################################################# hdf5 object example:
#variable_array = Testing_data_hdf5['Brho'][()]
#Testing_data_hdf5['Brho']['Brho'>75]

################################################ ndarray object example:
#bool_index = Testing_data_ndarray['Brho'] > 1.1
#Testing_data_ndarray_cut = Testing_data_ndarray[bool_index] #selection over all branches

#ThetaLdeg = Testing_data_ndarray['ThetaLdeg']
#ThetaLdeg_index = np.where(ThetaLdeg > 0.0) #obtain the indices for this condition
#ThetaLdeg = ThetaLdeg[ThetaLdeg > 0.0] #cut only one variable
#Brho = Testing_data_ndarray['Brho']
#Brho = Brho[ThetaLdeg_index] #cut another variable


'''
----------------------------------------------------------------- Plot variables ------------------------------------------------------------------------------------------------------------------
'''






'''
------------------------------------------------------------------ Save the data ------------------------------------------------------------------------------------------------------------------
'''

"""#####################################
   ############# hdf5 type #############
   #####################################"""

saved_hdf5_folder_path = basepath + 'Modules/Testing/Outputfiles/'
saved_hdf5_file_name = ['Analysis_SAVED_file']

############################################# Save only some variables
#Group_name = ['ThetaLdeg', 'Brho'] #write the variable names.
#RAS.Save_hdf5_or_ndarray_object_as_hdf5(saved_hdf5_folder_path, saved_hdf5_file_name, Group_name, [Testing_data_hdf5['ThetaLdeg'], Testing_data_hdf5['Brho']])

############################################# Save ALL variables
Group_name = 'All' #write "All" for all the variables.
RAS.Save_hdf5_or_ndarray_object_as_hdf5(saved_hdf5_folder_path, saved_hdf5_file_name, Group_name, Testing_data) #put directly the data array

############################################# Save ALL variables with compression
#Group_name = 'All'
#File_compression = 9 #from 4 to 9 integer numbers to more compression data, increasing the computational time
#RAS.Save_hdf5_or_ndarray_object_as_hdf5(saved_hdf5_folder_path, saved_hdf5_file_name, Group_name, Testing_data, File_compression) #put directly the data array and the compression level

"""#####################################
   ############# root type #############
   #####################################"""

#saved_Root_folder_path = basepath + 'Modules/Testing/Outputfiles/'
#saved_Root_file_name = 'Analysis_SAVED_file.root'
#saved_Root_tree_name = 'DA'

############################################# Save ALL variables like branches in a tree
#RAS.Save_hdf5_or_ndarray_object_as_root(Testing_data_ndarray, saved_Root_folder_path, saved_Root_file_name, saved_Root_tree_name, Tree_mode='recreate')
