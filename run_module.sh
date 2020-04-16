#!/bin/bash
: '
Created on Tue Apr 14 17:30:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

The control area to run an independent module:
0 --> Testing
1 --> DCs_Calibration
2 --> Phi_Acceptance
3 --> dE_vs_E
'

####################################### Modules Command List ###################################################
#----------------------- 0 - Module - Testing --------------------------------------------------
python -i -c 'from Modules import Module_selector' 'Testing'

#----------------------- 1 - Module - DCs_Calibration --------------------------------------------------
#python -i -c 'from Modules import Module_selector' 'DCs_Calibration'

#----------------------- 2 - Module - Phi_Acceptance --------------------------------------------------
#python -i -c 'from Modules import Module_selector' 'Phi_Acceptance'

#----------------------- 3 - Module - dE_vs_E --------------------------------------------------
#python -i -c 'from Modules import Module_selector' 'dE_vs_E'
