from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest, chi2

filename = 'datasets_228_482_diabetes_with_header.csv'
fpath = '/'.join(__file__.split('/')[:-2])+'/data/'+filename
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(fpath, names=names, header=0)