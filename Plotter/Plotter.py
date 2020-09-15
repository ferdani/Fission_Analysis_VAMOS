#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:01:00 2020

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

Plotter class -- Here is a powerful tool to develop plots for the different modules.
The plot is an object created by the Plotter class with the variables that one wants to represent
and in which different functions will be applied to represent them.
As it is an object, one can get and set properties of the object.

For example: Histo_example = Plotter([[X],[Y]). Now, over this object one can use predefined functions
to represent this variables, one by one or both together.

The predefined functions are:

--> Histo_1D(*weights)
--> Bar_diagram()
--> Bar_diagram_2D()
--> Histo_2D(*weights)
--> Histo_2D_mountain(*weights)
--> Histo_2D_mountain(*weights)
--> ScatterXYpoints_histograms_X_Y()

"""

import sys, os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.ticker import NullFormatter

class Plotter(object):
    """
    Creates a Plot-object with different properties.

    """

    def __init__(self,*args):
        """
        The Plotter's init function. The *args are the variables (x,y,z) one wants to represent. The maximum is three variables.
        The order of the variables is important, the first variable will be X_Variable and so on.

        Work in progress:
        Use **kargs to clarify things and interconnect better the functions

        """
        self.outdir = None
        self.FigSize = (10,7) #by default
        self.bin_x = None; self.bin_y = None; self.bin_x = None
        self.NticksX = None; self.NticksY = None; self.NticksZ = None
        self.FigTitle = None; self.SizeTitle = 15 #by default
        self.xmin = None; self.xmax = None; self.ymin = None; self.ymax = None; self.zmin = None; self.zmax = None
        self.LabelX = None; self.LabelY = None; self.LabelZ = None
        self.SizeLabelX = None; self.SizeLabelY = None; self.SizeLabelZ = None
        self.ScaleX = None; self.ScaleY = None; self.ScaleZ = None; self.Gamma = None
        self.SizeTicksX = None; self.SizeTicksY = None; self.SizeTicksZ = None;
        self.BoxText = None; self.Grid = None; self.lasso = None; self.cutg = None;
        self.x_range = None; self.binning = None;

        #Case 1:
        if len(args)==1 and type(args[0])==list and len(args[0])>0:
            plotList = args[0]
            if len(plotList) == 1:
                self.X_Variable = plotList[0]
                self.X_Variable = np.array(self.X_Variable)
            elif len(plotList) == 2:
                self.X_Variable = plotList[0]
                self.X_Variable = np.array(self.X_Variable)
                self.Y_Variable = plotList[1]
                self.Y_Variable = np.array(self.Y_Variable)
            elif len(plotList) == 3:
                self.X_Variable = plotList[0]
                self.X_Variable = np.array(self.X_Variable)
                self.Y_Variable = plotList[1]
                self.Y_Variable = np.array(self.Y_Variable)
                self.Z_Variable = plotList[2]
                self.Z_Variable = np.array(self.Z_Variable)
            else:
                raise RuntimeError('Cannot process input arguments {}'.format(plotList))


################################## 'Set' methods

    def SetOutDir(self, outdir):
        '''set the output directory'''
        self.outdir = outdir
        if self.outdir[-1] != '/': outdir += '/'

    def SetFigSize(self, x, y):
        '''set the size of the current figure'''
        self.FigSize = (x,y)

    def SetBinX(self, binx):
        '''set the bin number in X-axis'''
        self.bin_x = binx

    def SetBinY(self, biny):
        '''set the bin number in Y-axis'''
        self.bin_y = biny

    def SetBinZ(self, binz):
        '''set the bin number in Z-axis'''
        self.bin_z = binz

    def SetNticksX(self, Nx):
        '''set the ticks number in X-axis'''
        self.NticksX = Nx

    def SetNticksY(self, Ny):
        '''set the ticks number in Y-axis'''
        self.NticksY = Ny

    def SetNticksZ(self, Nz):
        '''set the ticks number in Z-axis'''
        self.NticksZ = Nz

    def SetFigTitle(self, figtitle, sizetitle):
        '''set the title in the figure'''
        self.FigTitle = figtitle
        self.SizeTitle = sizetitle

    def SetLimX(self, limx):
        '''set the limits in X axis'''
        self.xmin = limx[0]
        self.xmax = limx[1]

    def SetLimY(self, limy):
        '''set the limits in Y axis'''
        self.ymin = limy[0]
        self.ymax = limy[1]

    def SetLimZ(self, limz):
        '''set the limits in Z axis'''
        self.zmin = limz[0]
        self.zmax = limz[1]

    def SetLabelX(self, xlabel, xsizelabel):
        '''set the label under the X axis'''
        self.LabelX = xlabel
        self.SizeLabelX = xsizelabel

    def SetLabelY(self, ylabel, ysizelabel):
        '''set the label under the Y axis'''
        self.LabelY = ylabel
        self.SizeLabelY = ysizelabel

    def SetLabelZ(self, zlabel, zsizelabel):
        '''set the label under the Z axis'''
        self.LabelZ = zlabel
        self.SizeLabelZ = zsizelabel

    def SetScaleX(self, scalex):
        '''set ("linear", "log", "symlog", "logit", ...) scale in X axis'''
        self.ScaleX = scalex

    def SetScaleY(self, scaley):
        '''set ("linear", "log", "symlog", "logit", ...) scale in Y axis'''
        self.ScaleY = scaley

    def SetScaleZ(self, scalez, *gamma):
        '''set ("Normalize", "LogNorm", "PowerNorm", "SymLogNorm") scale in Z axis'''
        self.ScaleZ = scalez
        if gamma: self.Gamma = gamma[0] #used in PowerNorm

    def SetSizeTicksX(self, sizex):
        '''set ticks's size in X axis'''
        self.SizeTicksX = sizex

    def SetSizeTicksY(self, sizey):
        '''set ticks's size in Y axis'''
        self.SizeTicksY = sizey

    def SetSizeTicksZ(self, sizez):
        '''set ticks's size in Z axis'''
        self.SizeTicksZ = sizez

    def SetBoxText(self, text):
        '''set text in a rectangule inside the plot'''
        self.BoxText = text

    def SetGrid(self, grid):
        '''set grid on X-axis as "x", in Y-axis as "y" or in both as "both" '''
        self.Grid = grid


################################## 'Get' methods

    def GetFigSize(self):
        '''get the size of the current figure'''
        return self.FigSize

    def GetLimX(self):
        '''get the limits in X axis'''
        return (self.xmin, self.xmax)

    def GetLimY(self):
        '''get the limits in Y axis'''
        return (self.ymin, self.ymax)

    def GetLimZ(self):
        '''get the limits in Z axis'''
        return (self.zmin, self.zmax)

    def GetCutg(self):
        '''get the cutg extracted using Lasso'''
        return self.cutg


################################# 'Miscellaneous' methods

    def Show(self, *args):
        '''show the current figure for a moment or permanent'''
        if args:
            time = args[0]
            plt.show(block=False)
            plt.pause(time)
            plt.close()
        else:
            plt.show()

    def Close(self):
        '''close running figure'''
        plt.close()

    def SaveFig(self, figname):
        '''save the currnt figure'''
        if self.outdir:
            print('Saving figure as: ' + self.outdir + figname + '.png')
            print('\n')
            plt.savefig(self.outdir + figname + '.png', format='png')
        else:
            raise RuntimeError('You are trying to save without set a path to save figures. Set one with SetOutDir function')

    def Lasso(self):
        '''Use pointer into figure to select a data region with a lasso, nowadays only works with Histo_2D'''
        self.lasso = True

    def ShowProjectionX(self, y_range, binning):
        '''Show counts projection over X axis in 2d-histogram H in one specific y_range'''

        self.y_range = y_range
        self.binning = binning

        Y_to_hist_values = self.Y_Variable[(self.Y_Variable >= self.y_range[0]) & (self.Y_Variable <= self.y_range[1])]
        index = np.where(self.Y_Variable == Y_to_hist_values[0]) #index where is first element
        X_to_hist_values = self.X_Variable[index[0][0]:len(Y_to_hist_values)+index[0][0]]
        histo_projection, bin_edges = np.histogram(X_to_hist_values, self.binning)

        fig_aux = plt.figure()
        ax_aux = fig_aux.add_subplot(111)
        plt.hist(X_to_hist_values, self.binning)
        ax_aux.set_title('Projection over X in y_range=' + str(self.y_range), fontsize=16)

        return histo_projection_X

    def ShowProjectionY(self, x_range, binning):
        '''Show counts projection over Y axis in 2d-histogram H in one specific x_range'''

        self.x_range = x_range
        self.binning = binning

        X_to_hist_values = self.X_Variable[(self.X_Variable >= self.x_range[0]) & (self.X_Variable <= self.x_range[1])]
        index = np.where(self.X_Variable == X_to_hist_values[0]) #index where is first element
        Y_to_hist_values = self.Y_Variable[index[0][0]:len(X_to_hist_values)+index[0][0]]
        histo_projection, bin_edges = np.histogram(Y_to_hist_values, self.binning)

        fig_aux = plt.figure()
        ax_aux = fig_aux.add_subplot(111)
        plt.hist(Y_to_hist_values, self.binning)
        ax_aux.set_title('Projection over Y in x_range=' + str(self.x_range), fontsize=16)

        return histo_projection_Y


################################# PLOT MODES

    def Histo_1D(self, *weights):
        """Do one dimension histogram.

        Returns a histogram figure that represents the number of counts with bins for X-values.

        Variables:
        -- X_Variable
        -- *weights --> The values of the returned histogram are equal to the sum of the weights belonging to the samples falling into each bin.

        Excepctions:
        The length of weights is not correct

        """
        if weights:
            w = np.array(weights[0]) #the *args can be more than one, for *weights is the same and the first is used
            if len(self.X_Variable) != len(w):
                raise RuntimeError('You are trying to use Histo_1D function with weights with wrong length')
        else:
            w = np.ones(len(self.X_Variable)) #The weight is one

        #create the work space
        fig = plt.figure(figsize=self.FigSize)
        plt.ioff() #inline mode off

        plt.rcParams['agg.path.chunksize'] = 100 #If exist a problem doing zoom is here with chunks. It works with TkAgg matplotlib backend

        ax = fig.add_subplot(111)

        if self.bin_x:
            plt.hist(self.X_Variable, bins=self.bin_x, weights=w, histtype='step', align='mid', orientation='vertical', color='b')
        else:
            plt.hist(self.X_Variable, weights=w, histtype='step', align='mid', orientation='vertical')

        if self.Grid: plt.grid(True, which="major", axis=self.Grid, ls="-")

        if self.FigTitle: ax.set_title(self.FigTitle, fontsize=self.SizeTitle)

        ax.autoscale(enable=True, axis='both', tight=False)

        if self.xmin and self.xmax:
            ax.set_xlim(self.xmin,self.xmax)
        else:
            self.xmin, self.xmax = ax.get_xlim()

        if self.ymin and self.ymax:
            ax.set_ylim(self.ymin,self.ymax)
        else:
            self.ymin, self.ymax = ax.get_ylim()

        if self.NticksX: ax.set_xticks(np.round(np.linspace(self.xmin, self.xmax, self.NticksX), 2))
        if self.NticksY: ax.set_yticks(np.round(np.linspace(self.ymin, self.ymax, self.NticksY), 2))

        if self.LabelX and self.SizeLabelX: ax.set_xlabel(self.LabelX, fontsize=self.SizeLabelX)

        if self.LabelY and self.SizeLabelY:
            ax.set_ylabel(self.LabelY, fontsize=self.SizeLabelY)
        else:
            ax.set_ylabel('Counts', fontsize=15)

        if self.ScaleX: ax.set_xscale(self.ScaleX)
        if self.ScaleY: ax.set_yscale(self.ScaleY)

        if self.SizeTicksX: ax.tick_params(axis='x', labelsize=self.SizeTicksX)
        if self.SizeTicksY: ax.tick_params(axis='y', labelsize=self.SizeTicksY)

        if self.BoxText: plt.text(0.9, 0.8, s=self.BoxText, fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='white', edgecolor='blue', pad=8.0), ha='center', va='center')

        return fig


    def Bar_diagram(self):
        """Do a bar diagram plot.

        Returns a bar diagram that represents the number of counts (Y_Variable) per each (X_Variable) that can be strings or numbers.

        Variables:
        -- X_Variable (Represents the tags)
        -- Y_Variable (Represents the frequency)

        Excepctions:
        None

        """
        #create the work space
        fig = plt.figure(figsize=self.FigSize)
        plt.ioff() #inline mode off

        plt.rcParams['agg.path.chunksize'] = 100 #If exist a problem doing zoom is here with chunks. It works with TkAgg matplotlib backend

        ax = fig.add_subplot(111)

        # Plot the bar diagram (tags, frequency)
        plt.bar(self.X_Variable, self.Y_Variable, linewidth=0.5, edgecolor='k', color='b')

        if self.Grid: plt.grid(True, which="major", axis=self.Grid, ls="-")

        if self.FigTitle: ax.set_title(self.FigTitle, fontsize=self.SizeTitle)

        ax.autoscale(enable=True, axis='both', tight=False)

        if self.ymin and self.ymax:
            ax.set_ylim(self.ymin,self.ymax)
        else:
            self.ymin, self.ymax = ax.get_ylim()

        if self.NticksY: ax.set_yticks(np.round(np.linspace(self.ymin, self.ymax, self.NticksY), 2))

        ax.set_xticklabels(self.X_Variable, fontsize = 12)

        if self.LabelX and self.SizeLabelX: ax.set_xlabel(self.LabelX, fontsize=self.SizeLabelX)

        if self.LabelY and self.SizeLabelY:
            ax.set_ylabel(self.LabelY, fontsize=self.SizeLabelY)
        else:
            ax.set_ylabel('Counts', fontsize=15)

        if self.ScaleY: ax.set_yscale(self.ScaleY)

        if self.SizeTicksX: ax.tick_params(axis='x', labelsize=self.SizeTicksX)
        if self.SizeTicksY: ax.tick_params(axis='y', labelsize=self.SizeTicksY)

        if self.BoxText: plt.text(0.92, 0.8, s=self.BoxText, fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='none', edgecolor='blue', pad=8.0), ha='center', va='center')

        return fig


    def Bar_diagram_2D(self):
        """Do a two dimensions bar diagram.

        This function creates boxes using X values and Y values making a mesh and inside each box using weights (one per box)
        from (left to right) and (bottom to top) creates with color a values-denstiy.
        Each (Xi,Yi) point has got a Zi weight. With a mesh a box around the point (Xi,Yi) is created and inside this box
        the density (Zi) is represented with color.

          |---|---|---|---|---|---|                 Variables:
        30|   |   |   |   |   |   |
          |---|---|---|---|---|---|                 -- X_Variable
        25|   |   |   |   |   |   |                 -- Y_Variable
          |---|---|---|---|---|---|                 -- Z_Variable --> The weights like color in the third dimension
            1   2   3   4   5   6

        Excepctions:
        The length of Z_Variable have to be enough to add a weight per box, in other case a RuntimeError will appear in terminal

        """
        if (len(self.X_Variable)*(len(self.Y_Variable))) != len(self.Z_Variable):
            raise RuntimeError('You are trying to use Bar_diagram_2D function without corrected variable lengths')

        #create the work space
        fig = plt.figure(figsize=self.FigSize)
        plt.ioff() #inline mode off

        plt.rcParams['agg.path.chunksize'] = 100 #If exist a problem doing zoom is here with chunks. It works with TkAgg matplotlib backend

        ax = fig.add_subplot(111)

        #do a meshgrid to build the boxes
        XX,YY = np.meshgrid(self.X_Variable,self.Y_Variable)

        # self.X_Variable and self.Y_Variable are the middle point coordinates of each box. We want the edges of each box
        #Build the vertical edges over X axis (two per box)
        Xedges = np.zeros(len(self.X_Variable)+1)
        Xedges[:-1] = self.X_Variable-((self.X_Variable[1]-self.X_Variable[0])/2.0)
        Xedges[-1] = self.X_Variable[-1] + ((self.X_Variable[1]-self.X_Variable[0])/2.0)
        #Build the horizontal edges over Y axis (two per box)
        Yedges = np.zeros(len(self.Y_Variable)+1)
        Yedges[:-1] = self.Y_Variable-((self.Y_Variable[1]-self.Y_Variable[0])/2.0)
        Yedges[-1] = self.Y_Variable[-1] + ((self.Y_Variable[1]-self.Y_Variable[0])/2.0)

        # It is neccesary to do a histogram 2d introduce one dimension array per coordinate
        Xprime = np.concatenate(XX)
        Yprime = np.concatenate(YY)

        #Build the histogram in two dimensions
        H, xedges, yedges = np.histogram2d(Xprime, Yprime, bins=(Xedges,Yedges), weights=self.Z_Variable)

        # H needs to be transpose
        H = H.T

        Xnew, Ynew = np.meshgrid(xedges, yedges)
        # Mask zeros

        Hmasked = np.ma.masked_where(H==0,H) # Mask pixels with a value of zero

        # Plot 2D histogram using pcolor
        plt.pcolormesh(Xnew,Ynew,Hmasked, cmap='jet')

        cbar = plt.colorbar()
        cbar.ax.set_ylabel('Counts')

        if self.Grid: plt.grid(True, which="major", axis=self.Grid, ls="-")

        if self.FigTitle: ax.set_title(self.FigTitle, fontsize=self.SizeTitle)

        ax.autoscale(enable=True, axis='both', tight=False)

        if self.xmin and self.xmax:
            ax.set_xlim(self.xmin,self.xmax)
        else:
            self.xmin, self.xmax = ax.get_xlim()

        if self.ymin and self.ymax:
            ax.set_ylim(self.ymin,self.ymax)
        else:
            self.ymin, self.ymax = ax.get_ylim()

        if self.NticksX: ax.set_xticks(np.round(np.linspace(self.xmin, self.xmax, self.NticksX), 2))
        if self.NticksY: ax.set_yticks(np.round(np.linspace(self.ymin, self.ymax, self.NticksY), 2))

        if self.LabelX and self.SizeLabelX: ax.set_xlabel(self.LabelX, fontsize=self.SizeLabelX)
        if self.LabelY and self.SizeLabelY: ax.set_ylabel(self.LabelY, fontsize=self.SizeLabelY)

        if self.ScaleX: ax.set_xscale(self.ScaleX)
        if self.ScaleY: ax.set_yscale(self.ScaleY)

        if self.SizeTicksX: ax.tick_params(axis='x', labelsize=self.SizeTicksX)
        if self.SizeTicksY: ax.tick_params(axis='y', labelsize=self.SizeTicksY)

        if self.BoxText: plt.text(0.92, 0.8, s=self.BoxText, fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='none', edgecolor='blue', pad=8.0), ha='center', va='center')

        return fig


    def Histo_2D(self, *weights):
        """Do a two dimensional histogram with density color zones.

        Returns a figure in two dimensions with colors as density function of counts type "jet".
        This function use numpy histogram2d as basic base.
        This function represents the zero values with an empty color (white).
        For each pair of values (X, Y) with the correspondent value (W), the weight. If exist weight, implies that 2d histogram color
        will be this weight and will be represented as a color bar. In other case, the weight is one and the color is directly the density points per bin.

        The same in Root6 with an example:
        TFile *_file0 = TFile::Open("raw_root_files/r0092_000a.root")
        GM -> Draw("Delta:ThetaLdeg", "Z > 0.0 && Delta > 0.0", "col")

        Variables:
        -- X_Variable
        -- Y_Variable
        -- *weights --> The values of the returned histogram are equal to the sum of the weights belonging to the samples falling into each bin.

        Excepctions:
        If the length of Variables is not enough a RuntimeError will appear in terminal.

        Work in progress:
        density : bool, optional
            If False, the default, returns the number of samples in each bin.
            If True, returns the probability density function at the bin, bin_count / sample_count / bin_area.

        """
        if len(self.X_Variable) != len(self.Y_Variable):
            raise RuntimeError('You are trying to use Histo_2D_color function with different variables sizes')

        if weights:
            w = np.array(weights[0]) #the *args can be more than one, for *weights is the same and the first is used
            if len(self.X_Variable) != len(self.Y_Variable) != len(w):
                raise RuntimeError('You are trying to use Histo_2D function with weights with wrong length')
        else:
            w = np.ones(len(self.X_Variable)) #The weight is one

        # Make histogram stuff with numpy in 2d
        if self.bin_x and self.bin_y:
            H, xedges, yedges = np.histogram2d(self.X_Variable, self.Y_Variable, bins=(self.bin_x,self.bin_y), weights=w)
        else:
            H, xedges, yedges = np.histogram2d(self.X_Variable, self.Y_Variable, weights=w)

        # H needs to be rotated and flipped
        H = np.rot90(H)
        H = np.flipud(H)

        # Mask zeros, mask pixels with a value of zero
        Hmasked = np.ma.masked_where(H==0,H)

        # Create the work space
        fig = plt.figure(figsize=self.FigSize)
        plt.ioff() #inline mode off
        ax = fig.add_subplot(111)

        plt.rcParams['agg.path.chunksize'] = 100 #If exist a problem doing zoom is here with chunks. It works with TkAgg matplotlib backend

        # Plot 2D histogram using pcolormesh
        if self.ScaleZ:
            if self.ScaleZ == 'Normalization':
                plt.pcolormesh(xedges,yedges,Hmasked, cmap='jet', norm=colors.Normalize(vmin=-1, vmax=1))
            elif self.ScaleZ == 'SymLogNorm':
                plt.pcolormesh(xedges,yedges,Hmasked, cmap='jet', norm=colors.SymLogNorm(linthresh=0.03, linscale=0.03, vmin=-1.0, vmax=1.0))
            elif self.ScaleZ == 'LogNorm':
                plt.pcolormesh(xedges,yedges,Hmasked, cmap='jet', norm=colors.LogNorm(vmin=Hmasked.min(), vmax=Hmasked.max()))
            elif self.ScaleZ == 'PowerNorm':
                plt.pcolormesh(xedges,yedges,Hmasked, cmap='jet', norm=colors.PowerNorm(gamma=self.Gamma))
        else: plt.pcolormesh(xedges,yedges,Hmasked, cmap='jet')

        cbar = plt.colorbar()
        cbar.ax.set_ylabel('Counts')

        if self.Grid: plt.grid(True, which="major", axis=self.Grid, ls="-")

        if self.FigTitle: ax.set_title(self.FigTitle, fontsize=self.SizeTitle)

        ax.autoscale(enable=True, axis='both', tight=False)

        if self.xmin and self.xmax:
            ax.set_xlim(self.xmin,self.xmax)
        else:
            self.xmin, self.xmax = ax.get_xlim()

        if self.ymin and self.ymax:
            ax.set_ylim(self.ymin,self.ymax)
        else:
            self.ymin, self.ymax = ax.get_ylim()

        if self.NticksX: ax.set_xticks(np.round(np.linspace(self.xmin, self.xmax, self.NticksX), 2))
        if self.NticksY: ax.set_yticks(np.round(np.linspace(self.ymin, self.ymax, self.NticksY), 2))

        if self.LabelX and self.SizeLabelX: ax.set_xlabel(self.LabelX, fontsize=self.SizeLabelX)
        if self.LabelY and self.SizeLabelY: ax.set_ylabel(self.LabelY, fontsize=self.SizeLabelY)

        if self.ScaleX: ax.set_xscale(self.ScaleX)
        if self.ScaleY: ax.set_yscale(self.ScaleY)

        if self.SizeTicksX: ax.tick_params(axis='x', labelsize=self.SizeTicksX)
        if self.SizeTicksY: ax.tick_params(axis='y', labelsize=self.SizeTicksY)

        if self.BoxText: plt.text(0.92, 0.8, s=self.BoxText, fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='none', edgecolor='blue', pad=8.0), ha='center', va='center')

        if self.lasso:
            pts = ax.scatter(self.X_Variable, self.Y_Variable, s=1, c='black', alpha=0.0)
            selector = SelectFromCollection(ax, pts)

            def accept(event):
                if event.key == "enter":
                    #print("Selected points:")
                    #print(selector.xys[selector.ind])
                    selector.disconnect()
                    if self.FigTitle: ax.set_title(self.FigTitle, fontsize=self.SizeTitle, color='k')
                    else: ax.set_title("")
                    cutg_0_1 = selector.xys[selector.ind].data #the data inside lasso
                    cutg_0 = np.array([i[0] for i in cutg_0_1]) #the first data column (x-position)

                    # Extract the indices in original Branch to apply as a cut in all branches. (with one branch is sufficient, same lenght)
                    xsorted = np.argsort(self.X_Variable)
                    ypos = np.searchsorted(self.X_Variable[xsorted], cutg_0)
                    cutg_indices = xsorted[ypos]

                    woduplicates = list(set(cutg_indices)) #if one cross lasso, one point will be repeated. With set a new array is created without duplicated values
                    woduplicates.sort() #it is neccesary order it
                    np.asarray(woduplicates) #preference to work with arrays

                    self.cutg = woduplicates #Now this is a cutg to apply to each branch

            ax.set_title("Press enter to accept selected points", fontsize=25, color='r')
            fig.canvas.mpl_connect("key_press_event", accept)

        return fig


    def Histo_2D_mountain(self, *weights):
        """Do a two dimensional histogram like a mountain, with the third dimesion as density.

        Returns a figure in three dimensions with blocks of bins like columns painted in colors as density variable.
        This function use numpy histogram2d as basic base.
        For each pair of values (X, Y) with the correspondent value (W), the weight. If exist weight, implies that 2d histogram color
        will be this weight and will be represented as a color bar. In other case, the weight is one and the color is directly the density points per bin.

        Variables:
        -- X_Variable
        -- Y_Variable
        -- *weights --> The values of the returned histogram are equal to the sum of the weights belonging to the samples falling into each bin.

        Excepctions:
        If the length of Variables is not enough a RuntimeError will appear in terminal.

        Work in progress:
        Mask pixels with a value of zero as white zones.

        """
        if len(self.X_Variable) != len(self.Y_Variable):
            raise RuntimeError('You are trying to use Histo_2D_mountain function with different variables sizes')

        if weights:
            w = np.array(weights[0]) #the *args can be more than one, for *weights is the same and the first is used
            if len(self.X_Variable) != len(self.Y_Variable) != len(w):
                raise RuntimeError('You are trying to use Histo_2D_mountain function with weights with wrong length')
        else:
            w = np.ones(len(self.X_Variable)) #The weight is one

        # Create the work space
        fig = plt.figure(figsize=self.FigSize)
        plt.ioff() #inline mode off
        ax = fig.add_subplot(111, projection='3d')

        # Make histogram stuff with numpy in 2d
        if self.bin_x and self.bin_y:
            H, xedges, yedges = np.histogram2d(self.X_Variable, self.Y_Variable, bins=(self.bin_x,self.bin_y), weights=w)
        else:
            H, xedges, yedges = np.histogram2d(self.X_Variable, self.Y_Variable, weights=w)

        #make a mesh between points
        xpos, ypos = np.meshgrid(xedges[:-1]+xedges[1:], yedges[:-1]+yedges[1:])

        # H needs to be rotated and flipped
        H = np.rot90(H)
        H = np.flipud(H)

        xpos = xpos.flatten()/2.
        ypos = ypos.flatten()/2.
        zpos = np.zeros_like(xpos)

        dx = xedges [1] - xedges [0]
        dy = yedges [1] - yedges [0]
        dz = H.flatten()

        cmap = plt.cm.get_cmap('jet') # Get desired colormap - you can change this!
        max_height = np.max(dz)   # get range of colorbars so we can normalize
        min_height = np.min(dz)
        # scale each z to [0,1], and get their rgb values
        rgba = [cmap((k-min_height)/max_height) for k in dz]

        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=rgba, zsort='average')

        if self.FigTitle: ax.set_title(self.FigTitle, fontsize=self.SizeTitle)

        ax.autoscale(enable=True, axis='both', tight=False)

        if self.xmin and self.xmax:
            ax.set_xlim(self.xmin,self.xmax)
        else:
            self.xmin, self.xmax = ax.get_xlim()

        if self.ymin and self.ymax:
            ax.set_ylim(self.ymin,self.ymax)
        else:
            self.ymin, self.ymax = ax.get_ylim()

        if self.NticksX: ax.set_xticks(np.round(np.linspace(self.xmin, self.xmax, self.NticksX), 2))
        if self.NticksY: ax.set_yticks(np.round(np.linspace(self.ymin, self.ymax, self.NticksY), 2))

        if self.LabelX and self.SizeLabelX: ax.set_xlabel(self.LabelX, fontsize=self.SizeLabelX)
        if self.LabelY and self.SizeLabelY: ax.set_ylabel(self.LabelY, fontsize=self.SizeLabelY)
        if self.LabelZ and self.SizeLabelZ:
            ax.set_zlabel(self.LabelZ, fontsize=self.SizeLabelZ)
        else:
            ax.set_zlabel('Counts', fontsize=15)

        if self.ScaleX: ax.set_xscale(self.ScaleX)
        if self.ScaleY: ax.set_yscale(self.ScaleY)

        if self.SizeTicksX: ax.tick_params(axis='x', labelsize=self.SizeTicksX)
        if self.SizeTicksY: ax.tick_params(axis='y', labelsize=self.SizeTicksY)

        if self.BoxText: plt.text(0.92, 0.8, s=self.BoxText, fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='none', edgecolor='blue', pad=8.0), ha='center', va='center')

        return fig


    def ScatterXYpoints_histograms_X_Y(self):
        """Do a boxes plot in X and Y with density color (Z_values).

        The idea is return a histogram in two dimensions with X_values and Y_values, to plot easy each box,
        and add the color as a weight with the third variable Z_values.

        Excepctions:
        If the length of Variables is not enough a RuntimeError will appear in terminal.

        """
        if len(self.X_Variable) != len(self.Y_Variable):
            raise RuntimeError('You are trying to use ScatterXYpoints_histograms_X_Y function with different variables sizes')

        # Create the work space
        fig = plt.figure(figsize=self.FigSize) #recomended figsize=(10, 10)
        plt.ioff() #inline mode off

        plt.rcParams['agg.path.chunksize'] = 1000 #If exist a problem doing zoom is here with chunks. It works with TkAgg matplotlib backend

        # definitions for the axes to build the plot-zones
        left, width = 0.1, 0.62
        bottom, height = 0.1, 0.62
        bottom_h = left_h = left + width + 0.02
        # definition of the rectangule-places for plot: 1) Scatter 2) X-Histogram  3) Y-Histogram
        rect_scatter = [left, bottom, width, height]
        rect_histx = [left, bottom_h, width, 0.2]
        rect_histy = [left_h, bottom, 0.2, height]

        # define the axes for each plot-zone
        axScatter = plt.axes(rect_scatter)
        axHistx = plt.axes(rect_histx)
        axHisty = plt.axes(rect_histy)

        # no labels in the histograms
        nullfmt = NullFormatter()
        axHistx.xaxis.set_major_formatter(nullfmt)
        axHisty.yaxis.set_major_formatter(nullfmt)

        # the scatter plot:
        axScatter.scatter(self.X_Variable, self.Y_Variable, marker='o', c='g', edgecolor='k', linewidth=0.3)
        #Grid on scatter plot activated
        if self.Grid: axScatter.grid(True, which="major", axis=self.Grid, ls="-")

        if self.FigTitle: fig.suptitle(self.FigTitle, fontsize=self.SizeTitle)

        if self.xmin and self.xmax:
            axScatter.set_xlim(self.xmin,self.xmax)
        else:
            self.xmin, self.xmax = axScatter.get_xlim()
            axScatter.set_xlim((self.xmin+(self.xmin*0.1), self.xmax+(self.xmax*0.1)))

        if self.ymin and self.ymax:
            axScatter.set_ylim(self.ymin,self.ymax)
        else:
            self.ymin, self.ymax = axScatter.get_ylim()
            axScatter.set_ylim((self.ymin-(self.ymin*0.1), self.ymax+(self.ymax*0.1)))

        if self.NticksX: axScatter.set_xticks(np.round(np.linspace(self.xmin, self.xmax, self.NticksX), 2))
        if self.NticksY: axScatter.set_yticks(np.round(np.linspace(self.ymin, self.ymax, self.NticksY), 2))

        if self.LabelX and self.SizeLabelX: axScatter.set_xlabel(self.LabelX, fontsize=self.SizeLabelX)
        if self.LabelY and self.SizeLabelY: axScatter.set_ylabel(self.LabelY, fontsize=self.SizeLabelY)

        if self.ScaleX: axScatter.set_xscale(self.ScaleX)
        if self.ScaleY: axScatter.set_yscale(self.ScaleY)

        if self.SizeTicksX: axScatter.tick_params(axis='x', labelsize=self.SizeTicksX)
        if self.SizeTicksY: axScatter.tick_params(axis='y', labelsize=self.SizeTicksY)

        if self.bin_x:
            axHistx.hist(self.X_Variable, bins=self.bin_x, orientation='vertical', facecolor='g', edgecolor='k', linewidth=0.3, histtype='bar')
        else:
            axHistx.hist(self.X_Variable, orientation='vertical', facecolor='g', edgecolor='k', linewidth=0.3, histtype='bar')

        if self.bin_y:
            axHisty.hist(self.Y_Variable, bins=self.bin_y, orientation='horizontal', facecolor='g', edgecolor='k', linewidth=0.3, histtype='bar')
        else:
            axHisty.hist(self.Y_Variable, orientation='horizontal', facecolor='g', edgecolor='k', linewidth=0.3, histtype='bar')

        if self.BoxText: plt.text(0.92, 0.8, self.BoxText, fontsize=12, color='black', transform=plt.gcf().transFigure, bbox=dict(facecolor='none', edgecolor='blue', pad=8.0), ha='center', va='center')

        return fig



##########################################################################################################################################################################################################

"""
===================
Dani_Lasso based on Matplotlib Selector Demo: https://matplotlib.org/3.2.2/gallery/widgets/lasso_selector_demo_sgskip.html
===================

Interactively selecting data points with the lasso tool.

This examples plots a scatter plot. You can then select a few points by drawing
a lasso loop around the points on the graph. To draw, just click
on the graph, hold, and drag it around the points you need to select.
"""

from matplotlib.widgets import LassoSelector
from matplotlib.path import Path

class SelectFromCollection:
    """Select indices from a matplotlib collection using `LassoSelector`.

    Selected indices are saved in the `ind` attribute. This tool fades out the
    points that are not part of the selection (i.e., reduces their alpha
    values). If your collection has alpha < 1, this tool will permanently
    alter the alpha values.

    Note that this tool selects collection objects based on their *origins*
    (i.e., `offsets`).

    Parameters
    ----------
    ax : :class:`~matplotlib.axes.Axes`
        Axes to interact with.

    collection : :class:`matplotlib.collections.Collection` subclass
        Collection you want to select from.

    alpha_other : 0 <= float <= 1
        To highlight a selection, this tool sets all selected points to an
        alpha value of 1 and non-selected points to `alpha_other`.
    """

    def __init__(self, ax, collection, alpha_other=0.0):
        self.canvas = ax.figure.canvas
        self.collection = collection
        self.alpha_other = alpha_other

        self.xys = collection.get_offsets()
        self.Npts = len(self.xys)

        # Ensure that we have separate colors for each object
        self.fc = collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('Collection must have a facecolor')
        elif len(self.fc) == 1:
            self.fc = np.tile(self.fc, (self.Npts, 1))

        self.lasso = LassoSelector(ax, onselect=self.onselect)
        self.ind = []

    def onselect(self, verts):
        path = Path(verts)
        self.ind = np.nonzero(path.contains_points(self.xys))[0]
        self.fc[:, -1] = self.alpha_other
        self.fc[self.ind, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()

    def disconnect(self):
        self.lasso.disconnect_events()
        self.fc[:, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()
