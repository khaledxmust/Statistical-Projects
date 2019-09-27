import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dice = pd.DataFrame({'Rolls':[1,2,3,4,5,6]})
D1 = pd.DataFrame(np.random.randint(1,7,size=(1000, 1)),columns=['Dice'])
D2 = pd.DataFrame(np.random.randint(1,7,size=(1000, 1)),columns=['Dice'])
D1.hist(bins=100)
plt.title("Dice One 1000x")
D2.hist(bins=100)
plt.title("Dice Two 1000x")

Dav = pd.DataFrame({'Dice':[]})

for i in range(1000):
    x = sum(D1.iloc[i],D2.iloc[i])/2
    Dav = Dav.append(x)

Dav.hist(bins=100)
plt.title("Rolling two dice 1000x")
plt.show()
#print(Dav)

Mean =Dav.mean()
print('Mean= %f' %Mean)

Var = Dav.var()
print('Variance= %f' %Var)

#%% Creating 10 Dice 1000x

Dx = pd.DataFrame()
for i in range(10):
    x = pd.DataFrame(np.random.randint(1,7,size=(1000, 1)))
    Dx = x.join(Dx, lsuffix=i+1, rsuffix=i)
    
Davx = pd.DataFrame({'Avarage':[]})
for i in range(1000):
    x=0
    for z in range(10):
        x = x + Dx.iloc[i][z]
    Sx = x/10
    Davx = Davx.append({'Avarage': Sx}, ignore_index=True)
#print(Dx)
#print(Davx)
Davx.hist(bins=100)
plt.title("Rolling 10 dice 1000x")
plt.show()

Mean =Davx.mean()
print('Mean= %f' %Mean)

Var = Davx.var()
print('Variance= %f' %Var)