#!/bin/bash
: '
Created on Tue Apr 14 17:30:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

The control area to run an independent module
'

####################################### Modules List ###################################################

#----------------------- 0 - Module - DCs_Calibration --------------------------------------------------
python -i -c 'from Modules import Module_selector' 'DCs_Calibration'
