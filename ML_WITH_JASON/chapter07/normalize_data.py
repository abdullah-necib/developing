#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pandas import read_csv
from sklearn.preprocessing import Normalizer
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
X = array[:,0:8]
Y = array[:,8]

scaler = Normalizer().fit(X)
rescaledX =scaler.transform(X)
set_printoptions(precision=3)
print(rescaledX[0:5,:])
# write_log(str(rescaledX))
# write_log(str(dataframe[0:5]))
result =0
for i in rescaledX[0]:
    result += i**2
print(result)