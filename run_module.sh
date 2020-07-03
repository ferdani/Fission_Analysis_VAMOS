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
4 --> ToF_correction_in_AoverQ
5 --> ICs_Calibration
'

####################################### Modules Command List ###################################################

#----------------------- 0 - Module - Testing ------------------------------------------------------------------
#python -i Modules/Module_selector.py 'Testing'

#----------------------- 1 - Module - DCs_Calibration ----------------------------------------------------------
#python -i Modules/Module_selector.py 'DCs_Calibration'

#----------------------- 2 - Module - DCs_X_Y_Theta_Phi_FP -----------------------------------------------------
#python Modules/Module_selector.py 'DCs_X_Y_Theta_Phi_FP'

#----------------------- 3 - Module - Charge_states ------------------------------------------------------------
#python Modules/Module_selector.py 'Charge_states'

#----------------------- 4 - Module - ToF_correction_in_AoverQ -------------------------------------------------
#python -i Modules/Module_selector.py 'ToF_correction_in_AoverQ'

#----------------------- 5 - Module - ICs_Calibration ----------------------------------------------------------
python -i Modules/Module_selector.py 'ICs_Calibration'
