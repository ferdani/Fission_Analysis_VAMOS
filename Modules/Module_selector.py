#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:08:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

The Module_selector.py is an easy tool to choose a module in run_module.sh and run it
"""

import os, sys
import argparse
import importlib

basepath = os.path.abspath(__file__).rsplit('/Fission_Analysis_VAMOS/',1)[0]+'/Fission_Analysis_VAMOS/'
sys.path.append(basepath)
print('\n')
print('We are working on: ' + basepath)

'''
------------------------------------- Argparse arguments --------------------------------------
'''

my_parser = argparse.ArgumentParser(description='Gathers parameters to select a module package')

my_parser.add_argument('module', help='Name of the module package: Testing, DCs_Calibration, DCs_X_Y_Theta_Phi_FP, ICs_Calibration', type=str)

args = my_parser.parse_args()

module_name = args.module

if (module_name != 'Testing') and (module_name != 'DCs_Calibration') and (module_name != 'DCs_X_Y_Theta_Phi_FP') and (module_name != 'ICs_Calibration'):
    print('The module does not exist')
    sys.exit()
else:
    print('\n')
    print('Loading module: ' + module_name)
    print('\n')

'''
------------------------------------- Run choosen module ---------------------------------
'''

if module_name == 'Testing':
    #way 1:
    #from .Testing import Testing

    #way 2:
    #importlib.import_module('.Testing','Modules.Testing')

    #way 3:
    #os.system('python ./Modules/Testing/Testing.py') #With this way you are running like an independent script and root_numpy has got problems. Work in progress

    #way 4:
    exec(open('Modules/Testing/Testing.py').read())

if module_name == 'DCs_Calibration':
    exec(open('Modules/DCs_Calibration/DCs_Calibration.py').read())

if module_name == 'DCs_X_Y_Theta_Phi_FP':
    exec(open('Modules/DCs_X_Y_Theta_Phi_FP/DCs_X_Y_Theta_Phi_FP.py').read())

if module_name == 'ICs_Calibration':
    exec(open('Modules/ICs_Calibration/ICs_Calibration.py').read())


print('\n')
print('Exiting Module_selector...')
print('\n')
sys.exit()
