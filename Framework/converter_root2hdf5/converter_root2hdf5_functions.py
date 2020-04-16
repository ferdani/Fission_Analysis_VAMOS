#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:14:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

In this file there are auxiliar functions to use in the converter_root2hdf.py

Functions list:

-   Branches_to_Arrays(Path_to_tree, Tree_names, Tree_name_inside, Branches, Tree_selection = None)

-   Save_data_HDF5(Folder_path, File_name, Group_name, data_in_matrix, File_compression = None)

"""

import numpy as np
import root_numpy as rn
import sys, os
import h5py

'''
------------------------------------------------- Read .root files and converts to arrays --------------------------------------------------------------------------------------------------
'''

def Branches_to_Arrays(Path_to_tree, Tree_names, Tree_name_inside, Branches, Tree_selection = None):
        """Transform .root file with branches to array of arrays (similar a dictionary).

        Returns an array of arrays where each array will be a branch
        This function use root2array wich is a root_numpy's function.

        Parameters:
        Path_to_tree -- The complete path to the folder of the .root files
        Tree_names -- The name of each tree inside the folder without .root extension. Only the names in an array. For example: ['bla1', 'bla2']
        Tree_name_inside -- In general, all the root files have equal tree name inside, ex: 'GM', 'AD'
        Branches -- The branches can be selected one by one in array. For example: ['Brho' , 'D'] or 'All' if one wants all the branches
        Selection -- A prelimanar selection can be apply. For example: 'ThetaLdeg >> 0.0 & D == 0.0'

        Excepctions:
        None

        Return:
        array_data -- A matrix with the name of the branches in arrays related with the data of each initial branch in the original .root file

        """
        print('You are working with this samples: ')
        print(str(Tree_names))
        print('\n')
        path_filename = list(map(lambda s: os.path.join(Path_to_tree, s) + '.root', Tree_names)) #The file path
        path_treename = rn.list_trees(path_filename[0]) #The names inside the root file (is an array)
        print('The trees inside are: ', path_treename)
        print('\n')

        if path_treename[0] != Tree_name_inside:
            #by default is taken the first
            print('Wrong tree election!')
            print('\n')

        if Branches == 'All':
                #Tree_branches = rn.list_branches(path_treename[0]) #Asumption with all the trees have the same name for their branches
                Tree_branches = None #by default that means take all in root_numpy
                print('All branches are chosen')
                print('\n')
        else:
                Tree_branches = Branches
                print('This branches ')
                print(Branches)
                print('are selected')
                print('\n')

        if Tree_selection != None:
            print('The pre-selection over trees is ', Tree_selection)
            array_data = rn.root2array(filenames = path_filename, treename = path_treename[0], branches = Tree_branches, selection = Tree_selection)
        else:
            print('No pre-selection applied')
            array_data = rn.root2array(filenames = path_filename, treename = path_treename[0], branches = Tree_branches)

        return array_data

'''
----------------------------- Save array-matrix data in hdf5 format  -----------------------------------------------------------------------------------------------------------------------
'''

def Save_data_HDF5(Folder_path, File_name, Group_name, data_in_matrix, File_compression = None):
        """Save the data in columns in the hdf5 format in a folder.

        More information here: https://www.pythonforthelab.com/blog/how-to-use-hdf5-files-in-python/

        Parameters:
        Folder_path -- The complete path to the folder to save the data on it
        File_name -- The complete name of the data file in array with all variables inside file: example ['A', 'B', 'C'] --> A_B_C.hdf5 or ['Complete_Analysis'] --> Complete_Analysis.hdf5
        Group_name -- Inside each file exists a name to call the column with one data or other: example ['A_cut', 'B_cut2', 'C_cut_v2'] --> A_B_C['A_cut'] = [20.0, 23.0 ...]
                    or all the names into the data using 'All'
        data_in_matrix -- The data separated in arrays [file_data['A'], file_data['B']] or to save all the data use directtly file_data
        File_compression -- For default "None", one can apply a compression over the data. In different levels from 4 to 9. For example: compression = 9 (increasing the computational time)

        Exceptions:
        None

        Return:
        data_file -- A new file with the data saved in the format .hdf5

        """

        # Write data to HDF5
        Name = ''.join(map(lambda n: n + '_', File_name))
        data_file = h5py.File(Folder_path + Name[:-1] + '.hdf5', 'w') #erase the last _ character with [:-1]

        if Group_name != 'All':
            if File_compression != None:
                for i in range(0, len(data_in_matrix)):
                    data_file.create_dataset(Group_name[i], data=data_in_matrix[i], compression="gzip", compression_opts=File_compression)
            else:
                for i in range(0, len(data_in_matrix)):
                    data_file.create_dataset(Group_name[i], data=data_in_matrix[i])
        else:
            list_names = data_in_matrix.dtype.names #list the names of the data_in_matrix
            if File_compression != None:
                for i in range(0, len(list_names)):
                    data_file.create_dataset(list_names[i], data=data_in_matrix[list_names[i]], compression="gzip", compression_opts=File_compression)
            else:
                for i in range(0, len(list_names)):
                    data_file.create_dataset(list_names[i], data=data_in_matrix[list_names[i]])

        data_file.close()
        print('\n')
        print('A file was created called: ', Name[:-1] + '.hdf5')

        return data_file
