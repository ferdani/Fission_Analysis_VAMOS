#!/bin/bash
: '
Created on Tue Apr 14 17:30:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

From here one can run the converter_root2hdf5.py to converts root in hdf5 files located in Data_hdf5 folder
'

####################################### Command List ###################################################
#python -c 'import converter_root2hdf5' -s 'TEST' -n 'Analysis_TEST_file'
#python -i -c 'import converter_root2hdf5' -s 'TEST' -n 'Analysis_TEST_file' -p 'Z > 0.0 && Zi > 0.0 && TP_ThetaL > -1500.0 && Gamma > 0.0 && Brho > 0.0 && Beta > 0.0 && E > 0.0 && dE > 0.0 && Xf > -1500.0 && Yf > -1500.0 && M > 0.0 && M_Q > 0.0 && Mr > 0.0 && Q > 0.0 && Qi > 0.0 && TP_PhiL > -1500.0 && Delta > 0.0 && V > 0.0'
#python -i -c 'import converter_root2hdf5' -s 'TEST' -n 'Analysis_TEST_file' -b 'Z,Zi,Q,Qi,M,Mr,M_Q,E,dE,V,Gamma,Beta,Brho,Xf,Yf,Delta,TP_PhiL,TP_ThetaL'
#python -i -c 'import converter_root2hdf5' -s 'TEST' -n 'Analysis_TEST_file' -b 'Z,Zi,Q,Qi,M,Mr,M_Q,E,dE,V,Gamma,Beta,Brho,Xf,Yf,Delta,TP_PhiL,TP_ThetaL' -p 'Z > 0.0 && Zi > 0.0 && TP_ThetaL > -1500.0 && Gamma > 0.0 && Brho > 0.0 && Beta > 0.0 && E > 0.0 && dE > 0.0 && Xf > -1500.0 && Yf > -1500.0 && M > 0.0 && M_Q > 0.0 && Mr > 0.0 && Q > 0.0 && Qi > 0.0 && TP_PhiL > -1500.0 && Delta > 0.0 && V > 0.0'

###################################### Files for DCs_X_Y_Theta_Phi_FP MODULE ###########################
#python -c 'import converter_root2hdf5' -s '14' -n 'Analysis_14_file_DC_variables' -p 'Z > 0.0 && Zi > 0.0 && M > 0.0' -b 'Xf,Yf,Tf,Pf,PhiL,ThetaL'
#python -c 'import converter_root2hdf5' -s '21' -n 'Analysis_21_file_DC_variables' -p 'Z > 0.0 && Zi > 0.0 && M > 0.0' -b 'Xf,Yf,Tf,Pf,PhiL,ThetaL'
#python -c 'import converter_root2hdf5' -s '14+21' -n 'Analysis_14+21_file_DC_variables' -p 'Z > 0.0 && Zi > 0.0 && M > 0.0' -b 'Xf,Yf,Tf,Pf,PhiL,ThetaL'

###################################### Files for Charge_states MODULE ###########################
#python -c 'import converter_root2hdf5' -s '14' -n 'Analysis_14_file_ChargeStates_variables' -p 'Z > 0.0 && Zi > 0.0 && M > 0.0' -b 'Z,Zi,M,M_Q,Mri,Mr,Q,Qi,Xf,Yf,Tf,Pf'
#python -c 'import converter_root2hdf5' -s '21' -n 'Analysis_21_file_ChargeStates_variables' -p 'Z > 0.0 && Zi > 0.0 && M > 0.0' -b 'Z,Zi,M,M_Q,Mri,Mr,Q,Qi,Xf,Yf,Tf,Pf'
#python -c 'import converter_root2hdf5' -s '14+21' -n 'Analysis_14+21_file_ChargeStates_variables' -p 'Z > 0.0 && Zi > 0.0 && M > 0.0' -b 'Z,Zi,M,M_Q,Mri,Mr,Q,Qi,Xf,Yf,Tf,Pf'

###################################### Files for ToF_correction_in_AoverQ MODULE ###########################
#python -c 'import converter_root2hdf5' -s '14' -n 'Analysis_14_file_ToF_correction_in_AoverQ_variables' -p 'Z > 0.0 && Zi > 0.0 && M > 0.0' -b 'Z,Zi,M,M_Q,Mri,Mr,Q,Qi,Xf,Yf,Tf,Pf,MW_Nr,Brho,T,D'
#python -c 'import converter_root2hdf5' -s '21' -n 'Analysis_21_file_ToF_correction_in_AoverQ_variables' -p 'Z > 0.0 && Zi > 0.0 && M > 0.0' -b 'Z,Zi,M,M_Q,Mri,Mr,Q,Qi,Xf,Yf,Tf,Pf,MW_Nr,Brho,T,D'
#python -c 'import converter_root2hdf5' -s '14+21' -n 'Analysis_14+21_file_ToF_correction_in_AoverQ_variables' -p 'Z > 0.0 && Zi > 0.0 && M > 0.0' -b 'Z,Zi,M,M_Q,Mri,Mr,Q,Qi,Xf,Yf,Tf,Pf,MW_Nr,Brho,T,D'

###################################### Files for ICs_Calibration MODULE ###########################
python -c 'import converter_root2hdf5' -s '14' -n 'Analysis_14_file_ICs_Calibration_variables' -p 'Z > 0.0 && Zi > 0.0 && M > 0.0' -b 'ICE,ICdE0,ICdE1,ICdE2,ICdE3,ICdE4,ICdE5,E_0,dE_0,E_1,dE_1,E_2,dE_2,E_3,dE_3,E_4,dE_4,ICdE,ICdEM1,IcdE,IcEres,IcEtot,IcdE_bragg,IcEres_bragg,E,dE'
python -c 'import converter_root2hdf5' -s '21' -n 'Analysis_21_file_ICs_Calibration_variables' -p 'Z > 0.0 && Zi > 0.0 && M > 0.0' -b 'ICE,ICdE0,ICdE1,ICdE2,ICdE3,ICdE4,ICdE5,E_0,dE_0,E_1,dE_1,E_2,dE_2,E_3,dE_3,E_4,dE_4,ICdE,ICdEM1,IcdE,IcEres,IcEtot,IcdE_bragg,IcEres_bragg,E,dE'
python -c 'import converter_root2hdf5' -s '14+21' -n 'Analysis_14+21_file_ICs_Calibration_variables' -p 'Z > 0.0 && Zi > 0.0 && M > 0.0' -b 'ICE,ICdE0,ICdE1,ICdE2,ICdE3,ICdE4,ICdE5,E_0,dE_0,E_1,dE_1,E_2,dE_2,E_3,dE_3,E_4,dE_4,ICdE,ICdEM1,IcdE,IcEres,IcEtot,IcdE_bragg,IcEres_bragg,E,dE'
