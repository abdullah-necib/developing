#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 09:26:38 2020

@author: abdullah
"""

from matplotlib import pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from pandas import read_csv
import wx
import sympy as sym
import numpy as np

filename = 'datasets_228_482_diabetes_with_header.csv'
fpath = '/'.join(__file__.split('/')[:-2])+'/data/'+filename

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None, title='Test')
        pnl = MyPanel(self)
        # self.SetInitialSize(pnl.initialsize)
        self.Show()

class MyPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111,autoscale_on=True)
        # self.subPnl1 = wx.Panel(self)
        self.canvas = FigureCanvas(self, -1, self.figure)
        # self.sizer.Add(self.subPnl1,1,wx.ALL, 5)

        # self.subPnl2 = wx.Panel(self)
        # cmb = wx.ComboBox(self.subPnl2, value='density', choices=['density', 'box'])
        # self.sizer.Add(self.subPnl2,1,wx.ALL,5)
        #
        # self.SetSizer(self.sizer)
        self.draw()
        
    def draw(self):
        axis_font = {'fontname': 'Arial', 'size': '6'}
        names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
        data = read_csv(fpath, names=names, header=0)
        data.plot(kind='density', subplots=True, layout=(3, 3), sharex=False)
        self.axes.plot(plt.show())
        self.initialsize = self.canvas.GetSize()


if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame()
    app.MainLoop()