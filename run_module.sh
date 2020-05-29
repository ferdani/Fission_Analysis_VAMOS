#!/bin/bash
: '
Created on Tue Apr 14 17:30:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

The control area to run an independent module:
0 --> Testing
1 --> DCs_Calibration
2 --> DCs_X_Y_Theta_Phi_FP
3 --> Charge_states
4 --> ICs_Calibration
'

####################################### Modules Command List ###################################################

#----------------------- 0 - Module - Testing --------------------------------------------------
#python -i Modules/Module_selector.py 'Testing'

#----------------------- 1 - Module - DCs_Calibration --------------------------------------------------
#python -i Modules/Module_selector.py 'DCs_Calibration'

#----------------------- 2 - Module - DCs_X_Y_Theta_Phi_FP --------------------------------------------------
#python -i Modules/Module_selector.py 'DCs_X_Y_Theta_Phi_FP'

#----------------------- 3 - Module - Charge_states --------------------------------------------------
python -i Modules/Module_selector.py 'Charge_states'

#----------------------- 4 - Module - ICs_Calibration --------------------------------------------------
#python -i Modules/Module_selector.py 'ICs_Calibration'
