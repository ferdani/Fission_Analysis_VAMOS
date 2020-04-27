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

my_parser.add_argument('module', help='Name of the module package: Testing, DCs_Calibration, Phi_Acceptance, dE_vs_E', type=str)

args = my_parser.parse_args()

module_name = args.module

if (module_name != 'Testing') and (module_name != 'DCs_Calibration') and (module_name != 'Phi_Acceptance') and (module_name != 'dE_vs_E'):
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

if module_name == 'Phi_Acceptance':
    exec(open('Modules/Phi_Acceptance/Phi_Acceptance.py').read())

if module_name == 'dE_vs_E':
    exec(open('Modules/dE_vs_E/dE_vs_E.py').read())


print('Exiting Module_selector...')
print('\n')
sys.exit()
