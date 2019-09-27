import pandas
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


f1 = open('Data3-1.txt', 'r') 
w1 = f1.readlines()
for line in w1:
    w1 = line.split(',')
w1 = [float(x) for x in w1]
f1.close()

f2 = open('Data3-2.txt', 'r') 
w2 = f2.readlines()
for line in w2:
    w2 = line.split(',')
w2 = [float(x) for x in w2]
f2.close()

f3 = open('Data3-3.txt', 'r') 
w3 = f3.readlines()
for line in w3:
    w3 = line.split(',')
w3 = [float(x) for x in w3]
f3.close()

data = {
    'Data1': w1,
    'Data2': w2,
    'Data3': w3,
    }
from itertools import combinations
from scipy.stats import ttest_ind #Built-in function for one tail
print('1st  vs 2nd       P-value')
for list1, list2 in combinations(data.keys(), 2):
    t, p = ttest_ind(data[list1], data[list2])
    print(list1, list2, p)

df = pandas.DataFrame(data)
kwargs = dict(alpha=0.8, bins=100)
plt.hist(df['Data1'], **kwargs, color='g', label='D1',density=True, histtype='bar', stacked=True)
plt.hist(df['Data2'], **kwargs, color='b', label='D2',density=True, histtype='bar', stacked=True)
plt.hist(df['Data3'], **kwargs, color='r', label='D3',density=True, histtype='bar', stacked=True)
plt.show()

#%% Tailored function Comparing two lists for two tails

def Calculate_Pvalue(w1,w2):
    w1Mean, w2Mean = np.mean(w1), np.mean(w2)
    w1Std, w2Std = np.sqrt(np.var(w1)), np.sqrt(np.var(w2)) 
    n = len(w2)
    Mu0 = w1Mean
    x = w2Mean
    segma = w1Std
    print('Mean 1: %f' %w1Mean,' Mean 2: %f'%w2Mean)
    print('Std  1: %f' %w1Std , '  Std  2: %f' %w2Std)
    
    z0 = (x-Mu0)/(segma/np.sqrt(n))
    P_value = 2*(1-norm.cdf(abs(z0)))
    C_value = norm.ppf(P_value)
    print('P-value for Data is: %f' %P_value)
    print('with Critical Value: %f' %C_value)
    if P_value <= 0.05:
        print("we reject null hypothesis")
    else:
        print("we accept null hypothesis")
    kwargs = dict(alpha=0.8, bins=50)
    plt.hist(w1, **kwargs, color='b', label='D1',density=True, histtype='bar', stacked=True)
    plt.hist(w2, **kwargs, color='r', label='D2',density=True, histtype='bar', stacked=True)
    plt.show()

#%% Try here!!

#Calculate_Pvalue(w1,w2)
