#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:19:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

In this file there are functions to use in each module to read (.root or .hdf5) as a (ndarray matrix or hdf5 object)
and there are functions to save (hdf5 object or ndarray matrix) as a (.root or .hdf5) file.

Functions list:

-   Read_hdf5_file(Folder_path, File_name)

-   Read_Root_file(Path_to_tree, Tree_name_array, Branches, Tree_selection = None)

-   Save_hdf5_or_ndarray_object_as_hdf5(Folder_path, File_name, Group_name, data_in_matrix, File_compression = None)

-   Save_hdf5_or_ndarray_object_as_root(ndArray, Path_to_save_root, Root_file_name, Tree_name_inside, Tree_mode)

"""
import os, sys
import h5py
import root_numpy as rn

'''
------------------------------------------------- Read .hdf5 file --------------------------------------------------------------------------------------------------
'''

def Read_hdf5_file(Folder_path, File_name):
        """Read a data file saved in hdf5 format like an hdf5 object.

        More information here: https://www.pythonforthelab.com/blog/how-to-use-hdf5-files-in-python/

        Parameters:
        Folder_path -- The complete path to the folder of hdf5 data
        File_name -- The complete name of the data file without .hdf5 extension

        Exceptions:
        None

        Return:
        data_file -- A new matrix of arrays where each array is a variable

        """

        filename = Folder_path + File_name + '.hdf5'
        data_file = h5py.File(filename, 'r') #'r' only for read

        return data_file

'''
------------------------------------------------- Read .root files --------------------------------------------------------------------------------------------------
'''

def Read_Root_file(Path_to_tree, Tree_name_array, Branches, Tree_selection = None):
        """Transform .root file with branches to ndarray (similar as a dictionary).

        Returns an array of arrays where each array will be a branch
        This function use root2array wich is a root_numpy's function.

        Parameters:
        Path_to_tree -- The complete path to the folder of the .root files
        Tree_name_array -- The name of each tree inside the folder without .root extension. Only the names in an array. For example: ['bla1', 'bla2']
        Branches -- The branches can be selected one by one in array. For example: ['Brho' , 'D']
        Selection -- A prelimanar selection can be apply. For example: 'ThetaLdeg >> 0.0 & D == 0.0'

        Excepctions:
        None

        Return:
        array_data -- A matrix with the name of the branches in arrays related with the data of each initial branch in the original .root file

        """

        path_filename = list(map(lambda s: os.path.join(Path_to_tree, s) + '.root', Tree_name_array)) #The file path
        path_treename = rn.list_trees(path_filename[0]) #The name inside the tree

        print('We are reading this root files:')
        print(Tree_name_array)

        if Branches == 'All':
                Tree_branches = rn.list_branches(path_filename[0]) #Asumption with all the trees have the same name for their branches
                print('All branches are chosen')
        else:
                Tree_branches = Branches
                print('These branches ')
                print(Branches)
                print('are selected')

        if Tree_selection != None:
            print('The pre-selection over trees is ', Tree_selection)
            array_data = rn.root2array(filenames = path_filename, treename = path_treename[0], branches = Tree_branches, selection = Tree_selection)
        else:
            print('No pre-selection applied')
            array_data = rn.root2array(filenames = path_filename, treename = path_treename[0], branches = Tree_branches)

        return array_data

'''
------------------------------------------------- Save in .hdf5 file --------------------------------------------------------------------------------------------------
'''

def Save_hdf5_or_ndarray_object_as_hdf5(Folder_path, File_name, Group_name, data_in_matrix, File_compression = None):
        """Save a data hdf5 object or ndarray data matrix in a hdf5 file.

        More information here: https://www.pythonforthelab.com/blog/how-to-use-hdf5-files-in-python/

        Parameters:
        Folder_path -- The complete path to the folder to save the data on it
        File_name -- The complete name of the data file in array with all variables inside file: example ['A', 'B', 'C'] --> A_B_C.hdf5 or ['Complete_Analysis'] --> Complete_Analysis.hdf5
        Group_name -- Inside each file exists a name to call the column with one data or other: example ['A_cut', 'B_cut2', 'C_cut_v2'] --> A_B_C['A_cut'] = [20.0, 23.0 ...]
                    or all the names into the data using 'All'
        data_in_matrix -- The data separated in arrays [file_data['A'], file_data['B']] or to save all the data use directly "file_data". It works with ndarray format.
                       -- The data like a hdf5 object
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
            try:
                list_names = data_in_matrix.dtype.names #list the names of the ndarray matrix
            except:
                list_names = list(data_in_matrix.keys()) #list the names of a hdf5 object with keys() for labels

            if File_compression != None:
                for i in range(0, len(list_names)):
                    data_file.create_dataset(list_names[i], data=data_in_matrix[list_names[i]], compression="gzip", compression_opts=File_compression)
            else:
                for i in range(0, len(list_names)):
                    data_file.create_dataset(list_names[i], data=data_in_matrix[list_names[i]])

        data_file.close()
        print('\n')
        print('A file was created called: ', Name[:-1] + '.hdf5')
        print('\n')

        return data_file

'''
------------------------------------------------- Save in .root file --------------------------------------------------------------------------------------------------
'''

def Save_hdf5_or_ndarray_object_as_root(ndArray, Path_to_save_root, Root_file_name, Tree_name_inside, Tree_mode):
        """Save a data hdf5 object or ndarray data matrix in a root file.

        Parameters:
        ndArray -- The ndarray that one wants to convert in a .root file
        Path_to_save_root -- The complete path (string) to save the root file with the name of the root file. Ex: 'inputs/raw_root_files_Dani/'
        Root_file_name -- 'r0126_000a.root'
        Tree_name_inside -- The name (string) of the tree that will be inside the root file. Ex: 'DA'
        Tree_mode -- If exist a tree and one wants to add more branches --> Choose the same name for the tree and Tree_mode = 'update'
                  -- If one wants to create or recrate a new tree --> Tree_mode = 'recreate'

        Exceptions:
        None

        Return:
        tree -- A new file with .root extension

        """

        tree = rn.array2root(arr=ndArray, filename=Path_to_save_root + Root_file_name,  treename=Tree_name_inside, mode=Tree_mode)
        print('\n')
        print('A file was created called: ' + Root_file_name)
        print('\n')

        return tree
