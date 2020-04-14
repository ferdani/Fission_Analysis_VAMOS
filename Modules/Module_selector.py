#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:08:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

The Module_selector.py is an easy tool to choose a module in run_module.sh and run it
"""

import numpy as np
import root_numpy as rn
import os, sys
import argparse

basepath = os.path.abspath(__file__).rsplit('/Fission_Analysis_VAMOS/',1)[0]+'/Fission_Analysis_VAMOS/'
sys.path.append(basepath)

print(basepath)
'''
------------------------------------- Argparse arguments --------------------------------------
'''

my_parser = argparse.ArgumentParser(description='Gathers parameters to select a module package')

my_parser.add_argument('module', help='Name of the module package: DCs_Calibration, Phi_Acceptance, dE_vs_E', type=str)

args = my_parser.parse_args()

module_name = args.module

if (module_name != 'DCs_Calibration') and (module_name != 'Phi_Acceptance') and (module_name != 'dE_vs_E'):
    print('The module does not exist')
    sys.exit()
else:
    print('\n')
    print('Loading module: ' + module_name)
    print('\n')

'''
------------------------------------- Run choosen module ---------------------------------
'''

if module_name == 'DCs_Calibration':
    from . import DCs_Calibration
    print('Importing module DCs_Calibration')

if module_name == 'Phi_Acceptance':
    from . import Phi_Acceptance
    print('Importing module Phi_Acceptance')

if module_name == 'dE_vs_E':
    from . import dE_vs_E
    print('Importing module dE_vs_E')
