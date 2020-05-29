#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:40:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

Charge_states MODULE -- The Charge States module (A/q), (Ameasured) and (Areconstructed)

The code generates:
-- Outputfiles/Figures/

"""
'''
----------------------------------------------------------------- Protected part ----------------------------------------------------------------------------------------------------------------
'''
import os, sys
sys.path.append('.')
sys.path.append('..')
basepath = os.path.abspath(__file__).rsplit('/Fission_Analysis_VAMOS/',1)[0]+'/Fission_Analysis_VAMOS/'
sys.path.append(basepath)
Module_path = basepath + '/Modules/Charge_states/'
sys.path.append(Module_path)

'''
---------------------------------------------------- Import packages and Framework functions ----------------------------------------------------------------------------------------------------
'''
import numpy as np
import Framework.read_and_save.read_and_save as RAS
from Plotter.Plotter import Plotter
