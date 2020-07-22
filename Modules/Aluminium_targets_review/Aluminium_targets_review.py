#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:42:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

Aluminium_targets_review MODULE -- The runs of aluminium targets to check if everything is ok

The code generates:

-- Outputfiles/

"""
MODULE_name = 'Aluminium_targets_review'

'''
----------------------------------------------------- Protected part (Don't touch nothing) ------------------------------------------------------------------------------------------------------
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
import h5py

'''
--------------------------------------------------------- Open and read .root original file -----------------------------------------------------------------------------------------------------
'''

Path_to_tree = basepath + 'Data_hdf5/' + MODULE_name + '_run/'

Tree_name = ['r0095_000a', 'r0098_000a', 'r0099_000a', 'r0117_000a', 'r0118_000a', 'r0128_000a'] #Aluminum runs
Branches = ['Pf','Z','Zi','Xf','Yf','M_Q','M','MW_Nr','T','D','V','Beta','Gamma','Brho','E','RunN']

Alu_data_runs = RAS.Read_Root_file(Path_to_tree, Tree_name, Branches, Tree_selection = None)

condition_14 = ((Alu_data_runs['Xf'][:] > -1500) & (Alu_data_runs['Yf'][:] > -1500)
                    & (Alu_data_runs['Yf'][:] > -110) & (Alu_data_runs['Yf'][:] < 50)
                    & (Alu_data_runs['Pf'][:] > -100) & (Alu_data_runs['Pf'][:] < 100)
                    & (Alu_data_runs['M'][:] < 180) & (Alu_data_runs['M'][:] > 70)
                    & (Alu_data_runs['M_Q'][:] < 4.0) & (Alu_data_runs['M_Q'][:] > 2.25)
                    & (Alu_data_runs['MW_Nr'][:] >= 0))


Alu_data = Alu_data_runs[condition_14]

'''
------------------------------------------------------------------------- Analysis ---------------------------------------------------------------------------------------------------------------
'''


############################ Quiting conditions in MyVAna --> looking for original one

for count in range(0,len(Alu_data['MW_Nr'])):
    if (Alu_data['RunN'][count] >= 90.) or (Alu_data['RunN'][count] <= 99.):
        T_Al_Offset = [0,0,0,0,0.13,0.11,0.051,0.10,0.061,0.062,0.011,0.000145,0.09,0,0.046,0,0.0026,0,0,0]
        Alu_data['T'][..., count] = Alu_data['T'][..., count] - T_Al_Offset[int(Alu_data['MW_Nr'][count])]
    elif (Alu_data['RunN'][count] >= 115.) or (Alu_data['RunN'][count] <= 118.):
        T_Al_Offset = [0,0,0,0,0,-0.3724,-0.2909,-0.2143,-0.2822,-0.2798,-0.2773,-0.3435,-0.1363,-0.3383,-0.3361,-0.3338,-0.1986,-0.3281,0,0]
        Alu_data['T'][..., count] = Alu_data['T'][..., count] - T_Al_Offset[int(Alu_data['MW_Nr'][count])]
    elif (Alu_data['RunN'][count] == 128.):
        T_Al_Offset = [0,0,0,0,0,0,0,0,-0.2893,-0.1433,-0.3577,-0.2844,-0.2127,-0.4243,-0.2112,0,0,0,0,0]
        Alu_data['T'][..., count] = Alu_data['T'][..., count] - T_Al_Offset[int(Alu_data['MW_Nr'][count])]
    if count%100000==0:
        print('Counts analysed: ', round(count/len(Alu_data['MW_Nr']) * 100, 2), '%')


################################## New variables correcting T:
#V = D/T
Alu_data['V'][...] = Alu_data['D'][...]/Alu_data['T'][...]
#Beta = V/29.9792458
Alu_data['Beta'][...] = Alu_data['V'][...]/29.9792458
#Gamma = 1/sqrt(1-Beta**2)
Alu_data['Gamma'][...] = 1.0/(np.sqrt(1 - Alu_data['Beta'][...]**2))
#M_Q = Brho/(3.105*Beta*Gamma)
Alu_data['M_Q'][...] = Alu_data['Brho'][...]/(3.105*Alu_data['Beta'][...]*Alu_data['Gamma'][...])
#M = Etotal/([uma]*(gamma-1))
Alu_data['M'][...] = Alu_data['E']/(931.494 * (Alu_data['Gamma'][...] - 1))


'''
------- Saving ------
'''

######################### In .hdf5
saved_hdf5_folder_path = basepath + 'Modules/' + MODULE_name + '/Outputfiles/'
saved_hdf5_file_name = ['Al_runs-95-98-99-117-118-128']
Group_name = 'All' #write "All" for all the variables.
RAS.Save_hdf5_or_ndarray_object_as_hdf5(saved_hdf5_folder_path, saved_hdf5_file_name, Group_name, Alu_data) #put directly the data array


######################### In independent .root
saved_root_folder_path = basepath + 'Modules/' + MODULE_name + '/Outputfiles/'
saved_root_file_name = 'r095_000a_Tcorrected.root'
saved_Root_tree_name = 'DA'
r95 = Alu_data[(Alu_data['RunN'][:]==95)]
RAS.Save_hdf5_or_ndarray_object_as_root(r95, saved_root_folder_path, saved_root_file_name, saved_Root_tree_name, Tree_mode='recreate')
del r95

######################### In independent .root
saved_root_folder_path = basepath + 'Modules/' + MODULE_name + '/Outputfiles/'
saved_root_file_name = 'r098_000a_Tcorrected.root'
saved_Root_tree_name = 'DA'
r98 = Alu_data[(Alu_data['RunN'][:]==98)]
RAS.Save_hdf5_or_ndarray_object_as_root(r98, saved_root_folder_path, saved_root_file_name, saved_Root_tree_name, Tree_mode='recreate')
del r98

######################### In independent .root
saved_root_folder_path = basepath + 'Modules/' + MODULE_name + '/Outputfiles/'
saved_root_file_name = 'r099_000a_Tcorrected.root'
saved_Root_tree_name = 'DA'
r99 = Alu_data[(Alu_data['RunN'][:]==99)]
RAS.Save_hdf5_or_ndarray_object_as_root(r99, saved_root_folder_path, saved_root_file_name, saved_Root_tree_name, Tree_mode='recreate')
del r99

######################### In independent .root
saved_root_folder_path = basepath + 'Modules/' + MODULE_name + '/Outputfiles/'
saved_root_file_name = 'r0117_000a_Tcorrected.root'
saved_Root_tree_name = 'DA'
r117 = Alu_data[(Alu_data['RunN'][:]==117)]
RAS.Save_hdf5_or_ndarray_object_as_root(r117, saved_root_folder_path, saved_root_file_name, saved_Root_tree_name, Tree_mode='recreate')
del r117

######################### In independent .root
saved_root_folder_path = basepath + 'Modules/' + MODULE_name + '/Outputfiles/'
saved_root_file_name = 'r0118_000a_Tcorrected.root'
saved_Root_tree_name = 'DA'
r118 = Alu_data[(Alu_data['RunN'][:]==118)]
RAS.Save_hdf5_or_ndarray_object_as_root(r118, saved_root_folder_path, saved_root_file_name, saved_Root_tree_name, Tree_mode='recreate')
del r118

######################### In independent .root
saved_root_folder_path = basepath + 'Modules/' + MODULE_name + '/Outputfiles/'
saved_root_file_name = 'r0128_000a_Tcorrected.root'
saved_Root_tree_name = 'DA'
r128 = Alu_data[(Alu_data['RunN'][:]==128)]
RAS.Save_hdf5_or_ndarray_object_as_root(r128, saved_root_folder_path, saved_root_file_name, saved_Root_tree_name, Tree_mode='recreate')
del r128
