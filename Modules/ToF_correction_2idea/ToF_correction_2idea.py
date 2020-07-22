#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat 4 June 17:41:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

ToF_correction_in_AoverQ MODULE -- The module to correct the ToF (time of flight) in A/Q

The code generates:
-- Outputfiles/Figures/

"""
MODULE_name = 'ToF_correction_2idea'

'''
----------------------------------------------------------------- Protected part (Don't touch nothing) ----------------------------------------------------------------------------------------------------------------
'''
import os, sys
sys.path.append('.')
sys.path.append('..')
basepath = os.path.abspath(__file__).rsplit('/Fission_Analysis_VAMOS/',1)[0]+'/Fission_Analysis_VAMOS/'
sys.path.append(basepath)
Module_path = basepath + '/Modules/' + MODULE_name + '/'
sys.path.append(Module_path)

'''
---------------------------------------------------- Import packages and Framework functions ----------------------------------------------------------------------------------------------------
'''
import numpy as np
import Framework.read_and_save.read_and_save as RAS
from Plotter.Plotter import Plotter
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

'''
---------------------------------------------- Open and read .hdf5 original file like a hdf5 object ----------------------------------------------------------------------------------
'''
hdf5_folder_path = basepath + 'Data_hdf5/' + MODULE_name + '_run/' #The folder with files after the calibrations comming from RootA transformed in hdf5
file_14_degrees = 'Analysis_14_file_ToF_variables' #Without .hdf5 extension
file_21_degrees = 'Analysis_21_file_ToF_variables' #Without .hdf5 extension
file_14_21_degrees = 'Analysis_14+21_file_ToF_variables' #Without .hdf5 extension

data_14_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_14_degrees) #Array-matrix with our data
data_21_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_21_degrees) #Array-matrix with our data
data_14_21_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_14_21_degrees) #Array-matrix with our data

#CONDITIONS FOR 14, 21 AND 14+21 (after seeing Charge_states module variables):
condition_mass_14 = ((data_14_degrees['Xf'][:] > -1500) & (data_14_degrees['Yf'][:] > -1500)
                & (data_14_degrees['Yf'][:] > -110) & (data_14_degrees['Yf'][:] < 50)
                & (data_14_degrees['Pf'][:] > -100) & (data_14_degrees['Pf'][:] < 100)
                & (data_14_degrees['M'][:] < 180) & (data_14_degrees['M'][:] > 70)
                & (data_14_degrees['M_Q'][:] < 4) & (data_14_degrees['M_Q'][:] > 2.25)
                & (data_14_degrees['MW_Nr'][:] >= 0) & (data_14_degrees['Qi'][:] == 40))

condition_mass_21 = ((data_21_degrees['Xf'][:] > -1500) & (data_21_degrees['Yf'][:] > -1500)
                & (data_21_degrees['Yf'][:] > -110) & (data_21_degrees['Yf'][:] < 50)
                & (data_21_degrees['Pf'][:] > -100) & (data_21_degrees['Pf'][:] < 100)
                & (data_21_degrees['M'][:] < 180) & (data_21_degrees['M'][:] > 70)
                & (data_21_degrees['M_Q'][:] < 4) & (data_21_degrees['M_Q'][:] > 2.25)
                & (data_21_degrees['MW_Nr'][:] >= 0))

condition_mass_14_21 = ((data_14_21_degrees['Xf'][:] > -1500) & (data_14_21_degrees['Yf'][:] > -1500)
                & (data_14_21_degrees['Yf'][:] > -110) & (data_14_21_degrees['Yf'][:] < 50)
                & (data_14_21_degrees['Pf'][:] > -100) & (data_14_21_degrees['Pf'][:] < 100)
                & (data_14_21_degrees['M'][:] < 180) & (data_14_21_degrees['M'][:] > 70)
                & (data_14_21_degrees['M_Q'][:] < 4) & (data_14_21_degrees['M_Q'][:] > 2.25)
                & (data_14_21_degrees['MW_Nr'][:] >= 0))


'''
------------------------------------------------------ Pattern A vs A/Q simulated and A vs A/Q real data -----------------------------------------------------------
'''

Q_simulated = np.linspace(30,60,60-30+1)
A_simulated = np.linspace(60,190,190-60+1)

Q,A=np.meshgrid(Q_simulated, A_simulated)

A_Q = A/Q

'''
------------------------------------------------ Finding peaks in histograms M_Q into 2histo M vs M_Q --------------------------------------------------------------
'''

################################################## 14 degrees
#for q in range(30, 51):
for q in range(40, 41):
    #charge q points pattern to plot it
    q_x = np.array([])
    q_y = np.array([])

    for j in range(0, len(Q)):
        for i in range(0, len(Q[j])):
            if Q[j][i] == q:
                q_x = np.append(q_x, A_Q[j][i])
                q_y = np.append(q_y, A[j][i])

    #variable condtion with charge q
    condition_mass_14_q = ((data_14_degrees['Xf'][:] > -1500) & (data_14_degrees['Yf'][:] > -1500)
                    & (data_14_degrees['Yf'][:] > -110) & (data_14_degrees['Yf'][:] < 50)
                    & (data_14_degrees['Pf'][:] > -100) & (data_14_degrees['Pf'][:] < 100)
                    & (data_14_degrees['M'][:] < 180) & (data_14_degrees['M'][:] > 70)
                    & (data_14_degrees['M_Q'][:] < 4.0) & (data_14_degrees['M_Q'][:] > 2.25)
                    & (data_14_degrees['MW_Nr'][:] >= 0) & (data_14_degrees['Qi'][:] == q))

    #change bins, distance and height to find better the peaks:
    if q == 30:
        bins=450
        distance=7.0
        height=100
    elif q == 31:
        bins=500
        distance=7.0
        height=150
    elif q == 32:
        bins=750
        distance=8.0
        height=200
    elif (q >= 33) and (q <= 36):
        bins=1100
        distance=12.0
        height=350
    elif (q >= 37) and (q <= 39):
        bins=1400
        distance=15.0
        height=800
    elif q==40:
        bins=20000
        distance=180.0
        height=80
    elif (q >= 41) and (q <= 46):
        bins=1900
        distance=17.0
        height=500
    elif (q >= 47) and (q <= 49):
        bins=1000
        distance=10.0
        height=400
    elif q == 50:
        bins=700
        distance=10.0
        height=250

    histo, bin_edges = np.histogram(data_14_degrees['M_Q'][condition_mass_14_q], bins=bins)
    bin_edges = bin_edges[1:]
    fig = plt.figure(figsize=(12,7))
    plt.plot(bin_edges, histo)
    peaks, _ = find_peaks(histo, distance = distance, height=height)
    plt.plot(bin_edges[peaks], histo[peaks], "x")
    texto = 'Selection:\n Z>0 \n Zi>0 \n 100<M<160 \n 2.6<M_Q<3.5 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0 \n Qi==%i' %q
    plt.text(0.9, 0.8, s=texto, fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='blue', pad=8.0), ha='center', va='center')
    plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/14_degrees_peaks/' + '14_degrees_peaks_q_%i.png' %q)
    print(q)
    plt.close('all')
    plt.close(fig)


    M_vs_M_Q_14_pattern_q = Plotter([data_14_degrees['M_Q'][condition_mass_14_q],data_14_degrees['M'][condition_mass_14_q]]) #Create the base with the variables in a object
    M_vs_M_Q_14_pattern_q.SetFigSize(12,7)
    M_vs_M_Q_14_pattern_q.SetBinX(500)
    M_vs_M_Q_14_pattern_q.SetBinY(500)
    M_vs_M_Q_14_pattern_q.SetFigTitle(r'M vs M_Q with pattern and q = %i     14$\degree$' %q, 20)
    M_vs_M_Q_14_pattern_q.SetLabelX('M_Q', 20)
    M_vs_M_Q_14_pattern_q.SetLabelY('M', 20)
    M_vs_M_Q_14_pattern_q.SetSizeTicksX(10)
    M_vs_M_Q_14_pattern_q.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 100<M<160 \n 2.6<M_Q<3.5 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0 \n Qi==%i' %q)
    M_vs_M_Q_14_pattern_q.SetLimX((2.4,3.6))
    M_vs_M_Q_14_pattern_q.SetLimY((q*2.5,q*4.0))
    M_vs_M_Q_14_pattern_q.Histo_2D() #Draw it

    #plot pattern charge
    plt.plot(q_x, q_y, '.-k', label='q = %i' %q)
    plt.legend()

    ##### make histograms in X to see the position of highs ########
    left, width = 0.18, 0.45
    bottom, height = 0.1, 0.40
    bottom_h = left_h = left + width + 0.02
    # definition of the rectangule-places for X-Histogram
    rect_histx = [left, bottom_h, width, 0.2]
    # define the axes for each plot-zone
    axHistx = plt.axes(rect_histx)
    axHistx.plot(bin_edges, histo)
    axHistx.plot(bin_edges[peaks], histo[peaks], "x")

    ######### Save and show the created figure
    M_vs_M_Q_14_pattern_q.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/14_degrees_pattern_and_q_peaks/')
    M_vs_M_Q_14_pattern_q.SaveFig('M_vs_M_Q_14_pattern_q_%i' %q)
    M_vs_M_Q_14_pattern_q.Show(1) #show during 1 seconds, the close authomatically
    M_vs_M_Q_14_pattern_q.Close() #close all windows, axes and figures running backend
    del M_vs_M_Q_14_pattern_q #erase M_vs_M_Q_14_pattern_q (is an object)


    #make the difference between pattern and peaks
    q_data = bin_edges[peaks]
    q_pattern = np.array([])
    diff_pattern_q = np.array([])

    #finding (matching pattern to peaks) first index of first element to match with peaks (the pattern is longer than q_data peaks always)
    bool_q_x = np.where(q_x >= q_data[0])
    bool_q_x = bool_q_x[0]
    q_pattern = q_x[bool_q_x[0:len(q_data)]]
    if len(q_pattern) == len(q_data):
        diff_pattern_q = q_pattern - q_data

    fig2 = plt.figure(figsize=(12,7))
    plt.plot(np.arange(0, len(diff_pattern_q), 1), diff_pattern_q, '.-')
    plt.grid()
    plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/14_degrees_difference_peaks/' + '14_degrees_difference_peaks_q_%i.png' %q)
    plt.close('all')

    del histo
    del bin_edges
    del peaks
    del condition_mass_14_q
    del fig
    del fig2
    del q_data
    del q_pattern
    del bool_q_x
    del q_x
    del diff_pattern_q

'''
################################################## 21 degrees

for q in range(30, 50):
    #charge q points pattern to plot it
    q_x = np.array([])
    q_y = np.array([])

    for j in range(0, len(Q)):
        for i in range(0, len(Q[j])):
            if Q[j][i] == q:
                q_x = np.append(q_x, A_Q[j][i])
                q_y = np.append(q_y, A[j][i])

    #variable condtion with charge q
    condition_mass_21_q = ((data_21_degrees['Xf'][:] > -1500) & (data_21_degrees['Yf'][:] > -1500)
                    & (data_21_degrees['Yf'][:] > -110) & (data_21_degrees['Yf'][:] < 50)
                    & (data_21_degrees['Pf'][:] > -100) & (data_21_degrees['Pf'][:] < 100)
                    & (data_21_degrees['M'][:] < 180) & (data_21_degrees['M'][:] > 70)
                    & (data_21_degrees['M_Q'][:] < 4.0) & (data_21_degrees['M_Q'][:] > 2.25)
                    & (data_21_degrees['MW_Nr'][:] >= 0) & (data_21_degrees['Qi'][:] == q))

    #change bins, distance and height to find better the peaks:
    if q <= 32:
        bins=450
        distance=7.0
        height=100
    elif q >= 46:
        bins=550
        distance=6.0
        height=100
    else:
        bins=600
        distance=6.05
        height=500

    histo, bin_edges = np.histogram(data_21_degrees['M_Q'][condition_mass_21_q], bins=bins)
    bin_edges = bin_edges[1:]
    fig = plt.figure(figsize=(12,7))
    plt.plot(bin_edges, histo)
    peaks, _ = find_peaks(histo, distance = distance, height=height)
    plt.plot(bin_edges[peaks], histo[peaks], "x")
    texto = 'Selection:\n Z>0 \n Zi>0 \n 100<M<160 \n 2.6<M_Q<3.5 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0 \n Qi==%i' %q
    plt.text(0.9, 0.8, s=texto, fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='blue', pad=8.0), ha='center', va='center')
    plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/14_degrees_peaks/' + '14_degrees_peaks_q_%i.png' %q)
    print(q)
    plt.close('all')
    plt.close(fig)


    M_vs_M_Q_21_pattern_q = Plotter([data_21_degrees['M_Q'][condition_mass_21_q],data_21_degrees['M'][condition_mass_21_q]]) #Create the base with the variables in a object
    M_vs_M_Q_21_pattern_q.SetFigSize(12,7)
    M_vs_M_Q_21_pattern_q.SetBinX(500)
    M_vs_M_Q_21_pattern_q.SetBinY(500)
    M_vs_M_Q_21_pattern_q.SetFigTitle(r'M vs M_Q with pattern and q = %i     21$\degree$' %q, 20)
    M_vs_M_Q_21_pattern_q.SetLabelX('M_Q', 20)
    M_vs_M_Q_21_pattern_q.SetLabelY('M', 20)
    M_vs_M_Q_21_pattern_q.SetSizeTicksX(10)
    M_vs_M_Q_21_pattern_q.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 100<M<160 \n 2.6<M_Q<3.5 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0 \n Qi==%i' %q)
    M_vs_M_Q_21_pattern_q.SetLimX((2.4,3.6))
    M_vs_M_Q_21_pattern_q.SetLimY((q*2.5,q*4.0))
    M_vs_M_Q_21_pattern_q.Histo_2D() #Draw it

    #plot pattern charge
    plt.plot(q_x, q_y, '.-k', label='q = %i' %q)
    plt.legend()

    ##### make histograms in X to see the position of highs ########
    left, width = 0.18, 0.45
    bottom, height = 0.1, 0.40
    bottom_h = left_h = left + width + 0.02
    # definition of the rectangule-places for X-Histogram
    rect_histx = [left, bottom_h, width, 0.2]
    # define the axes for each plot-zone
    axHistx = plt.axes(rect_histx)
    axHistx.plot(bin_edges, histo)
    axHistx.plot(bin_edges[peaks], histo[peaks], "x")

    ######### Save and show the created figure
    M_vs_M_Q_21_pattern_q.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/21_degrees_pattern_and_q_peaks/')
    M_vs_M_Q_21_pattern_q.SaveFig('M_vs_M_Q_21_pattern_q_%i' %q)
    M_vs_M_Q_21_pattern_q.Show(1) #show during 1 seconds, the close authomatically
    M_vs_M_Q_21_pattern_q.Close() #close all windows, axes and figures running backend
    del M_vs_M_Q_21_pattern_q #erase M_vs_M_Q_21_pattern_q (is an object)


    #make the difference between pattern and peaks
    q_data = bin_edges[peaks]
    q_pattern = np.array([])
    diff_pattern_q = np.array([])

    #finding (matching pattern to peaks) first index of first element to match with peaks (the pattern is longer than q_data peaks always)
    bool_q_x = np.where(q_x >= q_data[0])
    bool_q_x = bool_q_x[0]
    q_pattern = q_x[bool_q_x[0:len(q_data)]]
    if len(q_pattern) == len(q_data):
        diff_pattern_q = q_pattern - q_data

    fig2 = plt.figure(figsize=(12,7))
    plt.plot(np.arange(0, len(diff_pattern_q), 1), diff_pattern_q, '.-')
    plt.grid()
    plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/21_degrees_difference_peaks/' + '21_degrees_difference_peaks_q_%i.png' %q)
    plt.close('all')

    del histo
    del bin_edges
    del peaks
    del condition_mass_21_q
    del fig
    del fig2
    del q_data
    del q_pattern
    del bool_q_x
    del q_x
    del diff_pattern_q


################################################## 14+21 degrees

for q in range(30, 51):
    #charge q points pattern to plot it
    q_x = np.array([])
    q_y = np.array([])

    for j in range(0, len(Q)):
        for i in range(0, len(Q[j])):
            if Q[j][i] == q:
                q_x = np.append(q_x, A_Q[j][i])
                q_y = np.append(q_y, A[j][i])

    #variable condtion with charge q
    condition_mass_14_21_q = ((data_14_21_degrees['Xf'][:] > -1500) & (data_14_21_degrees['Yf'][:] > -1500)
                    & (data_14_21_degrees['Yf'][:] > -110) & (data_14_21_degrees['Yf'][:] < 50)
                    & (data_14_21_degrees['Pf'][:] > -100) & (data_14_21_degrees['Pf'][:] < 100)
                    & (data_14_21_degrees['M'][:] < 180) & (data_14_21_degrees['M'][:] > 70)
                    & (data_14_21_degrees['M_Q'][:] < 4.0) & (data_14_21_degrees['M_Q'][:] > 2.25)
                    & (data_14_21_degrees['MW_Nr'][:] >= 0) & (data_14_21_degrees['Qi'][:] == q))

    #change bins, distance and height to find better the peaks:
    if q <= 32:
        bins=450
        distance=7.0
        height=100
    elif q >= 48:
        bins=550
        distance=6.0
        height=200
    else:
        bins=600
        distance=6.05
        height=500

    histo, bin_edges = np.histogram(data_14_21_degrees['M_Q'][condition_mass_14_21_q], bins=bins)
    bin_edges = bin_edges[1:]
    fig = plt.figure(figsize=(12,7))
    plt.plot(bin_edges, histo)
    peaks, _ = find_peaks(histo, distance = distance, height=height)
    plt.plot(bin_edges[peaks], histo[peaks], "x")
    texto = 'Selection:\n Z>0 \n Zi>0 \n 100<M<160 \n 2.6<M_Q<3.5 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0 \n Qi==%i' %q
    plt.text(0.9, 0.8, s=texto, fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='blue', pad=8.0), ha='center', va='center')
    plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/14+21_degrees_peaks/' + '14+21_degrees_peaks_q_%i.png' %q)
    print(q)
    plt.close('all')
    plt.close(fig)


    M_vs_M_Q_14_21_pattern_q = Plotter([data_14_21_degrees['M_Q'][condition_mass_14_21_q],data_14_21_degrees['M'][condition_mass_14_21_q]]) #Create the base with the variables in a object
    M_vs_M_Q_14_21_pattern_q.SetFigSize(12,7)
    M_vs_M_Q_14_21_pattern_q.SetBinX(500)
    M_vs_M_Q_14_21_pattern_q.SetBinY(500)
    M_vs_M_Q_14_21_pattern_q.SetFigTitle(r'M vs M_Q with pattern and q = %i     14$\degree$+21$\degree$' %q, 20)
    M_vs_M_Q_14_21_pattern_q.SetLabelX('M_Q', 20)
    M_vs_M_Q_14_21_pattern_q.SetLabelY('M', 20)
    M_vs_M_Q_14_21_pattern_q.SetSizeTicksX(10)
    M_vs_M_Q_14_21_pattern_q.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 100<M<160 \n 2.6<M_Q<3.5 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0 \n Qi==%i' %q)
    M_vs_M_Q_14_21_pattern_q.SetLimX((2.4,3.6))
    M_vs_M_Q_14_21_pattern_q.SetLimY((q*2.5,q*4.0))
    M_vs_M_Q_14_21_pattern_q.Histo_2D() #Draw it

    #plot pattern charge
    plt.plot(q_x, q_y, '.-k', label='q = %i' %q)
    plt.legend()

    ##### make histograms in X to see the position of highs ########
    left, width = 0.18, 0.45
    bottom, height = 0.1, 0.40
    bottom_h = left_h = left + width + 0.02
    # definition of the rectangule-places for X-Histogram
    rect_histx = [left, bottom_h, width, 0.2]
    # define the axes for each plot-zone
    axHistx = plt.axes(rect_histx)
    axHistx.plot(bin_edges, histo)
    axHistx.plot(bin_edges[peaks], histo[peaks], "x")

    ######### Save and show the created figure
    M_vs_M_Q_14_21_pattern_q.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/14+21_degrees_pattern_and_q_peaks/')
    M_vs_M_Q_14_21_pattern_q.SaveFig('M_vs_M_Q_14_21_pattern_q_%i' %q)
    M_vs_M_Q_14_21_pattern_q.Show(1) #show during 1 seconds, the close authomatically
    M_vs_M_Q_14_21_pattern_q.Close() #close all windows, axes and figures running backend
    del M_vs_M_Q_14_21_pattern_q #erase M_vs_M_Q_21_pattern_q (is an object)


    #make the difference between pattern and peaks
    q_data = bin_edges[peaks]
    q_pattern = np.array([])
    diff_pattern_q = np.array([])

    #finding (matching pattern to peaks) first index of first element to match with peaks (the pattern is longer than q_data peaks always)
    bool_q_x = np.where(q_x >= q_data[0])
    bool_q_x = bool_q_x[0]
    q_pattern = q_x[bool_q_x[0:len(q_data)]]
    if len(q_pattern) == len(q_data):
        diff_pattern_q = q_pattern - q_data

    fig2 = plt.figure(figsize=(12,7))
    plt.plot(np.arange(0, len(diff_pattern_q), 1), diff_pattern_q, '.-')
    plt.grid()
    plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/14+21_degrees_difference_peaks/' + '14+21_degrees_difference_peaks_q_%i.png' %q)
    plt.close('all')

    del histo
    del bin_edges
    del peaks
    del condition_mass_14_21_q
    del fig
    del fig2
    del q_data
    del q_pattern
    del bool_q_x
    del q_x
    del diff_pattern_q
'''

'''
################################################################## 14 degrees
A_vs_A_Q_14_data_pattern = Plotter([data_14_degrees['M_Q'][condition_mass_14],data_14_degrees['M'][condition_mass_14]]) #Create the base with the variables in a object
A_vs_A_Q_14_data_pattern.SetFigSize(12,7)
A_vs_A_Q_14_data_pattern.SetBinX(500)
A_vs_A_Q_14_data_pattern.SetBinY(500)
A_vs_A_Q_14_data_pattern.SetFigTitle(r'M vs M_Q with pattern        14$\degree$', 20)
A_vs_A_Q_14_data_pattern.SetLabelX('M_Q', 20)
A_vs_A_Q_14_data_pattern.SetLabelY('M', 20)
A_vs_A_Q_14_data_pattern.SetSizeTicksX(10)
A_vs_A_Q_14_data_pattern.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 100<M<160 \n 2.6<M_Q<3.5 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0 \n Qi==40')
A_vs_A_Q_14_data_pattern.SetLimX((2.6,3.5))
A_vs_A_Q_14_data_pattern.SetLimY((100,160))
#A_vs_A_Q_14_data_pattern.ScatterXYpoints_histograms_X_Y() #Draw it
A_vs_A_Q_14_data_pattern.Histo_2D() #Draw it
plt.plot(q_40_x, q_40_y, '.-k', label='q = 40')

##### make histograms in X and Y to see the position of highs ########
left, width = 0.1, 0.62
bottom, height = 0.1, 0.62
bottom_h = left_h = left + width + 0.02
# definition of the rectangule-places for plot: 1) Scatter 2) X-Histogram  3) Y-Histogram
rect_histx = [left, bottom_h, width, 0.2]
#rect_histy = [left_h, bottom, 0.2, height]
# define the axes for each plot-zone
axHistx = plt.axes(rect_histx)
#axHisty = plt.axes(rect_histy)

axHistx.hist(data_14_degrees['M_Q'][condition_mass_14], bins=500, orientation='vertical', edgecolor='k', linewidth=0.5, histtype='step')
#axHisty.hist(data_14_degrees['M'][condition_mass_14], bins=500, orientation='horizontal', facecolor='g', edgecolor='k', linewidth=0.3, histtype='bar')

plt.legend()

######### Save and show the created figure
A_vs_A_Q_14_data_pattern.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
A_vs_A_Q_14_data_pattern.SaveFig('A_vs_A_Q_14_data_pattern')
A_vs_A_Q_14_data_pattern.Show(1) #show during 1 seconds, the close authomatically
A_vs_A_Q_14_data_pattern.Close() #close all windows, axes and figures running backend
del A_vs_A_Q_14_data_pattern #erase A_vs_A_Q_14_data_pattern (is an object)
'''
