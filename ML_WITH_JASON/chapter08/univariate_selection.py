import matplotlib.pyplot as pyplot
import numpy as np
import pandas as pd
from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest, chi2
import random as rd
from scipy.stats import norm,chi2_contingency
from scipy.stats import chi2 as kai


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
print(fit.pvalues_)
features = fit.transform(x)
# with open('selctKBest.log','a') as f:
#     f.write(str(fit.scores_) + '\n')
#     for i in features:
#         f.write(str(i)+'\n')

def analyse_chi2_Col(col_name='plas',margins= True):
    
                                                                                    
    col_class_crosstable =\
        pd.crosstab(dataframe[col_name],dataframe['class'],margins=margins)
    
    # =========================================================================
    # my own analysis     
    # =========================================================================
    result = np.array(col_class_crosstable)
    # =====================================================================
    # result array consist of col0 = Obs of 0, col1 = obs of 1,
    # col2 = col0+col1
    # col3 = Exp0, col4 = Exp1, col5 = (col0-col3)**2  / col3, 
    # col6 = (col1-col4)**2 / col4
    # =====================================================================
    # add empty cols to the array
    for i in range(4):
        result = np.column_stack((result,np.zeros(len(result))))
    # calculate the new columns and add it
    for i in result:
        Obs0 = i[0]
        Obs1 = i[1]
        Exp0 = i[2] * result[-1][0]/  result[-1][2] 
        Exp1 = i[2] * result[-1][1]/  result[-1][2]
        Dev0 = (1/Exp0)*(Obs0-Exp0)**2
        Dev1 = (1/Exp1)*(Obs1-Exp1)**2
        i[3],i[4],i[5],i[6] = Exp0,Exp1,Dev0,Dev1
    
    k0 = 0
    k1 = 0
    for i in result:
        k0 += i[-2]
        k1 += i[-1]
    
    stat, p, dof, expected = chi2_contingency(col_class_crosstable)

    # print(col_class_crosstable)
    print('My Summary for ',col_name)    
    print(f'Chai2 for o is: {k0:.3f} , for 1 is {k1:.3f} and sum is: {k0+k1:.3f}')  
    print(f'dof is: {dof}')
    print('Probability is: {}'.format(1-kai(dof).cdf(k0+k1)))
    
    print(40*'-')
    
    confidence_interval = 0.95
    print ("Chi-Square Statistic value = {}".format(stat))
    print ("P - Value = {}".format(p))
    print('df is:{}'.format(dof))
    alpha = 1.0 - confidence_interval
    if p <= alpha:
        print('Dependent (reject H0)')
    else:
	      print('Independent (fail to reject H0)')
    return expected


def analyse_chi2_Col_without_margins(col_name='plas', margins=False):
    col_class_crosstable = \
        pd.crosstab(dataframe[col_name], dataframe['class'], margins=margins)
    # =========================================================================
    # my own analysis
    # =========================================================================
    result = np.array(col_class_crosstable)
    sum_array = result.sum(axis=0)
    # print(sum_array)
    # =====================================================================
    # result array consist of col0 = Obs of 0, col1 = obs of 1,
    # col2 = col0+col1
    # col3 = Exp0, col4 = Exp1, col5 = (col0-col3)**2  / col3,
    # col6 = (col1-col4)**2 / col4
    # =====================================================================
    # add empty cols to the array
    for i in range(5):
        result = np.column_stack((result, np.zeros(len(result))))
    # calculate the new columns and add it
    for i in result:
        i[2]=i[0] + i[1]
        Obs0 = i[0]
        Obs1 = i[1]
        Exp0 = i[2] * sum_array[0] / (sum_array[0]+sum_array[1])
        Exp1 = i[2] * sum_array[1] / (sum_array[0]+sum_array[1])
        Dev0 = (1 / Exp0) * (Obs0 - Exp0) ** 2
        Dev1 = (1 / Exp1) * (Obs1 - Exp1) ** 2
        i[3], i[4], i[5], i[6] = Exp0, Exp1, Dev0, Dev1

    k0 = 0
    k1 = 0
    for i in result:
        k0 += i[-2]
        k1 += i[-1]

    stat, p, dof, expected = chi2_contingency(col_class_crosstable)

    # print(col_class_crosstable)
    print('My Summary for ', col_name)
    print(f'Chai2 for o is: {k0:.3f} , for 1 is {k1:.3f} and sum is: {k0 + k1:.3f}')
    print(f'dof is: {dof}')
    print('Probability is: {}'.format(1 - kai(dof).cdf(k0 + k1)))

    print(40 * '-')

    confidence_interval = 0.95
    print("Chi-Square Statistic value = {}".format(stat))
    print("P - Value = {}".format(p))
    print('df is:{}'.format(dof))
    alpha = 1.0 - confidence_interval
    if p <= alpha:
        print('Dependent (reject H0)')
    else:
        print('Independent (fail to reject H0)')
    return expected
    

for i in names:
    if i != names[-1]:
        print(50*'=')
        analyse_chi2_Col_without_margins(i)
        print(50*'=')

# analyse_chi2_Col_without_margins('plas')