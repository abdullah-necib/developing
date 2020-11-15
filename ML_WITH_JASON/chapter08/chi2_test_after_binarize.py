import pandas
from pandas import read_csv
from sklearn.preprocessing import LabelBinarizer

filename = 'datasets_228_482_diabetes_with_header.csv'
fpath = '/'.join(__file__.split('/')[:-2])+'/data/'+filename
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(fpath, names=names, header=0)
array = dataframe.values
plas_ar = array[:, 1]
class_ar = array[:, 8]

# this is not what is done
plas_df = pandas.crosstab(dataframe['plas'],dataframe['class'])
print(plas_df)
y= LabelBinarizer().fit_transform(class_ar)

# for i in range(len(plas_ar)):
#     print(f'{plas_ar[i]}\t {class_ar[i]}\t{y[i]}')