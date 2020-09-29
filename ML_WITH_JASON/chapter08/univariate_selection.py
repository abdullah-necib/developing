from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest, chi2

filename = 'datasets_228_482_diabetes_with_header.csv'
fpath = '/'.join(__file__.split('/')[:-2])+'/data/'+filename
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(fpath, names=names, header=0)
array = dataframe.values
x = array[:,0:8]
y = array[:,8]
# feature extraction
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(x,y)
# summurize score
set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(x)
print(features[0:5,:])