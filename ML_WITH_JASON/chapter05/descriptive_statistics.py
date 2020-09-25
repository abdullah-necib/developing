#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 07:23:07 2020

@author: abdullah
"""

from pandas import read_csv
from pandas import set_option

filename = 'datasets_228_482_diabetes_with_header.csv'
fpath = '/'.join(__file__.split('/')[:-2])+'/data/'+filename
# print(fpath)

names =['preg','plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(fpath,names= names,header=0)
peek = data.head(20)
print(peek) # peek 20 line only to print
print(data.shape) #this for db deminsions
types = data.dtypes
print(types)
set_option('display.width',100)
set_option('precision',3)
description = data.describe()
print(description)
class_counts = data.groupby('class').size()
# class_test = data.groupby('mass').sum()
print(class_counts)
# print(class_test)

correlation = data.corr(method='pearson')
print(correlation)
print('>>>>>>>>>> now print skew  >>>>>>>>>>>')
print(data.skew())