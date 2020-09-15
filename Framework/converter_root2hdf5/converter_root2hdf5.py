#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:11:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

This code converts root files, after the calibration located in RootA, in hdf5 files.
"""
import numpy as np
import root_numpy as rn
import converter_root2hdf5_functions as Cfun
import os, sys
import argparse

basepath = os.path.abspath(__file__).rsplit('/Fission_Analysis_VAMOS/',1)[0]+'/Fission_Analysis_VAMOS/'
sys.path.append(basepath)
print('\n')
print('We are working on: ' + basepath)
print('\n')

'''
------------------------------------------------------- Argparse arguments --------------------------------------------------------------------------------------------
'''

my_parser = argparse.ArgumentParser(description='Gathers parameters to root_to_py_to_root')

my_parser.add_argument('-s', '--samples', help='Name of the samples to do analysis. Ex: PRUEBA, 14, 21', type=str)
my_parser.add_argument('-b', '--branches', default=None, help='Name of each branch one wants from .root file by default All. Ex: Z,Q,Qi', type=str)
my_parser.add_argument('-p', '--preselection', default=None, help='Complete pre-selection over the root files. Ex: Z > 0.0 && Q == 2.0', type=str)
my_parser.add_argument('-n', '--filename', default='', help='Add a file name to hdf5 data', type=str)
my_parser.add_argument('-c', '--compression', default=None, help='You can compress the file in the saved from 4 to 9 increasing the compression. By default: 4', type=int)

args = my_parser.parse_args()

samples = args.samples
branches = args.branches
preselection = args.preselection
filename = args.filename
compression = args.compression

'''
------------------------------------- Load data .root , select the branches , do selection , converts tree -> hdf5 ----------------------------------------------------
'''

"""Select the root files"""
Path_to_calibrated_trees = '/Users/dani/Dani/FISICA/INVESTIGACION/DOCTORADO/TESIS_NUCLEAR/e753/Analysis_Dani/RootA/'

if os.path.isdir(Path_to_calibrated_trees) != True:
    print('The path is wrong!')
    sys.exit()
else:
    print('The calibrated root files comes from: ' + Path_to_calibrated_trees)

print('\n')
print('Loading the data and doing the selection ...')
print('\n')

""" Select the branches"""
if branches != None:
    Tree_branches = args.branches.split(',') #prepare a list of branches separated by ,
else:
    Tree_branches = 'All' #take all the branches by default

"""The name of each root file in an array, 14 degrees and 21 degrees collections (without .root extension)"""
if samples == 'TEST':
    samples_names = ['r0092_000a']
if samples == '14':
    samples_names = ['r0095_000a', 'r0098_000a', 'r0099_000a', 'r0101_000a', 'r0102_000a', 'r0105_000a',
                    'r0106_000a', 'r0107_000a', 'r0108_000a', 'r0109_000a', 'r0110_000a']
if samples == '21':
    samples_names = ['r0116_000a', 'r0117_000a', 'r0118_000a', 'r0119_000a', 'r0121_000a','r0122_000a',
                    'r0123_000a', 'r0124_000a', 'r0125_000a','r0126_000a', 'r0127_000a','r0128_000a', 'r0130_000a']
if (samples == 'All_Trees') or (samples == '14+21') or (samples == '14 + 21'):
    samples_names = ['r0095_000a', 'r0098_000a', 'r0099_000a', 'r0101_000a', 'r0102_000a', 'r0105_000a',
                    'r0106_000a', 'r0107_000a', 'r0108_000a', 'r0109_000a', 'r0110_000a', 'r0116_000a',
                    'r0117_000a', 'r0118_000a', 'r0119_000a', 'r0121_000a','r0122_000a', 'r0123_000a',
                    'r0124_000a', 'r0125_000a','r0126_000a', 'r0127_000a','r0128_000a', 'r0130_000a']

########## Light targets 14 degrees ###############
if samples == 'Al_14':
    samples_names = ['r0095_000a', 'r0098_000a', 'r0099_000a']
if samples == 'Mg_14':
    samples_names = ['r0101_000a', 'r0102_000a']
if samples == 'B_14':
    samples_names = ['r0105_000a']
if samples == 'Be_14':
    samples_names = ['r0106_000a']
if samples == 'Be+Ag_14':
    samples_names = ['r0107_000a', 'r0108_000a', 'r0109_000a', 'r0110_000a']

########## Light targets 21 degrees ###############
if samples == 'Al_21':
    samples_names = ['r0116_000a', 'r0117_000a', 'r0118_000a', 'r0128_000a']
if samples == 'Mg_21':
    samples_names = ['r0119_000a', 'r0121_000a', 'r0122_000a', 'r0130_000a']
if samples == 'B_21':
    samples_names = ['r0123_000a']
if samples == 'Be_21':
    samples_names = ['r0124_000a', 'r0125_000a']
if samples == 'Be+Ag_21':
    samples_names = ['r0126_000a', 'r0127_000a']

########## Light targets 14+21 degrees ###############
if samples == 'Al':
    samples_names = ['r0095_000a', 'r0098_000a', 'r0099_000a', 'r0116_000a', 'r0117_000a', 'r0118_000a', 'r0128_000a']
if samples == 'Mg':
    samples_names = ['r0101_000a', 'r0102_000a', 'r0119_000a', 'r0121_000a', 'r0122_000a', 'r0130_000a']
if samples == 'B':
    samples_names = ['r0105_000a', 'r0123_000a']
if samples == 'Be':
    samples_names = ['r0106_000a', 'r0124_000a', 'r0125_000a']
if samples == 'Be+Ag':
    samples_names = ['r0107_000a', 'r0108_000a', 'r0109_000a', 'r0110_000a', 'r0126_000a', 'r0127_000a']


Tree_name_inside = 'AD' #The name of the tree inside the root file

"""Create the file_data tree-root to python arrays"""
file_data = Cfun.Branches_to_Arrays(Path_to_calibrated_trees, samples_names, Tree_name_inside, Tree_branches, preselection)


'''
------------------------------------ Save the file_data in extension hdf5 in a file ---------------------------------------------------------------------------------
'''
Folder_path = basepath + 'Data_hdf5/'

File_name = [filename]
Group_name = 'All' #write all the names, one per variable.
Cfun.Save_array_matrix_data_to_HDF5(Folder_path, File_name, Group_name, file_data, compression) #put directly the data array and the compression level

print('\n')
print('The file is in: ' + Folder_path)
print('\n')
