#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu 4 June 16:40:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

ToF_correction_in_AoverQ MODULE -- The module to correct the ToF (time of flight) in A/Q

The code generates:
-- Outputfiles/Figures/

"""
MODULE_name = 'ToF_correction_in_AoverQ'

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
from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition, mark_inset)
from scipy.optimize import curve_fit

'''
---------------------------------------------- Open and read .hdf5 original file like a hdf5 object ----------------------------------------------------------------------------------
'''
hdf5_folder_path = basepath + 'Data_hdf5/' + MODULE_name + '_run/' #The folder with files after the calibrations comming from RootA transformed in hdf5
file_14_degrees = 'Analysis_14_file_ToF_correction_in_AoverQ_variables' #Without .hdf5 extension
file_21_degrees = 'Analysis_21_file_ToF_correction_in_AoverQ_variables' #Without .hdf5 extension
file_14_21_degrees = 'Analysis_14+21_file_ToF_correction_in_AoverQ_variables' #Without .hdf5 extension

data_14_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_14_degrees) #Array-matrix with our data
data_21_degrees = RAS.Read_hdf5_file(hdf5_folder_path, file_21_degrees) #Array-matrix with our data
data_14_21_degrees= RAS.Read_hdf5_file(hdf5_folder_path, file_14_21_degrees) #Array-matrix with our data

#CONDITIONS FOR 14, 21 AND 14+21 (after seeing Charge_states module variables):
condition_mass_14 = ((data_14_degrees['Xf'][:] > -1500) & (data_14_degrees['Yf'][:] > -1500)
                & (data_14_degrees['Yf'][:] > -110) & (data_14_degrees['Yf'][:] < 50)
                & (data_14_degrees['Pf'][:] > -100) & (data_14_degrees['Pf'][:] < 100)
                & (data_14_degrees['M'][:] < 180) & (data_14_degrees['M'][:] > 70)
                & (data_14_degrees['M_Q'][:] < 4) & (data_14_degrees['M_Q'][:] > 2.25)
                & (data_14_degrees['MW_Nr'][:] >= 0))

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
------------------------------------------------------ Pattern A vs A/Q simulated -----------------------------------------------------------
'''

fig = plt.figure(figsize=(10,7))

ax1 = fig.add_subplot(111)

Q_simulated = np.linspace(30,60,60-30+1)
A_simulated = np.linspace(80,190,190-80+1)

Q,A=np.meshgrid(Q_simulated, A_simulated)

A_Q = A/Q

plt.plot(A_Q,A, '.k')
plt.xlim(2.5,3.5)
plt.ylim(80,190)

#charge q = 40 in blue
q_40_x = np.array([])
q_40_y = np.array([])
for j in range(0, len(Q)):
    for i in range(0, len(Q[j])):
        if Q[j][i] == 40.0:
            q_40_x = np.append(q_40_x, A_Q[j][i])
            q_40_y = np.append(q_40_y, A[j][i])
plt.plot(q_40_x, q_40_y, '.-b', label='q = 40')

#charge q = 50 in green
q_50_x = np.array([])
q_50_y = np.array([])
for j in range(0, len(Q)):
    for i in range(0, len(Q[j])):
        if Q[j][i] == 50.0:
            q_50_x = np.append(q_50_x, A_Q[j][i])
            q_50_y = np.append(q_50_y, A[j][i])
plt.plot(q_50_x, q_50_y, '.-g', label='q = 50')

#A/Q = 3 in red
AQ_x = np.array([])
AQ_y = np.array([])
for j in range(0, len(A_Q)):
    for i in range(0, len(A_Q[j])):
        if A_Q[j][i] == 3.0:
            AQ_x = np.append(AQ_x, A_Q[j][i])
            AQ_y = np.append(AQ_y, A[j][i])
plt.plot(AQ_x, AQ_y, '.-r', label='A/Q = 3.0')

plt.legend()

ax1.set_ylabel(r'A', fontsize=20)
ax1.set_xlabel(r'A/Q', fontsize=20)

print('Saving figure as:' + basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/' + 'A_vs_A_Q_pattern' + '.png')
print('\n')
plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/' + 'A_vs_A_Q_pattern' + '.png', format='png')
plt.show()


'''
---------------------------------------------------------- M_Q pre-corrections -------------------------------------------------------------
'''

################################################################## 14 degrees
M_Q_14 = Plotter([data_14_degrees['M_Q'][condition_mass_14]]) #Create the base with the variables in a object
M_Q_14.SetFigSize(12,7)
M_Q_14.SetBinX(10000)
M_Q_14.SetFigTitle(r'M_Q        14$\degree$', 20)
M_Q_14.SetLabelX('M_Q', 20)
M_Q_14.SetLabelY('counts', 20)
M_Q_14.SetSizeTicksX(10)
M_Q_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0')
M_Q_14.SetLimX((2.6,3.6))
M_Q_14.Histo_1D() #Draw it

######### Save and show the created figure
M_Q_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_Q_14.SaveFig('M_Q_14_histogram')
M_Q_14.Show(1) #show during 1 seconds, the close authomatically
M_Q_14.Close() #close all windows, axes and figures running backend
del M_Q_14 #erase M_Q_14 (is an object)


################################################################## 21 degrees
M_Q_21 = Plotter([data_21_degrees['M_Q'][condition_mass_21]]) #Create the base with the variables in a object
M_Q_21.SetFigSize(12,7)
M_Q_21.SetBinX(10000)
M_Q_21.SetFigTitle(r'M_Q        21$\degree$', 20)
M_Q_21.SetLabelX('M_Q', 20)
M_Q_21.SetLabelY('counts', 20)
M_Q_21.SetSizeTicksX(10)
M_Q_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0')
M_Q_21.SetLimX((2.6,3.6))
M_Q_21.Histo_1D() #Draw it

######### Save and show the created figure
M_Q_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_Q_21.SaveFig('M_Q_21_histogram')
M_Q_21.Show(1) #show during 1 seconds, the close authomatically
M_Q_21.Close() #close all windows, axes and figures running backend
del M_Q_21 #erase M_Q_21 (is an object)


################################################################## 14+21 degrees
M_Q_14_21 = Plotter([data_14_21_degrees['M_Q'][condition_mass_14_21]]) #Create the base with the variables in a object
M_Q_14_21.SetFigSize(12,7)
M_Q_14_21.SetBinX(10000)
M_Q_14_21.SetFigTitle(r'M_Q        14$\degree$+21$\degree$', 20)
M_Q_14_21.SetLabelX('M_Q', 20)
M_Q_14_21.SetLabelY('counts', 20)
M_Q_14_21.SetSizeTicksX(10)
M_Q_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0')
M_Q_14_21.SetLimX((2.6,3.6))
M_Q_14_21.Histo_1D() #Draw it

######### Save and show the created figure
M_Q_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_Q_14_21.SaveFig('M_Q_14_21_histogram')
M_Q_14_21.Show(1) #show during 1 seconds, the close authomatically
M_Q_14_21.Close() #close all windows, axes and figures running backend
del M_Q_14_21 #erase M_Q_14_21 (is an object)



'''
---------------------------------------------------- M_Q special zoom plots fitting to a gaussian --------------------------------------------------------
'''

################################################### 14 degrees

binning = 10000


fig = plt.figure(figsize=(12,7))

ax1 = fig.add_subplot(111)
ax1.hist(data_14_degrees['M_Q'][condition_mass_14], bins=binning, weights=None, histtype='step', align='mid', orientation='vertical', color='b', label = 'M/Q')

ax1.set_ylabel(r'counts', fontsize=20)
ax1.set_xlabel(r'$\left(\frac{M}{Q}\right)$', fontsize=20)
ax1.grid(True)

plt.suptitle(r'Mass over Q      14$\degree$', fontsize=18, x=0.4, y=0.94)

plt.gca().set_xticks(np.arange(70.0, 180.0, 10.0), minor=True)
ax1.set_xlim([2.6, 3.6])
ax1.set_ylim([0.0, 3500])
ax1.xaxis.grid(True)
ax1.legend(loc=2, fontsize = 12)
plt.text(0.9, 0.3, 'Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0', fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='blue', pad=8.0), ha='center', va='center')

# Create a set of inset Axes: these should fill the bounding box allocated to
# them.
ax2 = plt.axes([0,0,1,1])
# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax1, [0.75,0.7,0.3,0.4])
ax2.set_axes_locator(ip)
# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
mark_inset(ax1, ax2, loc1=2, loc2=4, fc="none", ec='0.5')

# The data into the ax2
ax2.hist(data_14_degrees['M_Q'][condition_mass_14], bins=binning, weights=None, histtype='step', align='mid', orientation='vertical', color='b', label = 'M/Q')

ax2.set_xlim([2.985, 3.02])
ax2.set_ylim([1500, 3200])
ax2.grid(True, which='both')

####### Fit a gaussian in the zoom
def gaussian(x, a, mean, sigma):
    return a * np.exp(-((x - mean)**2 / (2 * sigma**2)))

#Evaluate the histogram
histo, bins_edge = np.histogram(data_14_degrees['M_Q'][condition_mass_14], bins=binning)

#plt.bar(bins_edge[:-1], histo, width=bins_edge[2]-bins_edge[1])
bins_edge = bins_edge[:-1]

bins_edge_cut = bins_edge[(bins_edge > 2.98) & (bins_edge < 3.02)]
histo_cut = histo[(bins_edge > 2.98) & (bins_edge < 3.02)]

popt, pcov = curve_fit(gaussian, bins_edge_cut, histo_cut, bounds=((1500, 2.9, 0.001), (3000, 3.1, 0.008)))

i = np.linspace(2.991, 3.01, 1000)

ax1.plot(i, gaussian(i, *popt), 'r')
ax2.plot(i, gaussian(i, *popt), 'r')

plt.text(0.85, 0.5, r'$\mu$ = %.7f $\pm$ %.7f' %(popt[1],pcov[1][1]) , fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='red', pad=8.0), ha='center', va='center')


######################
print('Saving figure as:' + basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/' + 'M_Q_14_fit_gauss' + '.png')
print('\n')
plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/' + 'M_Q_14_fit_gauss' + '.png', format='png')
plt.close()

del fig
del ax1
del ax2





################################################### 21 degrees

binning = 10000


fig = plt.figure(figsize=(12,7))

ax1 = fig.add_subplot(111)
ax1.hist(data_21_degrees['M_Q'][condition_mass_21], bins=binning, weights=None, histtype='step', align='mid', orientation='vertical', color='b', label = 'M/Q')

ax1.set_ylabel(r'counts', fontsize=20)
ax1.set_xlabel(r'$\left(\frac{M}{Q}\right)$', fontsize=20)
ax1.grid(True)

plt.suptitle(r'Mass over Q      21$\degree$', fontsize=18, x=0.4, y=0.94)

plt.gca().set_xticks(np.arange(70.0, 180.0, 10.0), minor=True)
ax1.set_xlim([2.6, 3.6])
ax1.set_ylim([0.0, 6000])
ax1.xaxis.grid(True)
ax1.legend(loc=2, fontsize = 12)
plt.text(0.9, 0.3, 'Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0', fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='blue', pad=8.0), ha='center', va='center')

# Create a set of inset Axes: these should fill the bounding box allocated to
# them.
ax2 = plt.axes([0,0,1,1])
# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax1, [0.75,0.7,0.3,0.4])
ax2.set_axes_locator(ip)
# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
mark_inset(ax1, ax2, loc1=2, loc2=4, fc="none", ec='0.5')

# The data into the ax2
ax2.hist(data_21_degrees['M_Q'][condition_mass_21], bins=binning, weights=None, histtype='step', align='mid', orientation='vertical', color='b', label = 'M/Q')

ax2.set_xlim([2.985, 3.02])
ax2.set_ylim([2500, 5500])
ax2.grid(True, which='both')

####### Fit a gaussian in the zoom
def gaussian(x, a, mean, sigma):
    return a * np.exp(-((x - mean)**2 / (2 * sigma**2)))

#Evaluate the histogram
histo, bins_edge = np.histogram(data_21_degrees['M_Q'][condition_mass_21], bins=binning)

#plt.bar(bins_edge[:-1], histo, width=bins_edge[2]-bins_edge[1])
bins_edge = bins_edge[:-1]

bins_edge_cut = bins_edge[(bins_edge > 2.98) & (bins_edge < 3.02)]
histo_cut = histo[(bins_edge > 2.98) & (bins_edge < 3.02)]

popt, pcov = curve_fit(gaussian, bins_edge_cut, histo_cut, bounds=((2500, 3.0019, 0.001), (5155, 3.1, 0.0085)))

i = np.linspace(2.991, 3.015, 1000)

ax1.plot(i, gaussian(i, *popt), 'r')
ax2.plot(i, gaussian(i, *popt), 'r')

plt.text(0.85, 0.5, r'$\mu$ = %.7f $\pm$ %.7f' %(popt[1],pcov[1][1]) , fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='red', pad=8.0), ha='center', va='center')


######################
print('Saving figure as:' + basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/' + 'M_Q_21_fit_gauss' + '.png')
print('\n')
plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/' + 'M_Q_21_fit_gauss' + '.png', format='png')
plt.close()

del fig
del ax1
del ax2




################################################### 14+21 degrees

binning = 10000


fig = plt.figure(figsize=(12,7))

ax1 = fig.add_subplot(111)
ax1.hist(data_14_21_degrees['M_Q'][condition_mass_14_21], bins=binning, weights=None, histtype='step', align='mid', orientation='vertical', color='b', label = 'M/Q')

ax1.set_ylabel(r'counts', fontsize=20)
ax1.set_xlabel(r'$\left(\frac{M}{Q}\right)$', fontsize=20)
ax1.grid(True)

plt.suptitle(r'Mass over Q      14$\degree$+21$\degree$', fontsize=18, x=0.4, y=0.94)

plt.gca().set_xticks(np.arange(70.0, 180.0, 10.0), minor=True)
ax1.set_xlim([2.6, 3.6])
ax1.set_ylim([0.0, 9000])
ax1.xaxis.grid(True)
ax1.legend(loc=2, fontsize = 12)
plt.text(0.9, 0.3, 'Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr>=0', fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='blue', pad=8.0), ha='center', va='center')

# Create a set of inset Axes: these should fill the bounding box allocated to
# them.
ax2 = plt.axes([0,0,1,1])
# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax1, [0.75,0.7,0.3,0.4])
ax2.set_axes_locator(ip)
# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
mark_inset(ax1, ax2, loc1=2, loc2=4, fc="none", ec='0.5')

# The data into the ax2
ax2.hist(data_14_21_degrees['M_Q'][condition_mass_14_21], bins=binning, weights=None, histtype='step', align='mid', orientation='vertical', color='b', label = 'M/Q')

ax2.set_xlim([2.985, 3.02])
ax2.set_ylim([4100, 8400])
ax2.grid(True, which='both')

####### Fit a gaussian in the zoom
def gaussian(x, a, mean, sigma):
    return a * np.exp(-((x - mean)**2 / (2 * sigma**2)))

#Evaluate the histogram
histo, bins_edge = np.histogram(data_14_21_degrees['M_Q'][condition_mass_14_21], bins=binning)

#plt.bar(bins_edge[:-1], histo, width=bins_edge[2]-bins_edge[1])
bins_edge = bins_edge[:-1]

bins_edge_cut = bins_edge[(bins_edge > 2.98) & (bins_edge < 3.02)]
histo_cut = histo[(bins_edge > 2.98) & (bins_edge < 3.02)]

popt, pcov = curve_fit(gaussian, bins_edge_cut, histo_cut, bounds=((4500, 3.0014, 0.001), (8100, 3.1, 0.0083)))

i = np.linspace(2.991, 3.011, 1000)

ax1.plot(i, gaussian(i, *popt), 'r')
ax2.plot(i, gaussian(i, *popt), 'r')

plt.text(0.85, 0.5, r'$\mu$ = %.7f $\pm$ %.7f' %(popt[1],pcov[1][1]) , fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='red', pad=8.0), ha='center', va='center')


######################
print('Saving figure as:' + basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/' + 'M_Q_14_21_fit_gauss' + '.png')
print('\n')
plt.savefig(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/' + 'M_Q_14_21_fit_gauss' + '.png', format='png')
plt.close()

del fig
del ax1
del ax2




'''
---------------------------------------------------- M_Q in each MW_Nr --------------------------------------------------------
'''

condition_MW_14 = ((data_14_degrees['Xf'][:] > -1500) & (data_14_degrees['Yf'][:] > -1500)
                & (data_14_degrees['Yf'][:] > -110) & (data_14_degrees['Yf'][:] < 50)
                & (data_14_degrees['Pf'][:] > -100) & (data_14_degrees['Pf'][:] < 100)
                & (data_14_degrees['M'][:] < 180) & (data_14_degrees['M'][:] > 70)
                & (data_14_degrees['M_Q'][:] < 4) & (data_14_degrees['M_Q'][:] > 2.25))

condition_MW_21 = ((data_21_degrees['Xf'][:] > -1500) & (data_21_degrees['Yf'][:] > -1500)
                & (data_21_degrees['Yf'][:] > -110) & (data_21_degrees['Yf'][:] < 50)
                & (data_21_degrees['Pf'][:] > -100) & (data_21_degrees['Pf'][:] < 100)
                & (data_21_degrees['M'][:] < 180) & (data_21_degrees['M'][:] > 70)
                & (data_21_degrees['M_Q'][:] < 4) & (data_21_degrees['M_Q'][:] > 2.25))

condition_MW_14_21 = ((data_14_21_degrees['Xf'][:] > -1500) & (data_14_21_degrees['Yf'][:] > -1500)
                & (data_14_21_degrees['Yf'][:] > -110) & (data_14_21_degrees['Yf'][:] < 50)
                & (data_14_21_degrees['Pf'][:] > -100) & (data_14_21_degrees['Pf'][:] < 100)
                & (data_14_21_degrees['M'][:] < 180) & (data_14_21_degrees['M'][:] > 70)
                & (data_14_21_degrees['M_Q'][:] < 4) & (data_14_21_degrees['M_Q'][:] > 2.25))


##################################################### 14 degrees

for i in range(int(min(data_14_degrees['MW_Nr'][:])), int(max(data_14_degrees['MW_Nr'][:]))+1):
    MW_ch = i

    M_Q_with_ch_MWNr_14 = Plotter([data_14_degrees['M_Q'][condition_MW_14 & (data_14_degrees['MW_Nr'][:]==MW_ch)]]) #Create the base with the variables in a object
    M_Q_with_ch_MWNr_14.SetFigSize(12,7)
    M_Q_with_ch_MWNr_14.SetBinX(1000)
    M_Q_with_ch_MWNr_14.SetFigTitle(r'M_Q with MW_Nr = %i        14$\degree$' %MW_ch, 20)
    M_Q_with_ch_MWNr_14.SetLabelX('M_Q', 20)
    M_Q_with_ch_MWNr_14.SetLabelY('counts', 20)
    M_Q_with_ch_MWNr_14.SetSizeTicksX(10)
    M_Q_with_ch_MWNr_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr=%i' %MW_ch)
    M_Q_with_ch_MWNr_14.Histo_1D() #Draw it

    ######### Save and show the created figure
    M_Q_with_ch_MWNr_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_Q_per_MWNr/14degrees/')
    M_Q_with_ch_MWNr_14.SaveFig('M_Q_with_ch_%i_MWNr_14' %MW_ch)
    M_Q_with_ch_MWNr_14.Show(1) #show during 1 seconds, the close authomatically
    M_Q_with_ch_MWNr_14.Close() #close all windows, axes and figures running backend
    del M_Q_with_ch_MWNr_14 #erase M_Q_with_ch_MWNr_14 (is an object)



##################################################### 21 degrees
for i in range(int(min(data_21_degrees['MW_Nr'][:])), int(max(data_21_degrees['MW_Nr'][:]))+1):
    MW_ch = i

    M_Q_with_ch_MWNr_21 = Plotter([data_21_degrees['M_Q'][condition_MW_21 & (data_21_degrees['MW_Nr'][:]==MW_ch)]]) #Create the base with the variables in a object
    M_Q_with_ch_MWNr_21.SetFigSize(12,7)
    M_Q_with_ch_MWNr_21.SetBinX(1000)
    M_Q_with_ch_MWNr_21.SetFigTitle(r'M_Q with MW_Nr = %i        21$\degree$' %MW_ch, 20)
    M_Q_with_ch_MWNr_21.SetLabelX('M_Q', 20)
    M_Q_with_ch_MWNr_21.SetLabelY('counts', 20)
    M_Q_with_ch_MWNr_21.SetSizeTicksX(10)
    M_Q_with_ch_MWNr_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr=%i' %MW_ch)
    M_Q_with_ch_MWNr_21.Histo_1D() #Draw it

    ######### Save and show the created figure
    M_Q_with_ch_MWNr_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_Q_per_MWNr/21degrees/')
    M_Q_with_ch_MWNr_21.SaveFig('M_Q_with_ch_%i_MWNr_21' %MW_ch)
    M_Q_with_ch_MWNr_21.Show(1) #show during 1 seconds, the close authomatically
    M_Q_with_ch_MWNr_21.Close() #close all windows, axes and figures running backend
    del M_Q_with_ch_MWNr_21 #erase M_Q_with_ch_MWNr_14 (is an object)



##################################################### 14+21 degrees

for i in range(int(min(data_14_21_degrees['MW_Nr'][:])), int(max(data_14_21_degrees['MW_Nr'][:]))+1):
    MW_ch = i

    M_Q_with_ch_MWNr_14_21 = Plotter([data_14_21_degrees['M_Q'][condition_MW_14_21 & (data_14_21_degrees['MW_Nr'][:]==MW_ch)]]) #Create the base with the variables in a object
    M_Q_with_ch_MWNr_14_21.SetFigSize(12,7)
    M_Q_with_ch_MWNr_14_21.SetBinX(1000)
    M_Q_with_ch_MWNr_14_21.SetFigTitle(r'M_Q with MW_Nr = %i        14$\degree$+21$\degree$' %MW_ch, 20)
    M_Q_with_ch_MWNr_14_21.SetLabelX('M_Q', 20)
    M_Q_with_ch_MWNr_14_21.SetLabelY('counts', 20)
    M_Q_with_ch_MWNr_14_21.SetSizeTicksX(10)
    M_Q_with_ch_MWNr_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.25<M_Q<4 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr=%i' %MW_ch)
    M_Q_with_ch_MWNr_14_21.Histo_1D() #Draw it

    ######### Save and show the created figure
    M_Q_with_ch_MWNr_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_Q_per_MWNr/14+21degrees/')
    M_Q_with_ch_MWNr_14_21.SaveFig('M_Q_with_ch_%i_MWNr_14_21' %MW_ch)
    M_Q_with_ch_MWNr_14_21.Show(1) #show during 1 seconds, the close authomatically
    M_Q_with_ch_MWNr_14_21.Close() #close all windows, axes and figures running backend
    del M_Q_with_ch_MWNr_14_21 #erase M_Q_with_ch_MWNr_14_21 (is an object)




'''
---------------------------------------------------- M_Q in each MW_Nr gaussian fit --------------------------------------------------------
'''

##################################################### 14 degrees

for i in range(int(min(data_14_degrees['MW_Nr'][:])), int(max(data_14_degrees['MW_Nr'][:]))+1):
    MW_ch = i
    binning = 200
    M_Q_with_ch_MWNr_fit_14 = Plotter([data_14_degrees['M_Q'][condition_MW_14 & (data_14_degrees['M_Q'][:]>2.8) & (data_14_degrees['M_Q'][:]<3.2) & (data_14_degrees['MW_Nr'][:]==MW_ch)]]) #Create the base with the variables in a object
    M_Q_with_ch_MWNr_fit_14.SetFigSize(12,7)
    M_Q_with_ch_MWNr_fit_14.SetBinX(binning)
    M_Q_with_ch_MWNr_fit_14.SetFigTitle(r'M_Q with MW_Nr = %i        14$\degree$' %MW_ch, 20)
    M_Q_with_ch_MWNr_fit_14.SetLabelX('M_Q', 20)
    M_Q_with_ch_MWNr_fit_14.SetLabelY('counts', 20)
    M_Q_with_ch_MWNr_fit_14.SetSizeTicksX(10)
    M_Q_with_ch_MWNr_fit_14.SetLimX((2.8,3.2))
    M_Q_with_ch_MWNr_fit_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.8<M_Q<3.2 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr=%i' %MW_ch)
    M_Q_with_ch_MWNr_fit_14.Histo_1D() #Draw it

    ####### Fit a gaussian in the zoom
    def gaussian(x, a, mean, sigma):
        return a * np.exp(-((x - mean)**2 / (2 * sigma**2)))

    #Evaluate the histogram
    histo, bins_edge = np.histogram(data_14_degrees['M_Q'][condition_MW_14 & (data_14_degrees['M_Q'][:]>2.8) & (data_14_degrees['M_Q'][:]<3.2) & (data_14_degrees['MW_Nr'][:]==MW_ch)], bins=binning)
    bins_edge = bins_edge[:-1]

    try:
        popt, pcov = curve_fit(gaussian, bins_edge, histo, bounds=((min(histo), 2.9, 0.001), (max(histo)+max(histo)*0.005, 3.1, 0.0081)))
        i = np.linspace(2.98, 3.02, 1000)
        plt.plot(i, gaussian(i, *popt), 'r')
        plt.text(0.85, 0.5, r'$\mu$ = %.7f $\pm$ %.7f' %(popt[1],pcov[1][1]) , fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='red', pad=8.0), ha='center', va='center')
    except:
        None

    ######### Save and show the created figure
    M_Q_with_ch_MWNr_fit_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_Q_per_MWNr_fit_gauss/14degrees/')
    M_Q_with_ch_MWNr_fit_14.SaveFig('M_Q_with_ch_%i_MWNr_fit_14' %MW_ch)
    M_Q_with_ch_MWNr_fit_14.Show(1) #show during 1 seconds, the close authomatically
    M_Q_with_ch_MWNr_fit_14.Close() #close all windows, axes and figures running backend
    del M_Q_with_ch_MWNr_fit_14 #erase M_Q_with_ch_MWNr_14 (is an object)
    del histo
    del bins_edge




##################################################### 21 degrees

for i in range(int(min(data_21_degrees['MW_Nr'][:])), int(max(data_21_degrees['MW_Nr'][:]))+1):
    MW_ch = i
    binning = 200
    M_Q_with_ch_MWNr_fit_21 = Plotter([data_21_degrees['M_Q'][condition_MW_21 & (data_21_degrees['M_Q'][:]>2.8) & (data_21_degrees['M_Q'][:]<3.2) & (data_21_degrees['MW_Nr'][:]==MW_ch)]]) #Create the base with the variables in a object
    M_Q_with_ch_MWNr_fit_21.SetFigSize(12,7)
    M_Q_with_ch_MWNr_fit_21.SetBinX(binning)
    M_Q_with_ch_MWNr_fit_21.SetFigTitle(r'M_Q with MW_Nr = %i        21$\degree$' %MW_ch, 20)
    M_Q_with_ch_MWNr_fit_21.SetLabelX('M_Q', 20)
    M_Q_with_ch_MWNr_fit_21.SetLabelY('counts', 20)
    M_Q_with_ch_MWNr_fit_21.SetSizeTicksX(10)
    M_Q_with_ch_MWNr_fit_21.SetLimX((2.8,3.2))
    M_Q_with_ch_MWNr_fit_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.8<M_Q<3.2 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr=%i' %MW_ch)
    M_Q_with_ch_MWNr_fit_21.Histo_1D() #Draw it

    ####### Fit a gaussian in the zoom
    def gaussian(x, a, mean, sigma):
        return a * np.exp(-((x - mean)**2 / (2 * sigma**2)))

    #Evaluate the histogram
    histo, bins_edge = np.histogram(data_21_degrees['M_Q'][condition_MW_21 & (data_21_degrees['M_Q'][:]>2.8) & (data_21_degrees['M_Q'][:]<3.2) & (data_21_degrees['MW_Nr'][:]==MW_ch)], bins=binning)
    bins_edge = bins_edge[:-1]

    try:
        popt, pcov = curve_fit(gaussian, bins_edge, histo, bounds=((min(histo), 2.999, 0.003), (max(histo)+max(histo)*0.01, 3.005, 0.009)))
        i = np.linspace(2.98, 3.02, 1000)
        plt.plot(i, gaussian(i, *popt), 'r')
        plt.text(0.85, 0.5, r'$\mu$ = %.7f $\pm$ %.7f' %(popt[1],pcov[1][1]) , fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='red', pad=8.0), ha='center', va='center')
    except:
        None

    ######### Save and show the created figure
    M_Q_with_ch_MWNr_fit_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_Q_per_MWNr_fit_gauss/21degrees/')
    M_Q_with_ch_MWNr_fit_21.SaveFig('M_Q_with_ch_%i_MWNr_fit_21' %MW_ch)
    M_Q_with_ch_MWNr_fit_21.Show(1) #show during 1 seconds, the close authomatically
    M_Q_with_ch_MWNr_fit_21.Close() #close all windows, axes and figures running backend
    del M_Q_with_ch_MWNr_fit_21 #erase M_Q_with_ch_MWNr_21 (is an object)
    del histo
    del bins_edge



##################################################### 14+21 degrees

for i in range(int(min(data_14_21_degrees['MW_Nr'][:])), int(max(data_14_21_degrees['MW_Nr'][:]))+1):
    MW_ch = i
    binning = 200
    M_Q_with_ch_MWNr_fit_14_21 = Plotter([data_14_21_degrees['M_Q'][condition_MW_14_21 & (data_14_21_degrees['M_Q'][:]>2.8) & (data_14_21_degrees['M_Q'][:]<3.2) & (data_14_21_degrees['MW_Nr'][:]==MW_ch)]]) #Create the base with the variables in a object
    M_Q_with_ch_MWNr_fit_14_21.SetFigSize(12,7)
    M_Q_with_ch_MWNr_fit_14_21.SetBinX(binning)
    M_Q_with_ch_MWNr_fit_14_21.SetFigTitle(r'M_Q with MW_Nr = %i        14$\degree$+21$\degree$' %MW_ch, 20)
    M_Q_with_ch_MWNr_fit_14_21.SetLabelX('M_Q', 20)
    M_Q_with_ch_MWNr_fit_14_21.SetLabelY('counts', 20)
    M_Q_with_ch_MWNr_fit_14_21.SetSizeTicksX(10)
    M_Q_with_ch_MWNr_fit_14_21.SetLimX((2.8,3.2))
    M_Q_with_ch_MWNr_fit_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M<180 \n 2.8<M_Q<3.2 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500 \n MW_Nr=%i' %MW_ch)
    M_Q_with_ch_MWNr_fit_14_21.Histo_1D() #Draw it

    ####### Fit a gaussian in the zoom
    def gaussian(x, a, mean, sigma):
        return a * np.exp(-((x - mean)**2 / (2 * sigma**2)))

    #Evaluate the histogram
    histo, bins_edge = np.histogram(data_14_21_degrees['M_Q'][condition_MW_14_21 & (data_14_21_degrees['M_Q'][:]>2.8) & (data_14_21_degrees['M_Q'][:]<3.2) & (data_14_21_degrees['MW_Nr'][:]==MW_ch)], bins=binning)
    bins_edge = bins_edge[:-1]

    try:
        popt, pcov = curve_fit(gaussian, bins_edge, histo, bounds=((min(histo), 2.9, 0.001), (max(histo)+max(histo)*0.005, 3.1, 0.0081)))
        i = np.linspace(2.98, 3.02, 1000)
        plt.plot(i, gaussian(i, *popt), 'r')
        plt.text(0.85, 0.5, r'$\mu$ = %.7f $\pm$ %.7f' %(popt[1],pcov[1][1]) , fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='red', pad=8.0), ha='center', va='center')
    except:
        None

    ######### Save and show the created figure
    M_Q_with_ch_MWNr_fit_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/M_Q_per_MWNr_fit_gauss/14+21degrees/')
    M_Q_with_ch_MWNr_fit_14_21.SaveFig('M_Q_with_ch_%i_MWNr_fit_14_21' %MW_ch)
    M_Q_with_ch_MWNr_fit_14_21.Show(1) #show during 1 seconds, the close authomatically
    M_Q_with_ch_MWNr_fit_14_21.Close() #close all windows, axes and figures running backend
    del M_Q_with_ch_MWNr_fit_14_21 #erase M_Q_with_ch_MWNr_14_21 (is an object)
    del histo
    del bins_edge



'''
---------------------------------------------------------- M_Q vs MW_Nr ---------------------------------------------------------------
'''

################################################################## 14 degrees
M_Q_vs_MWNr_14 = Plotter([data_14_degrees['MW_Nr'][condition_MW_14], data_14_degrees['M_Q'][condition_MW_14]]) #Create the base with the variables in a object
M_Q_vs_MWNr_14.SetFigSize(12,7)
M_Q_vs_MWNr_14.SetBinX(18)
M_Q_vs_MWNr_14.SetBinY(10000)
M_Q_vs_MWNr_14.SetFigTitle(r'M_Q:MW_Nr        14$\degree$', 20)
M_Q_vs_MWNr_14.SetLabelX('MultiWire section', 20)
M_Q_vs_MWNr_14.SetLabelY(r'M_Q', 20)
M_Q_vs_MWNr_14.SetSizeTicksX(10)
M_Q_vs_MWNr_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M>180 \n 2.24<M_Q<4.0 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_Q_vs_MWNr_14.SetLimY((2.8,3.2))
M_Q_vs_MWNr_14.SetGrid("y")
M_Q_vs_MWNr_14.Histo_2D() #Draw it

######### Save and show the created figure
M_Q_vs_MWNr_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_Q_vs_MWNr_14.SaveFig('M_Q_vs_MWNr_14')
M_Q_vs_MWNr_14.Show(1) #show during 1 seconds, the close authomatically
M_Q_vs_MWNr_14.Close() #close all windows, axes and figures running backend
del M_Q_vs_MWNr_14 #erase M_Q_vs_MWNr_14 (is an object)


################################################################## 21 degrees
M_Q_vs_MWNr_21 = Plotter([data_21_degrees['MW_Nr'][condition_MW_21], data_21_degrees['M_Q'][condition_MW_21]]) #Create the base with the variables in a object
M_Q_vs_MWNr_21.SetFigSize(12,7)
M_Q_vs_MWNr_21.SetBinX(18)
M_Q_vs_MWNr_21.SetBinY(10000)
M_Q_vs_MWNr_21.SetFigTitle(r'M_Q:MW_Nr        21$\degree$', 20)
M_Q_vs_MWNr_21.SetLabelX('MultiWire section', 20)
M_Q_vs_MWNr_21.SetLabelY(r'M_Q', 20)
M_Q_vs_MWNr_21.SetSizeTicksX(10)
M_Q_vs_MWNr_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M>180 \n 2.24<M_Q<4.0 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_Q_vs_MWNr_21.SetLimY((2.8,3.2))
M_Q_vs_MWNr_21.SetGrid("y")
M_Q_vs_MWNr_21.Histo_2D() #Draw it

######### Save and show the created figure
M_Q_vs_MWNr_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_Q_vs_MWNr_21.SaveFig('M_Q_vs_MWNr_21')
M_Q_vs_MWNr_21.Show(1) #show during 1 seconds, the close authomatically
M_Q_vs_MWNr_21.Close() #close all windows, axes and figures running backend
del M_Q_vs_MWNr_21 #erase M_Q_vs_MWNr_21 (is an object)


################################################################## 14+21 degrees
M_Q_vs_MWNr_14_21 = Plotter([data_14_21_degrees['MW_Nr'][condition_MW_14_21], data_14_21_degrees['M_Q'][condition_MW_14_21]]) #Create the base with the variables in a object
M_Q_vs_MWNr_14_21.SetFigSize(12,7)
M_Q_vs_MWNr_14_21.SetBinX(18)
M_Q_vs_MWNr_14_21.SetBinY(10000)
M_Q_vs_MWNr_14_21.SetFigTitle(r'M_Q:MW_Nr        14$\degree$+21$\degree$', 20)
M_Q_vs_MWNr_14_21.SetLabelX('MultiWire section', 20)
M_Q_vs_MWNr_14_21.SetLabelY(r'M_Q', 20)
M_Q_vs_MWNr_14_21.SetSizeTicksX(10)
M_Q_vs_MWNr_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M>180 \n 2.24<M_Q<4.0 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_Q_vs_MWNr_14_21.SetLimY((2.8,3.2))
M_Q_vs_MWNr_14_21.SetGrid("y")
M_Q_vs_MWNr_14_21.Histo_2D() #Draw it

######### Save and show the created figure
M_Q_vs_MWNr_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_Q_vs_MWNr_14_21.SaveFig('M_Q_vs_MWNr_14_21')
M_Q_vs_MWNr_14_21.Show(1) #show during 1 seconds, the close authomatically
M_Q_vs_MWNr_14_21.Close() #close all windows, axes and figures running backend
del M_Q_vs_MWNr_14_21 #erase M_Q_vs_MWNr_14_21 (is an object)




'''
---------------------------------------------------------- M vs MW_Nr ---------------------------------------------------------------
'''

################################################################## 14 degrees
M_vs_MWNr_14 = Plotter([data_14_degrees['MW_Nr'][condition_MW_14], data_14_degrees['M'][condition_MW_14]]) #Create the base with the variables in a object
M_vs_MWNr_14.SetFigSize(12,7)
M_vs_MWNr_14.SetBinX(18)
M_vs_MWNr_14.SetBinY(1000)
M_vs_MWNr_14.SetFigTitle(r'M:MW_Nr        14$\degree$', 20)
M_vs_MWNr_14.SetLabelX('MultiWire section', 20)
M_vs_MWNr_14.SetLabelY(r'M', 20)
M_vs_MWNr_14.SetSizeTicksX(10)
M_vs_MWNr_14.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M>180 \n 2.24<M_Q<4.0 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_vs_MWNr_14.SetLimY((90.0,160.0))
M_vs_MWNr_14.SetGrid("y")
M_vs_MWNr_14.Histo_2D() #Draw it

######### Save and show the created figure
M_vs_MWNr_14.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_vs_MWNr_14.SaveFig('M_vs_MWNr_14')
M_vs_MWNr_14.Show(1) #show during 1 seconds, the close authomatically
M_vs_MWNr_14.Close() #close all windows, axes and figures running backend
del M_vs_MWNr_14 #erase M_vs_MWNr_14 (is an object)


################################################################## 21 degrees
M_vs_MWNr_21 = Plotter([data_21_degrees['MW_Nr'][condition_MW_21], data_21_degrees['M'][condition_MW_21]]) #Create the base with the variables in a object
M_vs_MWNr_21.SetFigSize(12,7)
M_vs_MWNr_21.SetBinX(18)
M_vs_MWNr_21.SetBinY(1000)
M_vs_MWNr_21.SetFigTitle(r'M:MW_Nr        21$\degree$', 20)
M_vs_MWNr_21.SetLabelX('MultiWire section', 20)
M_vs_MWNr_21.SetLabelY(r'M', 20)
M_vs_MWNr_21.SetSizeTicksX(10)
M_vs_MWNr_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M>180 \n 2.24<M_Q<4.0 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_vs_MWNr_21.SetLimY((90.0,160.0))
M_vs_MWNr_21.SetGrid("y")
M_vs_MWNr_21.Histo_2D() #Draw it

######### Save and show the created figure
M_vs_MWNr_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_vs_MWNr_21.SaveFig('M_vs_MWNr_21')
M_vs_MWNr_21.Show(1) #show during 1 seconds, the close authomatically
M_vs_MWNr_21.Close() #close all windows, axes and figures running backend
del M_vs_MWNr_21 #erase M_vs_MWNr_21 (is an object)


################################################################## 14+21 degrees
M_vs_MWNr_14_21 = Plotter([data_14_21_degrees['MW_Nr'][condition_MW_14_21], data_14_21_degrees['M'][condition_MW_14_21]]) #Create the base with the variables in a object
M_vs_MWNr_14_21.SetFigSize(12,7)
M_vs_MWNr_14_21.SetBinX(18)
M_vs_MWNr_14_21.SetBinY(1000)
M_vs_MWNr_14_21.SetFigTitle(r'M:MW_Nr        14$\degree$+21$\degree$', 20)
M_vs_MWNr_14_21.SetLabelX('MultiWire section', 20)
M_vs_MWNr_14_21.SetLabelY(r'M', 20)
M_vs_MWNr_14_21.SetSizeTicksX(10)
M_vs_MWNr_14_21.SetBoxText('Selection:\n Z>0 \n Zi>0 \n 70<M>180 \n 2.24<M_Q<4.0 \n -100<Pf<100 \n -110<Yf<50 \n  Xf>-1500')
M_vs_MWNr_14_21.SetLimY((90.0,160.0))
M_vs_MWNr_14_21.SetGrid("y")
M_vs_MWNr_14_21.Histo_2D() #Draw it

######### Save and show the created figure
M_vs_MWNr_14_21.SetOutDir(basepath + 'Modules/' + MODULE_name + '/Outputfiles/Figures/')
M_vs_MWNr_14_21.SaveFig('M_vs_MWNr_14_21')
M_vs_MWNr_14_21.Show(1) #show during 1 seconds, the close authomatically
M_vs_MWNr_14_21.Close() #close all windows, axes and figures running backend
del M_vs_MWNr_14_21 #erase M_vs_MWNr_14_21 (is an object)
