import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.loadtxt('Data1.txt')
dataset = pd.DataFrame({'No.':data[:]})
dataset.sort_values('No.',inplace=True)

dataset.hist(bins=50) # Exploring data
plt.show()
dataset.boxplot(vert=False)
plt.show()

Q1=np.percentile(dataset, [25]) # Calculating Quartiles
Q2=np.percentile(dataset, [50])
Q3=np.percentile(dataset, [75])
Iqr=np.percentile(dataset, [75])-np.percentile(dataset, [25])
print("1st quartile:",Q1,"\n2nd quartile:",Q2,"\n3rd quartile:",Q3)
print("Inter-quartile range:",Iqr)

x1= 1.5 * Iqr   # Calculating Boundary for Outlier
x2= 3 * Iqr     # Calculating Boundary for Extreme Outlier

w1= Q1 - x1     #Setting Outlier Whisker
w2= Q3 + x1

Ew1= Q1 - x2    # Setting Extreme Outlier Whisker
Ew2= Q3 + x2 

o =[] # Outliers points
Eo=[] # Extreme Outlier points
for i in range(len(dataset)):
    if dataset['No.'][i] >= w2 and dataset['No.'][i] <= Ew2:
        o.append(dataset['No.'][i])
    if dataset['No.'][i] <= w1 and dataset['No.'][i] >= Ew1:
        o.append(dataset['No.'][i])
    if dataset['No.'][i] >= Ew2 or dataset['No.'][i] <= Ew1 :
        Eo.append(dataset['No.'][i])
    
print("Outlier points: ", len(o))
print("Extreme Outlier points: ", len(Eo))