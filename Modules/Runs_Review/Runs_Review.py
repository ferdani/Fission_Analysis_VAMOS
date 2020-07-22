#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:42:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

Runs_Review MODULE -- The runs number: 97, 115, 116, 119 and 124 after see eLog and LogBook of e753 experiment are studied

The code generates:

-- Outputfiles/Figures/

"""
MODULE_name = 'Runs_Review'

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

Path_to_tree = basepath + 'Data_hdf5/' + MODULE_name + '_run/'


################################################################################################################################################################################################
################################################################################################################################################################################################
################################################################################################################################################################################################
################################################################################################################################################################################################
################### REVIEW OVER RUNS 97, 116, 115, 119, 124 ###################

'''
--------------------------------------------------------- Open and read .root original file -----------------------------------------------------------------------------------------------------
'''

Tree_name_14 = ['r0097_000a'] #14 degrees run
#Tree_name_21 = ['r0116_000a', 'r0119_000a', 'r0124_000a'] #21 degrees runs
#Tree_name_21 = ['r0115_000a'] #21 degrees runs
#Tree_name_21 = ['r0116_000a'] #21 degrees runs
#Tree_name_21 = ['r0119_000a'] #21 degrees runs
Tree_name_21 = ['r0124_000a'] #21 degrees runs

Branches = ['Pf','Z','Zi','Xf','Yf','M_Q','M','MW_Nr']

data_runs_14 = RAS.Read_Root_file(Path_to_tree, Tree_name_14, Branches, Tree_selection = None)
data_runs_21 = RAS.Read_Root_file(Path_to_tree, Tree_name_21, Branches, Tree_selection = None)

condition_14 = ((data_runs_14['Xf'][:] > -1500) & (data_runs_14['Yf'][:] > -1500)
                    & (data_runs_14['Yf'][:] > -110) & (data_runs_14['Yf'][:] < 50)
                    & (data_runs_14['Pf'][:] > -100) & (data_runs_14['Pf'][:] < 100)
                    & (data_runs_14['M'][:] < 180) & (data_runs_14['M'][:] > 70)
                    & (data_runs_14['M_Q'][:] < 4.0) & (data_runs_14['M_Q'][:] > 2.25)
                    & (data_runs_14['MW_Nr'][:] >= 0) & (data_runs_14['Z'][:] > 0) & (data_runs_14['Zi'][:] > 0))

condition_21 = ((data_runs_21['Xf'][:] > -1500) & (data_runs_21['Yf'][:] > -1500)
                    & (data_runs_21['Yf'][:] > -110) & (data_runs_21['Yf'][:] < 50)
                    & (data_runs_21['Pf'][:] > -100) & (data_runs_21['Pf'][:] < 100)
                    & (data_runs_21['M'][:] < 180) & (data_runs_21['M'][:] > 70)
                    & (data_runs_21['M_Q'][:] < 4.0) & (data_runs_21['M_Q'][:] > 2.25)
                    & (data_runs_21['MW_Nr'][:] >= 0) & (data_runs_21['Z'][:] > 0) & (data_runs_21['Zi'][:] > 0))


data_14 = data_runs_14[condition_14]
data_21 = data_runs_21[condition_21]

############################################# Save ALL variables once cut it
Group_name = 'All' #write "All" for all the variables.
RAS.Save_hdf5_or_ndarray_object_as_hdf5(Path_to_tree, ['data_runs_14'], Group_name, data_14) #put directly the data array
RAS.Save_hdf5_or_ndarray_object_as_hdf5(Path_to_tree, ['data_runs_21'], Group_name, data_21) #put directly the data array

'''
------------------------------------------------------------------------- Analysis ---------------------------------------------------------------------------------------------------------------
'''

################################################ 14 degrees ################################################################
data_hdf5_14 = RAS.Read_hdf5_file(Path_to_tree, 'data_runs_14')


M_vs_M_Q_14 = Plotter([data_hdf5_14['M_Q'],data_hdf5_14['M']]) #Create the base with the variables in a object
M_vs_M_Q_14.SetFigSize(12,7)
M_vs_M_Q_14.SetBinX(50)
M_vs_M_Q_14.SetBinY(50)
M_vs_M_Q_14.SetFigTitle(r'run97 M vs M_Q    14$\degree$', 20)
M_vs_M_Q_14.SetLabelX('M_Q', 20)
M_vs_M_Q_14.SetLabelY('M', 20)
M_vs_M_Q_14.SetSizeTicksX(10)
M_vs_M_Q_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4.0 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0')
M_vs_M_Q_14.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_vs_M_Q_14.SaveFig('M_vs_M_Q_14_run97')
M_vs_M_Q_14.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_14.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_14 #erase M_vs_M_Q_14 (is an object)


################################################ 21 degrees ################################################################
data_hdf5_21 = RAS.Read_hdf5_file(Path_to_tree, 'data_runs_21')


M_vs_M_Q_21 = Plotter([data_hdf5_21['M_Q'],data_hdf5_21['M']]) #Create the base with the variables in a object
M_vs_M_Q_21.SetFigSize(12,7)
M_vs_M_Q_21.SetBinX(500)
M_vs_M_Q_21.SetBinY(500)
M_vs_M_Q_21.SetFigTitle(r'run124    M vs M_Q    21$\degree$', 20)
M_vs_M_Q_21.SetLabelX('M_Q', 20)
M_vs_M_Q_21.SetLabelY('M', 20)
M_vs_M_Q_21.SetSizeTicksX(10)
M_vs_M_Q_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4.0 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0')
M_vs_M_Q_21.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_vs_M_Q_21.SaveFig('M_vs_M_Q_21_run124')
M_vs_M_Q_21.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_21.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_21 #erase M_vs_M_Q_21 (is an object)




################################################################################################################################################################################################
################################################################################################################################################################################################
################################################################################################################################################################################################
################################################################################################################################################################################################
########################## REVIEW OVER RUNS 124 AND 125 BECAUSE IN MyVAna T -= 0.3 only ins this runs ##########################

'''
--------------------------------------------------------- Open and read .root original file -----------------------------------------------------------------------------------------------------
'''

Tree_name_21 = ['r0124_000a', 'r0125_000a'] #21 degrees run

Branches = ['Pf','Z','Zi','Xf','Yf','M_Q','M','MW_Nr','T','D','V','Beta','Gamma','Brho','E','RunN']

data_runs_21 = RAS.Read_Root_file(Path_to_tree, Tree_name_21, Branches, Tree_selection = None)

condition_21 = ((data_runs_21['Xf'][:] > -1500) & (data_runs_21['Yf'][:] > -1500)
                    & (data_runs_21['Yf'][:] > -110) & (data_runs_21['Yf'][:] < 50)
                    & (data_runs_21['Pf'][:] > -100) & (data_runs_21['Pf'][:] < 100)
                    & (data_runs_21['M'][:] < 180) & (data_runs_21['M'][:] > 70)
                    & (data_runs_21['M_Q'][:] < 4.0) & (data_runs_21['M_Q'][:] > 2.25)
                    & (data_runs_21['MW_Nr'][:] >= 0) & (data_runs_21['Z'][:] > 0) & (data_runs_21['Zi'][:] > 0))

data_21 = data_runs_21[condition_21]

############################################# Save ALL variables once cut it
#Group_name = 'All' #write "All" for all the variables.
#RAS.Save_hdf5_or_ndarray_object_as_hdf5(Path_to_tree, ['data_runs_21_124-125'], Group_name, data_21) #put directly the data array

'''
------------------------------------------------------------------------- Analysis ---------------------------------------------------------------------------------------------------------------
'''

################################################ 21 degrees ################################################################
#data_hdf5_21 = h5py.File(Path_to_tree + 'data_runs_21_124-125.hdf5', 'r+')

#[...] --> Means Ellipsing

################################# Original variables:
print('Original variables:')
print('T --> ', data_21['T'][:])
print('V --> ', data_21['V'][:])
print('Beta --> ', data_21['Beta'][:])
print('Gamma --> ', data_21['Gamma'][:])
print('M_Q --> ', data_21['M_Q'][:])
print('M --> ', data_21['M'][:])


M_vs_M_Q_21 = Plotter([data_21['M_Q'],data_21['M']]) #Create the base with the variables in a object
M_vs_M_Q_21.SetFigSize(12,7)
M_vs_M_Q_21.SetBinX(500)
M_vs_M_Q_21.SetBinY(500)
M_vs_M_Q_21.SetFigTitle(r'run124-125 T-=0.3    M vs M_Q    21$\degree$', 20)
M_vs_M_Q_21.SetLabelX('M_Q', 20)
M_vs_M_Q_21.SetLabelY('M', 20)
M_vs_M_Q_21.SetSizeTicksX(10)
M_vs_M_Q_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4.0 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0')
M_vs_M_Q_21.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_vs_M_Q_21.SaveFig('M_vs_M_Q_21_run124-125_T-')
M_vs_M_Q_21.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_21.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_21 #erase M_vs_M_Q_21 (is an object)


################################## New variables correcting T:
data_21['T'][...] = data_21['T'][...] + 0.3
#V = D/T
data_21['V'][...] = data_21['D'][...]/data_21['T'][...]
#Beta = V/29.9792458
data_21['Beta'][...] = data_21['V'][...]/29.9792458
#Gamma = 1/sqrt(1-Beta**2)
data_21['Gamma'][...] = 1.0/(np.sqrt(1 - data_21['Beta'][...]**2))
#M_Q = Brho/(3.105*Beta*Gamma)
data_21['M_Q'][...] = data_21['Brho'][...]/(3.105*data_21['Beta'][...]*data_21['Gamma'][...])
#M = Etotal/([uma]*(gamma-1))
data_21['M'][...] = data_21['E']/(931.494 * (data_21['Gamma'][...] - 1))

print('New variables correcting T += 0.3')
print('T --> ', data_21['T'][:])
print('V --> ', data_21['V'][:])
print('Beta --> ', data_21['Beta'][:])
print('Gamma --> ', data_21['Gamma'][:])
print('M_Q --> ', data_21['M_Q'][:])
print('M --> ', data_21['M'][:])

M_vs_M_Q_21 = Plotter([data_21['M_Q'],data_21['M']]) #Create the base with the variables in a object
M_vs_M_Q_21.SetFigSize(12,7)
M_vs_M_Q_21.SetBinX(500)
M_vs_M_Q_21.SetBinY(500)
M_vs_M_Q_21.SetFigTitle(r'run124-125 T+=0.3    M vs M_Q    21$\degree$', 20)
M_vs_M_Q_21.SetLabelX('M_Q', 20)
M_vs_M_Q_21.SetLabelY('M', 20)
M_vs_M_Q_21.SetSizeTicksX(10)
M_vs_M_Q_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4.0 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0')
M_vs_M_Q_21.Histo_2D() #Draw it
######### Save and show the created figure
M_vs_M_Q_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_vs_M_Q_21.SaveFig('M_vs_M_Q_21_run124-125_T+')
M_vs_M_Q_21.Show(1) #show during 1 seconds, the close authomatically
M_vs_M_Q_21.Close() #close all windows, axes and figures running backend
del M_vs_M_Q_21 #erase M_vs_M_Q_21 (is an object)


'''
---------------------------------------------- Save data with the branchs corrected ---------------------------------------------------
'''

######################### In .hdf5
saved_hdf5_folder_path = basepath + 'Modules/' + MODULE_name + '/Outputfiles/'
saved_hdf5_file_name = ['run_124_125_Tcorrected']
Group_name = 'All' #write "All" for all the variables.
RAS.Save_hdf5_or_ndarray_object_as_hdf5(saved_hdf5_folder_path, saved_hdf5_file_name, Group_name, data_21) #put directly the data array

######################### In independent .root
saved_root_folder_path = basepath + 'Modules/' + MODULE_name + '/Outputfiles/'
saved_root_file_name = 'r0124_000a_Tcorrected.root'
saved_Root_tree_name = 'DA'
r124 = data_21[(data_21['RunN'][:]==124)]
RAS.Save_hdf5_or_ndarray_object_as_root(r124, saved_root_folder_path, saved_root_file_name, saved_Root_tree_name, Tree_mode='recreate')

######################### In independent .root
saved_root_folder_path = basepath + 'Modules/' + MODULE_name + '/Outputfiles/'
saved_root_file_name = 'r0125_000a_Tcorrected.root'
saved_Root_tree_name = 'DA'
r125 = data_21[(data_21['RunN'][:]==125)]
RAS.Save_hdf5_or_ndarray_object_as_root(r125, saved_root_folder_path, saved_root_file_name, saved_Root_tree_name, Tree_mode='recreate')
