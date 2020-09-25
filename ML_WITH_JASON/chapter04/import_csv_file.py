#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:44:53 2020

@author: abdullah
"""

import csv
import numpy as np
from numpy import loadtxt

# =============================================================================
# import csv from python - normally
# =============================================================================

print('---------- import from python ------------------')
filename1 = 'datasets_228_482_diabetes_with_header.csv'
raw_data = open(filename1, 'r')
print('type of open() is %s' % type(raw_data))
reader = csv.reader(raw_data, delimiter=',',quoting=csv.QUOTE_NONE)
x = list(reader)
data = np.array(x)
print(data.shape)
print(data[0])
print(data[1])
print('---------- import from python using with statement------------------')
with open(filename1, 'r') as f:
    x = list(csv.reader(f))
print(np.array(x).shape)

# =============================================================================
# import csv file from numpy
# =============================================================================
print('---------- import from numpy ------------------')
filename = 'datasets_228_482_diabetes.csv'
raw_data = open(filename, 'r')
print('type of open() is %s' % type(raw_data))
try:
    # here i had to remove the header to make it work
    data = loadtxt(raw_data,delimiter=',')
    print(data.shape)
    print(type(data))
except Exception as err:
    print(err)
print(data)
# =============================================================================
# import csv file from urlopen
# =============================================================================
print('---------- import from numpy using urlopen() ------------------')
from urllib.request import urlopen
url = 'https://goo.g1/vhm1eU'

try:
    raw_data = urlopen(url)
    dataset = loadtxt(raw_data)
    print(data.shape)
except Exception as err:
    print(err)

# =============================================================================
# import csv file with pandas
# =============================================================================
from pandas import read_csv
print('---------- import from numpy using pandas.read_csv() ------------------')
names =['preg','plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(filename1,names= names)
print(filename1)
print(data.shape)
print(data)
print(type(data))