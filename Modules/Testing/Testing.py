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
from Plotter.Plotter import Plotter


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
#Tree_name = ['r0092_000a'] #More than one tree is allowed
#Branches = 'All' #Or do a selection over concrete braches
#Testing_data_ndarray = RAS.Read_Root_file(Path_to_tree, Tree_name, Branches, Tree_selection = None)


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
------------------------------------------------------------- Using "Plotter" Class ---------------------------------------------------------------------------------------------------------------
'''

################################################ Histo_1D() function ##########################################################################################
Histo1D_object = Plotter([Testing_data_hdf5['Brho'][()]]) #Create the base with the variables in a Histo1D_object)

######### Some options
Histo1D_object.SetFigSize(10,7)
Histo1D_object.SetBinX(100)
Histo1D_object.SetFigTitle('Variable 1 histogram 1D', 20)
Histo1D_object.SetLimX((0.0,2.0))
Histo1D_object.SetLabelX('Variable 1', 15)

######### Generate the histogram
Histo1D_object.Histo_1D()

######### Save and show the created figure
Histo1D_object.SetOutDir(basepath + 'Modules/Testing/Outputfiles/Figures/')
Histo1D_object.SaveFig('figure_TEST_Histo1D')
Histo1D_object.Show(1) #show during 1 seconds, then close authomatically. Leave empty for normal plt.show()
Histo1D_object.Close() #close all windows, axes and figures running backend
del Histo1D_object #erase Histo1D_object


################################################ Bar_diagram() function #########################################################################################
Bar_diagram_object = Plotter([['a', 'e', 'i', 'o', 'u'], [4,3,3,4,7]]) #Create the base with (tags, frequency) respectively

######### Some options
Bar_diagram_object.SetFigSize(10,7)
Bar_diagram_object.SetFigTitle('Variable Bar diagram', 20)
Bar_diagram_object.SetLabelX('Variable 1', 15)

######### Generate the bar diagram
Bar_diagram_object.Bar_diagram()

######### Save and show the created figure
Bar_diagram_object.SetOutDir(basepath + 'Modules/Testing/Outputfiles/Figures/')
Bar_diagram_object.SaveFig('figure_TEST_Bar_diagram')
Bar_diagram_object.Show(1) #show during 1 seconds, the close authomatically
Bar_diagram_object.Close() #close all windows, axes and figures running backend
del Bar_diagram_object #erase Bar_diagram_object (is an object)


################################################ Bar_diagram_2D() function #########################################################################################
Bar_d2D_object = Plotter([[1, 2, 3], [20,25,30,35], [234, 345, 238, 287, 320, 340, 347, 285, 240, 230, 290, 330]]) #one variable, another variable, value in each box

######### Some options
Bar_d2D_object.SetFigSize(10,7)
Bar_d2D_object.SetFigTitle('Density plot', 20)
Bar_d2D_object.SetLabelX('Variable 1', 15)
Bar_d2D_object.SetLabelY('Variable 2', 15)

######### Generate the bar diagram
Bar_d2D_object.Bar_diagram_2D()

######### Save and show the created figure
Bar_d2D_object.SetOutDir(basepath + 'Modules/Testing/Outputfiles/Figures/')
Bar_d2D_object.SaveFig('figure_TEST_Bar_diagram_2D')
Bar_d2D_object.Show(1) #show during 3 seconds, the close authomatically
Bar_d2D_object.Close() #close all windows, axes and figures running backend
del Bar_d2D_object #erase Bar_diagram_object (is an object)


################################################ Histo_2D() function #############################################################################################
Histo2D_object = Plotter([Testing_data_hdf5['Brho'][()], Testing_data_hdf5['Brho'][()]]) #Create the base with the variables in a Histo2D_object

######### Some options
Histo2D_object.SetFigSize(10,7)
Histo2D_object.SetBinX(100)
Histo2D_object.SetBinY(100)
Histo2D_object.SetFigTitle('Variable 2 vs Variable 1', 15)
Histo2D_object.SetNticksX(10)
Histo2D_object.SetLabelX('Variable 1', 15)
Histo2D_object.SetLabelY('Variable 2', 15)
Histo2D_object.SetSizeTicksX(10)

######### Generate the histogram, with weights
weights = np.ones(len(Testing_data_hdf5['Brho'][()])) #one weight equal one per (Xi, Yi) pair
Histo2D_object.Histo_2D(weights)

######### Save and show the created figure
Histo2D_object.SetOutDir(basepath + 'Modules/Testing/Outputfiles/Figures/')
Histo2D_object.SaveFig('figure_TEST_Histo2D')
Histo2D_object.Show(1) #show during 1 seconds, the close authomatically
Histo2D_object.Close() #close all windows, axes and figures running backend
del Histo2D_object #erase Histo2D (is an object)


################################################ Histo_2D_mountain() function ######################################################################################
Histo2D_mountain_object = Plotter([Testing_data_hdf5['Brho'][()], Testing_data_hdf5['Brho'][()]]) #Create the base with the variables in a Histo2D_mountain_object

######### Some options
Histo2D_mountain_object.SetFigSize(10,7)
Histo2D_mountain_object.SetBinX(100)
Histo2D_mountain_object.SetBinY(100)
Histo2D_mountain_object.SetFigTitle('Variable 2 vs Variable 1', 15)
Histo2D_mountain_object.SetLabelX('Variable 1', 15)
Histo2D_mountain_object.SetLabelY('Variable 2', 15)

######### Generate the histogram
Histo2D_mountain_object.Histo_2D_mountain()

######### Save and show the created figure
Histo2D_mountain_object.SetOutDir(basepath + 'Modules/Testing/Outputfiles/Figures/')
Histo2D_mountain_object.SaveFig('figure_TEST_Histo2D_mountain')
Histo2D_mountain_object.Show(1) #show during 1 seconds, the close authomatically
Histo2D_mountain_object.Close() #close all windows, axes and figures running backend
del Histo2D_mountain_object #erase Histo2D_mountain (is an object)


################################################ ScatterXYpoints_histograms_X_Y() function ######################################################################################
Scatter_XY_histograms = Plotter([Testing_data_hdf5['Brho'][()], Testing_data_hdf5['Brho'][()]]) #Create the base with the variables in a Scatter_XY_histograms

######### Some options
Scatter_XY_histograms.SetFigSize(10,7)
Scatter_XY_histograms.SetBinX(100)
Scatter_XY_histograms.SetBinY(100)
Scatter_XY_histograms.SetFigTitle('Variable 2 vs Variable 1 and distributions', 15)
Scatter_XY_histograms.SetLabelX('Variable 1', 15)
Scatter_XY_histograms.SetLabelY('Variable 2', 15)

######### Generate the histogram
Scatter_XY_histograms.ScatterXYpoints_histograms_X_Y()

######### Save and show the created figure
Scatter_XY_histograms.SetOutDir(basepath + 'Modules/Testing/Outputfiles/Figures/')
Scatter_XY_histograms.SaveFig('figure_TEST_ScatterXYpoints_histograms_X_Y')
Scatter_XY_histograms.Show(1) #show during 1 seconds, the close authomatically
Scatter_XY_histograms.Close() #close all windows, axes and figures running backend
del Scatter_XY_histograms #erase HScatter_XY_histograms (is an object)


'''
------------------------------------------------------------------ Save the data ------------------------------------------------------------------------------------------------------------------
'''

"""#####################################
   ############# hdf5 type #############
   #####################################"""

#saved_hdf5_folder_path = basepath + 'Modules/Testing/Outputfiles/'
#saved_hdf5_file_name = ['Analysis_SAVED_file']

############################################# Save only some variables
#Group_name = ['ThetaLdeg', 'Brho'] #write the variable names.
#RAS.Save_hdf5_or_ndarray_object_as_hdf5(saved_hdf5_folder_path, saved_hdf5_file_name, Group_name, [Testing_data_hdf5['ThetaLdeg'], Testing_data_hdf5['Brho']])

############################################# Save ALL variables
#Group_name = 'All' #write "All" for all the variables.
#RAS.Save_hdf5_or_ndarray_object_as_hdf5(saved_hdf5_folder_path, saved_hdf5_file_name, Group_name, Testing_data_hdf5) #put directly the data array

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
