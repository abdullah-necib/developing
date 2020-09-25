#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 09:26:38 2020

@author: abdullah
"""

from matplotlib import pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from pandas import read_csv, set_option
from pandas.plotting import scatter_matrix
import wx
import sympy as sy
import numpy as np

filename = 'datasets_228_482_diabetes_with_header.csv'
fpath = '/'.join(__file__.split('/')[:-2])+'/data/'+filename

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None, title='Test')
        pnl = MyPanel(self)
        self.SetInitialSize(pnl.initialsize)
        self.Show()

class MyPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111,autoscale_on=True)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.draw()
        
    def draw(self):
        names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
        set_option('precision',3)
        data = read_csv(fpath, names=names, header=0)
        scatter_matrix(data)
        plt.show()
        self.initialsize = self.canvas.GetSize()


if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame()
    app.MainLoop()