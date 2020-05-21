#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:42:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

DCs_Calibration MODULE -- The Drift Chamber Calibration Module

The code generates:
-- Outputfiles/Figures/Raw_figures/         All the plots without any correction. DC_QV[channel] vs DC_QV[60] (60-channel as reference channel is used).
                                            These plots give the parameters a0 a1 making linear fit. These parameters are saved in "parameters_a0a1.txt".

-- Outputfiles/Figures/Corrected_figures/   Is necesary to correct some plots, producing a new figure with new fit with of course new a0 a1 parameters and saving these final parameters in
                                            .cal files inside "Calibration_files" folder.

-- Outputfiles/Calibration_files/           The .cal files to correct DC0.cal, DC1.cal, DC2.cal and DC3.cal, inside "Calibs" to apply over all r.root, are generated here.

-- Outputfiles/Figures/Final_Results/       The final plots to check if the channels in each DC are correct

"""
'''
----------------------------------------------------------------- Protected part ----------------------------------------------------------------------------------------------------------------
'''
import os, sys
sys.path.append('.')
sys.path.append('..')
basepath = os.path.abspath(__file__).rsplit('/Fission_Analysis_VAMOS/',1)[0]+'/Fission_Analysis_VAMOS/'
sys.path.append(basepath)
Module_path = basepath + '/Modules/DCs_Calibration/'
sys.path.append(Module_path)

'''
---------------------------------------------------- Import packages and Framework functions ----------------------------------------------------------------------------------------------------
'''
import numpy as np
import datetime
import Framework.read_and_save.read_and_save as RAS
from Plotter.Plotter import Plotter
from ROOT import TCanvas, TFile, TLegend, TH2F, TF1, gStyle

'''
--------------------------------------------------------- Open and read .root original file -----------------------------------------------------------------------------------------------------
'''
root_folder_path = basepath + 'Data_hdf5/DCs_Calibration_run/' #The folder with files after the calibrations comming from RootA transformed in hdf5.
f = TFile.Open(root_folder_path + 'r0061_000a.root') #The .root file with pulser calibration data. Is "a" because in the experiment the raw data was calibrated.
                                                     #We will use it to generate a new .cal file for each DC to correct and test the initial calibration over .root file.

'''
------------------------------------------------------------------------- Analysis ---------------------------------------------------------------------------------------------------------------
'''
#Tree access
mitree = f.AD
#Turn off all branches
mitree.SetBranchStatus("*", 0)
#Turn on some specific branches
mitree.SetBranchStatus("DC0_QV", 1)
mitree.SetBranchStatus("DC0_QVN", 1)
mitree.SetBranchStatus("DC1_QV", 1)
mitree.SetBranchStatus("DC1_QVN", 1)
mitree.SetBranchStatus("DC2_QV", 1)
mitree.SetBranchStatus("DC2_QVN", 1)
mitree.SetBranchStatus("DC3_QV", 1)
mitree.SetBranchStatus("DC3_QVN", 1)

#######################################################################################################################################################
############### Fit 60-channel (as reference) vs the rest channels for each DC. Extract the fits on Outputfiles/Figures/Raw_figures/ ##################
#######################################################################################################################################################

for j in range(0, 4): #4 Drift Chambers

    # Open a txt file to save the parameters value for each DC:
    myfile = open(Module_path + '/Outputfiles/Calibration_files/' + 'DC' + str(j) + 'NoCorrected.cal', 'w')

    # Create a new canvas, and customize it.
    c1 = TCanvas('c1', 'DC' + str(j) + '_calibration', 400, 100, 1000, 700 )
    c1.SetFillColor(0)
    c1.GetFrame().SetFillColor(21)
    c1.GetFrame().SetBorderSize(6)
    c1.GetFrame().SetBorderMode(-1)

    for i in range(0, 160):
        h_Q60vsQ = TH2F('h_Q60vsQ', 'DC' + str(j) + '_QV[60]:DC' + str(j) + '_QV[' + str(i) + ']', 1000, 0, 3000, 1000, 0, 3000)
        h_Q60vsQ.SetFillColor(42)
        h_Q60vsQ.SetYTitle('DC' + str(j) + '_QV[60]')
        h_Q60vsQ.SetXTitle('DC' + str(j) + '_QV[' + str(i) + ']')
        #h_Q60vsQ.SetStats(1)
        gStyle.SetOptStat(1000000001) #only write the name of the histogram

        mitree.Draw("DC" + str(j) + "_QV[60]:DC" + str(j) + "_QV[" + str(i) + "]>>h_Q60vsQ","","col")
        func = TF1('func', '[0] + [1]*x', 0, 2500)
        fit = h_Q60vsQ.Fit('func', 'SQ') #Q (quit) for turn off the statistics

        p0 = func.GetParameter(0)
        p1 = func.GetParameter(1)

        gStyle.SetOptFit(1) #fit stats
        gStyle.SetStatX(0.96)
        gStyle.SetStatY(0.5)

        c1.Update()
        c1.SaveAs(Module_path + '/Outputfiles/Figures/Raw_figures/DC' + str(j) + '_QV[60]:DC' + str(j) + '_QV[' + str(i) + '].png')

        #The old values of each DCi.cal file (preserved for security)
        if j == 0:
            a0_old = [-1566.70, -390.437, -535.551, -438.883, -481.988, -540.881, -445.376, -426.473, -472.282, -400.903, -459.905, -467.821, -407.577, -434.495, -465.170, -409.004, -425.109,
                        -436.646, -421.710, -389.570, -395.566, -427.529, -442.021, -421.452, -448.372, -413.188, -482.225, -392.057, -396.033, -483.005, -386.542, -365.434, -408.169, -383.857,
                        -439.858, -364.598, -390.653, -404.120, -350.144, -390.192, -380.620, -399.585, -387.237, -369.930, -377.522, -439.632, -350.989, -366.886, -450.600, -439.935, -407.366,
                        -433.674, -392.782, -366.439, -395.112, -395.595, -414.695, -382.915, -413.617, -400.646, -424.376, -386.006, -386.083, -374.952, -556.113, -463.076, -567.185, -550.736,
                        -500.297, -474.551, -437.598, -476.635, -536.926, -485.439, -508.494, -507.102, -465.547, -499.087, -533.458, -553.506, -579.513, -610.064, -499.401, -532.306, -534.349,
                        -585.676, -548.345, -497.001, -504.650, -504.196, -426.115, -601.396, -536.479, -475.036, -529.729, -483.414, -473.999, -473.303, -495.385, -423.232, -526.030, -432.874,
                        -404.198, -427.318, -424.577, -424.856, -402.790, -492.967, -427.706, -420.454, -439.796, -441.225, -424.768, -430.365, -429.845, -419.097, -402.416, -372.376, -397.688,
                        -409.765, -347.082, -360.143, -349.422, -395.044, -397.557, -397.083, -414.555, -479.496, -544.872, -490.845, -442.759, -464.550, -484.646, -472.934, -438.153, -491.039,
                        -435.735, -470.860, -442.666, -461.215, -462.514, -443.259, -433.187, -390.656, -389.697, -411.522, -471.405, -438.647, -450.735, -428.723, -387.133, -395.856, -426.639,
                        -386.281, -413.450, -366.842, -350.679, -247.385, -74.4865, -1387.34]
            a1_old = [0.538861, 0.499220, 0.766733, 0.854336, 0.887407, 0.898585, 0.895778, 0.897530, 0.896703, 0.894912, 0.899244, 0.899670, 0.894926, 0.890571, 0.893464, 0.885255, 0.864081,
                        0.860980, 0.864050, 0.857036, 0.858153, 0.856533, 0.854778, 0.856755, 0.854119, 0.851299, 0.851057, 0.846367, 0.846254, 0.844961, 0.842057, 0.838976, 0.852347, 0.851669,
                        0.854357, 0.850111, 0.850325, 0.845666, 0.846081, 0.845993, 0.843677, 0.842968, 0.841331, 0.840255, 0.840881, 0.838286, 0.837269, 0.835348, 0.845408, 0.843102, 0.845296,
                        0.841758, 0.840176, 0.838230, 0.841699, 0.840168, 0.839765, 0.835465, 0.836093, 0.836101, 0.839654, 0.840503, 0.835251, 0.809175, 0.939050, 0.941689, 0.939745, 0.931902,
                        0.933003, 0.931545, 0.924921, 0.916389, 0.919136, 0.908996, 0.897959, 0.903998, 0.899554, 0.899143, 0.903557, 0.911433, 1.00000, 1.00501, 0.981435, 0.992721, 0.993037,
                        0.993194, 0.987985, 0.974927, 0.971069, 0.965691, 0.966569, 0.973535, 0.963465, 0.960701, 0.964036, 0.960523, 0.868996, 0.824275, 0.799312, 0.779215, 0.772354, 0.761233,
                        0.762059, 0.763625, 0.767189, 0.771062, 0.764780, 0.756590, 0.757514, 0.760988, 0.764312, 0.765064, 0.806127, 0.814420, 0.816398, 0.810896, 0.805283, 0.806888, 0.808205,
                        0.800504, 0.791858, 0.786314, 0.790589, 0.790931, 0.792066, 0.793710, 0.793001, 0.806641, 0.826601, 0.838710, 0.838119, 0.839525, 0.839150, 0.835907, 0.827870, 0.823369,
                        0.820697, 0.823115, 0.821062, 0.815198, 0.812066, 0.812573, 0.815282, 0.813346, 0.821102, 0.823731, 0.830759, 0.832416, 0.832954, 0.831236, 0.835505, 0.833006, 0.824421,
                        0.812950, 0.802740, 0.761287, 0.711106, 0.493662, 0.124911, 1.97244]

        elif j == 1:
            a0_old = [0.00000, -112.520, -316.765, -348.449, -121.201, -383.663, -407.282, -374.023, -435.991, -380.526, -449.580, -441.438, -400.905, -335.731, -387.642, -376.136, -404.728,
                        -441.740, -366.617, -430.971, -414.460, -388.962, -349.147, -387.163, -426.282, -399.290, -370.503, -329.224, -339.386, -374.782, -313.177, -355.801, -385.799, -450.639,
                        -443.277, -430.274, -411.516, -433.145, -429.528, -412.305, -350.692, -419.940, -366.182, -420.287, -433.950, -373.790, -408.703, -391.119, -359.050, -327.243, -369.826,
                        -412.908, -375.209, -337.422, -339.332, -356.206, -415.773, -388.426, -417.749, -399.500, -359.114, -376.032, -318.710, -399.977, -168.131, -190.568, -181.520, -238.385,
                        -236.281, -200.618, -163.981, -195.705, -150.404, -126.907, -222.592, -216.997, -214.970, -201.628, -177.088, -95.1846, -222.715, -196.285, -159.944, -163.758, -227.717,
                        -123.104, -185.487, -203.665, -213.741, -212.645, -218.945, -209.353, -166.010, -170.460, -182.464, -79.5423, -260.556, -289.630, -241.003, -325.695, -242.659, -238.959,
                        -306.223, -264.062, -278.801, -200.735, -230.192, -268.344, -250.170, -229.275, -222.221, -267.469, -266.101, -262.596, -237.068, -278.527, -249.523, -198.696, -243.581,
                        -214.407, -293.713, -252.126, -233.313, -253.054, -180.581, -271.510, -231.693, -599.521, -348.127, -403.452, -377.968, -359.505, -330.368, -328.975, -284.135, -343.459,
                        -335.358, -351.308, -359.712, -416.334, -354.093, -382.307, -313.233, -355.450, -402.250, -355.655, -271.609, -265.423, -303.561, -306.409, -289.097, -333.504, -296.676,
                        -311.892, -284.103, -237.384, -265.992, -219.550, -150.167, -1834.91]
            a1_old = [1.00000, 0.203792, 0.588909, 0.630448, 0.760688, 0.689855, 0.784863, 0.764139, 0.803497, 0.796596, 0.805102, 0.797530, 0.804674, 0.792363, 0.796973, 0.791762, 0.782534,
                        0.785234, 0.781329, 0.776727, 0.776403, 0.774769, 0.772075, 0.774743, 0.772518, 0.772652, 0.769574, 0.769887, 0.770636, 0.766085, 0.767959, 0.775746, 0.770061, 0.771957,
                        0.771847, 0.769785, 0.770238, 0.768485, 0.763140, 0.763588, 0.764248, 0.762150, 0.759683, 0.759416, 0.757735, 0.754005, 0.755643, 0.749059, 0.818997, 0.814050, 0.810777,
                        0.813657, 0.813959, 0.812508, 0.809683, 0.810719, 0.812213, 0.808327, 0.808419, 0.809016, 0.809687, 0.808140, 0.804379, 0.797795, 0.896590, 0.884348, 0.888439, 0.889618,
                        0.884413, 0.875314, 0.873621, 0.873293, 0.874057, 0.870180, 0.878159, 0.870352, 0.871292, 0.871857, 0.866782, 0.859933, 0.878838, 0.869623, 0.865619, 0.868620, 0.873238,
                        0.868221, 0.872586, 0.875511, 0.879261, 0.874663, 0.875519, 0.869455, 0.865657, 0.867737, 0.867413, 0.858134, 0.763695, 0.739734, 0.749218, 0.755322, 0.754937, 0.755229,
                        0.751384, 0.744613, 0.739962, 0.732263, 0.734268, 0.740779, 0.747411, 0.746605, 0.746675, 0.742117, 0.754776, 0.747171, 0.735247, 0.737407, 0.734905, 0.742379, 0.752909,
                        0.746730, 0.747938, 0.755286, 0.759159, 0.751133, 0.746807, 0.729596, 0.688125, 1.58166 , 0.715490, 0.737999, 0.734628, 0.741385, 0.733534, 0.734442, 0.724821, 0.723333,
                        0.715888, 0.723819, 0.724932, 0.728791, 0.731405, 0.735138, 0.727765, 0.727544, 0.772480, 0.771252, 0.759463, 0.746099, 0.755960, 0.751484, 0.746029, 0.738636, 0.747363,
                        0.748826, 0.739224, 0.714858, 0.696362, 0.611333, 0.365178, 0.533562]
        elif j == 2:
            a0_old = [-1579.39, -172.692, -206.789, -185.754, -233.720, -220.204, -253.758, -264.335, -180.604, -164.953, -252.854, -228.248, -239.096, -200.934, -237.996, -174.136, -155.608,
                        -138.212, -132.687, -160.483, -172.642, -153.953, -175.159, -134.541, -162.077, -149.695, -165.597, -150.237, -118.476, -197.234, -156.915, -148.408, -188.434, -146.590,
                        -110.390, -169.586, -163.569, -108.821, -155.951, -140.763, -141.127, -108.017, -153.459, -155.819, -114.559, -176.697, -98.2187, -125.509, -81.8334, -94.8074, -85.7714,
                        -52.3624, -150.642, -131.494, -131.374, -158.036, -94.1193, -144.301, -104.197, -82.7881, -76.3800, -102.726, -141.205, -95.2345, -323.199, -279.365, -242.339, -329.020,
                        -226.526, -311.278, -269.590, -287.667, -275.359, -307.258, -308.228, -216.600, -273.754, -260.580, -300.668, -231.507, -228.837, -184.881, -198.058, -178.476, -268.805,
                        -240.893, -225.230, -214.580, -175.062, -196.834, -224.783, -142.365, -205.343, -192.071, -231.803, -239.495, -557.354, -529.394, -603.297, -473.159, -561.436, -497.368,
                        -523.648, -509.201, -547.328, -541.530, -489.031, -500.098, -473.542, -518.344, -414.267, -385.196, -388.251, -375.996, -424.972, -368.113, -369.186, -332.664, -430.610,
                        -386.192, -349.709, -337.475, -380.902, -405.142, -373.786, -337.354, -339.000, -408.857, -358.606, -313.368, -308.041, -375.034, -311.799, -380.166, -329.690, -390.305,
                        -395.856, -359.881, -364.650, -327.424, -329.519, -341.208, -345.655, -305.233, -461.797, -381.026, -394.071, -359.121, -404.268, -403.985, -387.464, -385.875, -349.382,
                        -267.763, -395.467, -395.357, -340.834, -287.443, -99.9064, 0.00000]
            a1_old = [0.538573, 0.443862, 0.725547, 0.814475, 0.838539, 0.850956, 0.858326, 0.858653, 0.855776, 0.855114, 0.856457, 0.850111, 0.848770, 0.844695, 0.849079, 0.847980, 0.831972,
                        0.828639, 0.830274, 0.828808, 0.829664, 0.829636, 0.828788, 0.825771, 0.827155, 0.823007, 0.822913, 0.815841, 0.815083, 0.815543, 0.811538, 0.812655, 0.847320, 0.850684,
                        0.850972, 0.845940, 0.844180, 0.837772, 0.839428, 0.838040, 0.832384, 0.832801, 0.829358, 0.823714, 0.820657, 0.823313, 0.819450, 0.817555, 0.835544, 0.833962, 0.834331,
                        0.834913, 0.836831, 0.832767, 0.830185, 0.834500, 0.828398, 0.832086, 0.833604, 0.825402, 0.824807, 0.822752, 0.820030, 0.818421, 1.03102, 1.02016, 1.01597, 1.01994,
                        1.01133, 1.01399, 1.00682, 1.00225, 1.00166, 0.993070, 0.993121, 0.982949, 0.985496, 0.979920, 0.980754, 0.971819, 0.983730, 0.988990, 0.984043, 0.982245, 0.981699,
                        0.986748, 0.985033, 0.985213, 0.987215, 0.980815, 0.983406, 0.978764, 0.980119, 0.980687, 0.981462, 0.978775, 0.868504, 0.840367, 0.843933, 0.835990, 0.837794, 0.834219,
                        0.837839, 0.833381, 0.833022, 0.826245, 0.824470, 0.823004, 0.819913, 0.822889, 0.816310, 0.814975, 0.830958, 0.832219, 0.834082, 0.835473, 0.830388, 0.827014, 0.837101,
                        0.831969, 0.829039, 0.830531, 0.835986, 0.835730, 0.829420, 0.825049, 0.825510, 0.825209, 0.838103, 0.845725, 0.838959, 0.842678, 0.837298, 0.840696, 0.833569, 0.833720,
                        0.828955, 0.826080, 0.827067, 0.821491, 0.823048, 0.823591, 0.820216, 0.816070, 0.852320, 0.856173, 0.853343, 0.850127, 0.850661, 0.846721, 0.851117, 0.840890, 0.840340,
                        0.829630, 0.831179, 0.804067, 0.761104, 0.577265, 0.784623, 1.00000]
        elif j == 3:
            a0_old = [0.00000, -148.240, -327.519, -274.980, -562.887, -489.022, -435.075, -463.304, -551.986, -474.507, -529.363, -450.051, -464.649, -445.515, -507.015, -403.313, -443.418,
                        -336.298, -400.542, -358.909, -383.801, -428.093, -412.482, -442.772, -387.532, -378.130, -359.477, -407.428, -342.450, -352.088, -395.594, -287.324, -643.611, -610.423,
                        -634.034, -572.819, -568.033, -553.592, -590.794, -586.257, -562.492, -569.345, -561.489, -608.054, -601.711, -566.534, -539.951, -593.972, -639.995, -576.759, -584.197,
                        -630.973, -603.641, -581.812, -593.934, -560.468, -596.888, -579.088, -589.279, -583.435, -592.247, -574.806, -562.772, -462.717, -643.743, -664.875, -592.531, -587.959,
                        -596.629, -625.661, -569.492, -533.240, -649.249, -550.524, -676.472, -473.417, -485.070, -537.913, -596.095, -569.429, -482.290, -530.597, -563.576, -558.617, -442.007,
                        -511.672, -531.257, -425.209, -505.799, -425.301, -475.797, -483.437, -430.124, -485.869, -497.679, -502.435, -265.336, -368.847, -268.569, -321.941, -258.505, -264.237,
                        -250.076, -260.389, -279.426, -268.763, -238.957, -276.095, -256.561, -252.198, -306.202, -276.973, -317.060, -310.408, -359.764, -242.610, -235.781, -262.993, -271.573,
                        -290.968, -241.766, -226.876, -275.413, -307.694, -259.167, -267.343, -245.495, -262.815, -503.881, -455.517, -459.749, -538.422, -502.888, -460.861, -490.116, -481.853,
                        -486.668, -494.631, -445.523, -558.820, -498.388, -525.703, -464.032, -410.086, -444.043, -508.069, -500.819, -389.445, -455.404, -439.716, -424.430, -451.138, -453.881,
                        -468.856, -428.133, -458.943, -437.888, -346.009, -191.371, -1912.09]
            a1_old = [1.00000, 0.223700, 0.622980, 0.716927, 0.837177, 0.844758, 0.854938, 0.858971, 0.862239, 0.855728, 0.859681, 0.854750, 0.857246, 0.853100, 0.855021, 0.848589, 0.839035,
                        0.838721, 0.831669, 0.834311, 0.829979, 0.827987, 0.830242, 0.828010, 0.824250, 0.819715, 0.818508, 0.819372, 0.815555, 0.815522, 0.818768, 0.810162, 0.831602, 0.838551,
                        0.835698, 0.834662, 0.833660, 0.832181, 0.827764, 0.830299, 0.826622, 0.830185, 0.827583, 0.824190, 0.824656, 0.824534, 0.823373, 0.819561, 0.847129, 0.851480, 0.845973,
                        0.844469, 0.844589, 0.841545, 0.842149, 0.840075, 0.842386, 0.833323, 0.839398, 0.831205, 0.833707, 0.828057, 0.825858, 0.824852, 1.02632, 1.01294, 1.00327, 1.00004,
                        0.998767, 0.996151, 0.990761, 0.984876, 0.984735, 0.977567, 0.981599, 0.968123, 0.966519, 0.969676, 0.968869, 0.976767, 0.984050, 0.983297, 0.978928, 0.980028, 0.973888,
                        0.973319, 0.971171, 0.971459, 0.968590, 0.964627, 0.967961, 0.966691, 0.966162, 0.965124, 0.964984, 0.973118, 0.851843, 0.823057, 0.814652, 0.812090, 0.806306, 0.801086,
                        0.797441, 0.792455, 0.795961, 0.789327, 0.787348, 0.790513, 0.789360, 0.786786, 0.784448, 0.784960, 0.824046, 0.824450, 0.824679, 0.819996, 0.822687, 0.823225, 0.825439,
                        0.824988, 0.820732, 0.820647, 0.821745, 0.827121, 0.820628, 0.821718, 0.822569, 0.821845, 0.815721, 0.822032, 0.821476, 0.818002, 0.815985, 0.815379, 0.814701, 0.811520,
                        0.809932, 0.809296, 0.804862, 0.801208, 0.800439, 0.797380, 0.797441, 0.794243, 0.823538, 0.830571, 0.835108, 0.829390, 0.832448, 0.831059, 0.828258, 0.830714, 0.829166,
                        0.822584, 0.820068, 0.807041, 0.780657, 0.672929, 0.351187, 0.532294]

        #Correction over old values
        a0 = p0 + p1 * a0_old[i]
        a1 = p1 * a1_old[i]

        if i==0:
            myfile.write("// Title   : calibration file for <DC" + str(j) + "><> :\n")
            myfile.write("// Date : " + str(datetime.datetime.now()) + ":\n")
            myfile.write("// Comment :\n")
            myfile.write("// Reference Position X Y (Z+150mm due to the new FPMW)\n")
            myfile.write("-463.00 -80.56 7839.5\n")
            myfile.write("// DriftVelocity cm/us   new DC 23/09/2010 MR\n")
            myfile.write("5.387\n")
            myfile.write("// QThresh\n")
            myfile.write("0.01\n")
            myfile.write("//Energy Wire calib\n")
            myfile.write("0. 1. 0\n")
            myfile.write("//Time Wire calib\n")
            if j==0:
                myfile.write("0. 0.250921 0\n")
            elif j==1:
                myfile.write("0. 0.24323 0\n")
            elif j==2:
                myfile.write("0. 0.25059 0\n")
            elif j==3:
                myfile.write("0. 0.242188 0\n")
            myfile.write("//Charge Strip calib\n")
            myfile.write("// Format  : a0 	 a1 	 a2 	 // ParameterName)\n")
            myfile.write("%f  %f   0.00000 // %i ch %s\n" %(a0, a1, j, str(i)))

        else:
            myfile.write("%f  %f   0.00000 // %i ch %s\n" %(a0, a1, j, str(i)))

        del h_Q60vsQ
        del func
        del fit

    c1.Close()
    myfile.close()
    print('\n')
    print('The file: ' + Module_path + '/Outputfiles/Calibration_files/' + 'DC' + str(j) + 'NoCorrected.cal' + ' was saved\n')

####################################################################################################################################################
########################## Now corrects some fits in specific channels using the plots in Outputfiles/Figures/Raw_figures/ #########################
####################################################################################################################################################

for DCn in range(0, 4):

    # Open NoCorrected .cal file for each  DC
    NoCorrected_file = open(Module_path + '/Outputfiles/Calibration_files/DC' + str(DCn) + 'NoCorrected.cal', 'r')

    # Open .cal file for each  DC
    cal_file = open(Module_path + '/Outputfiles/Calibration_files/' + 'DC' + str(DCn) + '.cal', 'w')

    cal_file.write("// Title   : Corrected calibration file for <DC" + str(DCn) + "><> :\n")
    cal_file.write("// Date : " + str(datetime.datetime.now()) + ":\n")
    cal_file.write("// Comment :\n")
    cal_file.write("// Reference Position X Y (Z+150mm due to the new FPMW)\n")
    cal_file.write("-463.00 -80.56 7839.5\n")
    cal_file.write("// DriftVelocity cm/us   new DC 23/09/2010 MR\n")
    cal_file.write("5.387\n")
    cal_file.write("// QThresh\n")
    cal_file.write("0.01\n")
    cal_file.write("//Energy Wire calib\n")
    cal_file.write("0. 1. 0\n")
    cal_file.write("//Time Wire calib\n")
    if DCn==0:
        cal_file.write("0. 0.250921 0\n")
    elif DCn==1:
        cal_file.write("0. 0.24323 0\n")
    elif DCn==2:
        cal_file.write("0. 0.25059 0\n")
    elif DCn==3:
        cal_file.write("0. 0.242188 0\n")
    cal_file.write("//Charge Strip calib\n")
    cal_file.write("// Format  : a0 	 a1 	 a2 	 // ParameterName\n")

    for line_index, line in enumerate(NoCorrected_file):
        if line_index > 14: #skip the initial 14 lines
            cal_file.write(line)

    cal_file.close()
    NoCorrected_file.close()

    #Channel number to correct it
    if   DCn == 0: Correct_DC = [0, 1, 157, 158, 159] #DC0
    elif DCn == 1: Correct_DC = [0, 1, 2, 3, 4, 157, 158, 159] #DC1
    elif DCn == 2: Correct_DC = [0, 1, 157, 158, 159] #DC2
    elif DCn == 3: Correct_DC = [0, 1, 2, 157, 158, 159] #DC3

    # Create a new canvas, and customize it.
    c2 = TCanvas('c2', 'DC' + str(DCn) + '_calibration_newfit', 400, 100, 1000, 700 )
    c2.SetFillColor(0)
    c2.GetFrame().SetFillColor(21)
    c2.GetFrame().SetBorderSize(6)
    c2.GetFrame().SetBorderMode(-1)

    for number in Correct_DC:

        h_Q60vsQ = TH2F('h_Q60vsQ', 'DC' + str(DCn) + '_QV[60]:DC' + str(DCn) + '_QV[' + str(number) + ']', 1000, 0, 3000, 1000, 0, 3000)
        h_Q60vsQ.SetFillColor(42)
        h_Q60vsQ.SetYTitle('DC' + str(DCn) + '_QV[60]')
        h_Q60vsQ.SetXTitle('DC' + str(DCn) + '_QV[' + str(number) + ']')
        #h_Q60vsQ.SetStats(1)
        gStyle.SetOptStat(1000000001) #only write the name of the histogram

        mitree.Draw("DC" + str(DCn) + "_QV[60]:DC" + str(DCn) + "_QV[" + str(number) + "]>>h_Q60vsQ","","col")
        func = TF1('func', '[0] + [1]*x', 0, 2500)

        #Conditions over each channel and specific DC, where xmin and xmax are the limits of linear fit
        xmin = 0.0 #By default
        if DCn == 0:
            if   number == 0: xmax = 1000
            elif number == 1: xmax = 1700; xmin = 250
            elif number == 157: xmax = 1700
            elif number == 158: xmax = 1200
            elif number == 159: xmax = 2500; xmin = 400
        if DCn == 1:
            if   number == 0: xmax = 150
            elif number == 1: xmax = 1000
            elif number == 2: xmax = 2000
            elif number == 3: xmax = 2300; xmin = 100
            elif number == 4: xmax = 100
            elif number == 157: xmax = 2300
            elif number == 158: xmax = 1500
            elif number == 159: xmax = 0
        if DCn == 2:
            if   number == 0: xmax = 0
            elif number == 1: xmax = 1800; xmin = 100
            elif number == 157: xmax = 1600
            elif number == 158: xmax = 0
            elif number == 159: xmax = 0
        if DCn == 3:
            if   number == 0: xmax = 250
            elif number == 1: xmax = 1400; xmin = 250
            elif number == 2: xmax = 2250; xmin = 250
            elif number == 157: xmax = 2300
            elif number == 158: xmax = 1600
            elif number == 159: xmax = 1100

        fit = h_Q60vsQ.Fit('func', 'SQ', '', xmin, xmax)

        p0 = func.GetParameter(0)
        p1 = func.GetParameter(1)

        gStyle.SetOptFit(1) #draw fit stats
        gStyle.SetStatX(0.96)
        gStyle.SetStatY(0.5)

        c2.Update()
        c2.SaveAs(Module_path + '/Outputfiles/Figures/Corrected_figures/DC' + str(DCn) + '_QV[60]:DC' + str(DCn) + '_QV[' + str(number) + '].png')

        del h_Q60vsQ
        del func
        del fit

        #Open the calibration file to change the new parameters in the specific channels.
        cal_file = open(Module_path + '/Outputfiles/Calibration_files/' + 'DC' + str(DCn) + '.cal', 'r+')
        content = cal_file.readlines() #reads line by line and out puts a list of each line

        #Re-evaluate the parameters with the new values
        data_line = content[number+15].split() #+15 skipping the first lines
        a0_old = float(data_line[0])
        a1_old = float(data_line[1])
        #Correction over old values
        a0 = p0 + p1 * a0_old
        a1 = p1 * a1_old

        content[number+15] = "%f  %f  0.00000 // %i ch %s\n" %(a0, a1, DCn, str(number)) #replaces content

        cal_file.close()
        cal_file = open(Module_path + '/Outputfiles/Calibration_files/' + 'DC' + str(DCn) + '.cal', 'w') #clears content of file.
        cal_file.close()
        cal_file = open(Module_path + '/Outputfiles/Calibration_files/' + 'DC' + str(DCn) + '.cal', 'r+')

        for item in content: #rewrites file content from list
            cal_file.write("%s" % item)
        del content
        cal_file.close()
    print('\n')
    print('The file: ' + Module_path + '/Outputfiles/Calibration_files/' + 'DC' + str(DCn) + '.cal' + ' was saved\n')

    c2.Close()

####################################################################################################################################################
####################### Second order correction. Seeing the results of  (DC2_QV vs DC2_QVN) exist some channels with a hole ########################
####################################################################################################################################################

# Open DC2.cal file to read the last correction
DC2 = open(Module_path + '/Outputfiles/Calibration_files/DC2.cal', 'r')

# Open DC2_new.cal to apply second order correction over some channels
DC2_new = open(Module_path + '/Outputfiles/Calibration_files/DC2_new.cal', 'w')

DC2_new.write("// Title   : Second order calibration file for <DC2><> :\n")
DC2_new.write("// Date : " + str(datetime.datetime.now()) + ":\n")
DC2_new.write("// Comment :\n")
DC2_new.write("// Reference Position X Y (Z+150mm due to the new FPMW)\n")
DC2_new.write("-463.00 -80.56 7839.5\n")
DC2_new.write("// DriftVelocity cm/us   new DC 23/09/2010 MR\n")
DC2_new.write("5.387\n")
DC2_new.write("// QThresh\n")
DC2_new.write("0.01\n")
DC2_new.write("//Energy Wire calib\n")
DC2_new.write("0. 1. 0\n")
DC2_new.write("//Time Wire calib\n")
DC2_new.write("0. 0.25059 0\n")
DC2_new.write("//Charge Strip calib\n")
DC2_new.write("// Format  : a0 	 a1 	 a2 	 // ParameterName\n")

for line_index, line in enumerate(DC2):
    if line_index > 14: #skip the initial 14 lines
        DC2_new.write(line)

DC2_new.close()
DC2.close()

#Channel numbers to apply second order:
Channels_2nd = [140, 141, 142, 143, 144, 145, 146, 147, 148, 149]

# Create a new canvas, and customize it.
c3 = TCanvas('c3', 'DC2_calibration_2nd_order', 400, 100, 1000, 700 )
c3.SetFillColor(0)
c3.GetFrame().SetFillColor(21)
c3.GetFrame().SetBorderSize(6)
c3.GetFrame().SetBorderMode(-1)

for ch in Channels_2nd:
    histo_Q60_vs_ch = TH2F('histo_Q60_vs_ch', 'DC2_QV[60]:DC2_QV[' + str(ch) + ']', 1000, 0, 3000, 1000, 0, 3000)
    histo_Q60_vs_ch.SetFillColor(42)
    histo_Q60_vs_ch.SetYTitle('DC2_QV[60]')
    histo_Q60_vs_ch.SetXTitle('DC2_QV[' + str(ch) + ']')

    gStyle.SetOptStat(1000000001) #only write the name of the histogram

    mitree.Draw("DC2_QV[60]:DC2_QV[" + str(ch) + "]>>histo_Q60_vs_ch","","col")
    func_2nd_order = TF1('func_2nd_order', '[0] + [1]*x + [2]*x**2', 0, 2700)

    #By default
    xmin = 0.0
    xmax = 2700.0

    fit_2nd_order = histo_Q60_vs_ch.Fit('func_2nd_order', 'SQ', '', xmin, xmax)

    p0 = func_2nd_order.GetParameter(0)
    p1 = func_2nd_order.GetParameter(1)
    p2 = func_2nd_order.GetParameter(2)

    gStyle.SetOptFit(1) #draw fit stats
    gStyle.SetStatX(0.96)
    gStyle.SetStatY(0.5)

    c3.Update()
    c3.SaveAs(Module_path + '/Outputfiles/Figures/2nd_order_corrected_figures/' + 'DC2_QV[60]:DC2_QV[' + str(ch) + '].png')

    del histo_Q60_vs_ch
    del func_2nd_order
    del fit_2nd_order

    #Open the calibration file to change the new parameters in the specific channels.
    DC2_new = open(Module_path + '/Outputfiles/Calibration_files/' + 'DC2_new.cal', 'r+')
    content_DC2_new = DC2_new.readlines() #reads line by line and out puts a list of each line

    #Re-evaluate the parameters with the new values
    data_line_DC2_new = content_DC2_new[ch+15].split() #+15 skipping the first lines
    a0_old = float(data_line_DC2_new[0])
    a1_old = float(data_line_DC2_new[1])
    a2_old = float(data_line_DC2_new[2]) #It is zero generally, so it is not important and is not apply

    #Second correction over previous values
    a0 = p0 + p1 * a0_old
    a1 = p1 * a1_old
    '''------------------work in progress. Is not clear and right---------------'''
    a2 = (p2 * a0_old**2 + p2 * a1_old**2 + 2*p2 * a0_old * a1_old)*10**(-6)
    '''-------------------------------------------------------------------------'''
    content_DC2_new[ch+15] = "%f  %f  %f // %i ch %s\n" %(a0, a1, a2, 2, str(ch)) #replaces content_DC2_new

    DC2_new.close()
    DC2_new = open(Module_path + '/Outputfiles/Calibration_files/' + 'DC2_new.cal', 'w') #clears content of file.
    DC2_new.close()
    DC2_new = open(Module_path + '/Outputfiles/Calibration_files/' + 'DC2_new.cal', 'r+')

    for item in content_DC2_new: #rewrites file content from list
        DC2_new.write("%s" % item)
    del content_DC2_new
    DC2_new.close()

print('\n')
print('The file: ' + Module_path + '/Outputfiles/Calibration_files/' + 'DC2_new.cal' + ' was saved\n')

c3.Close()


#######################################################################################################################################################
############### Fit the results: (DC0_QV vs DC0_QVN) , (DC1_QV vs DC1_QVN) ,  (DC2_QV vs DC2_QVN) , (DC3_QV vs DC3_QVN) ###############################
#######################################################################################################################################################

for DCn in range(0, 4):

    c4 = TCanvas('c4', 'DC' + str(DCn) + '_QV vs DC' + str(DCn) + '_QVN', 500, 150, 1000, 700 )
    c4.SetFillColor(0)
    c4.GetFrame().SetFillColor(21)
    c4.GetFrame().SetBorderSize(6)
    c4.GetFrame().SetBorderMode(-1)

    h_DCQV_DCQVN = TH2F('h_DCQV_DCQVN', 'DC' + str(DCn) + '_QV vs DC' + str(DCn) + '_QVN', 160, 0, 160, 500, -50, 2600)

    h_DCQV_DCQVN.SetFillColor(42)
    h_DCQV_DCQVN.SetYTitle('DC' + str(DCn) + '_QV')
    h_DCQV_DCQVN.SetXTitle('DC' + str(DCn) + '_QVN')

    gStyle.SetStatY(0.74);
    gStyle.SetStatX(0.99);
    gStyle.SetStatW(0.13);
    gStyle.SetStatH(0.13);

    mitree.Draw("DC" + str(DCn) + "_QV:DC" + str(DCn) + "_QVN>>h_DCQV_DCQVN","","col")

    c4.SetLogz()
    c4.Update()
    c4.SaveAs(Module_path + '/Outputfiles/Figures/Final_Results/DC' + str(DCn) + '_QV--DC' + str(DCn) + '_QVN.png')
    #c4.SaveAs(Module_path + '/Outputfiles/Figures/Final_Results/New_post_MyVAna_calibration/DC' + str(DCn) + '_QV--DC' + str(DCn) + '_QVN_post_MyVAna.png')

    del h_DCQV_DCQVN

    c4.Close()
