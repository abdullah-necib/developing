#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler
from numpy import set_printoptions

filename = 'datasets_228_482_diabetes_with_header.csv'
fpath = '/'.join(__file__.split('/')[:-2])+'/data/'+filename
output_file = 'output.log'

def write_log(data,outfile=output_file,format='a'):
    import datetime
    length =int( (len(__file__)-len(str(datetime.datetime.now())))/2)
    x = length * '-' if length <=0 else ''
    y = length * '-' if length > 0 else ''
    with open(outfile,format) as f:

        f.writelines('{0} {1} {2}\n{3} at {4} {5}\n'\
                     .format(10*'-'+x,__file__,10*'-'+x,
                             10*'-'+y,datetime.datetime.now(),10*'-'+y))
        f.writelines(str(data))
        f.writelines('\n-------------------------------------- DONE ---------------------------------\n\n')




names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(fpath, names=names, header=0)
array = dataframe.values
# print(dataframe)
# print(array)
X = array[:,0:8]
# print(X)
# Y = array[:,8]

scaler = MinMaxScaler(feature_range=(0,1))
rescaledX =scaler.fit_transform(X)
set_printoptions(precision=3)
print(rescaledX[0:5,:])
print()
description = dataframe.describe()
print(description)
write_log(str(description))
