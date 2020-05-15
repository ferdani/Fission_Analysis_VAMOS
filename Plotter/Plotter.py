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
        self.ScaleX = None; self.ScaleY = None;
        self.SizeTicksX = None; self.SizeTicksY = None; self.SizeTicksZ = None;

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

    def SetSizeTicksX(self, sizex):
        '''set ticks's size in X axis'''
        self.SizeTicksX = sizex

    def SetSizeTicksY(self, sizey):
        '''set ticks's size in Y axis'''
        self.SizeTicksY = sizey

    def SetSizeTicksZ(self, sizez):
        '''set ticks's size in Z axis'''
        self.SizeTicksZ = sizez


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

        # Plot histogram
        if self.bin_x:
            hist, bins = np.histogram(self.X_Variable, bins=self.bin_x, weights=w)
        else:
            hist, bins = np.histogram(self.X_Variable, weights=w)

        width = 1.0 * (bins[1] - bins[0])
        center = (bins[:-1] + bins[1:]) / 2

        plt.grid(True, which="major", ls="-", axis='both')

        if self.FigTitle: ax.set_title(self.FigTitle, fontsize=self.SizeTitle)

        ax.autoscale(enable=True, axis='both', tight=False)

        plt.bar(center, hist, align='center', width=width, linewidth=0.5, edgecolor='k', color='b')

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

        plt.grid(True, which="major", ls="-", axis='y')

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

        plt.grid(True, which="major", ls="-", axis='both')

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
        plt.pcolormesh(xedges,yedges,Hmasked, cmap='jet')

        cbar = plt.colorbar()
        cbar.ax.set_ylabel('Counts')

        plt.grid(True, which="both", ls="-")

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
        axScatter.grid(True, which="major", ls="-", axis='both')

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

        return fig
