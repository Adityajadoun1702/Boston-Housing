

import pandas as pd
import numpy as np

df=pd.read_csv('advertising.csv')
X=df.iloc[:,:-1].values
Y=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)



from sklearn .linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)

Y_pred=regressor.predict(X_test)

import matplotlib.pyplot as plt
Y_train_pred=regressor.predict(X_train)
residuals=Y_train-Y_train_pred
plt.scatter(Y_train_pred,residuals)
plt.axhline(y=0,color='red')
plt.show()

from statsmodels.stats.stattools import durbin_watson
dw=durbin_watson(residuals)
print(dw)

plt.plot(residuals)
plt.axhline(y=0,color='red')
plt.show()

import seaborn as sns
sns.histplot(residuals,kde=True)

plt.show()

import scipy.stats as stats

stats.probplot(residuals, dist="norm", plot=plt)

plt.show()

X_pd = df.drop('Sales', axis=1)
corr = X_pd.corr()

plt.figure(figsize=(10,8))

sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.show()


from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = pd.DataFrame()

vif["Feature"] = X_pd.columns

vif["VIF"] = [
    variance_inflation_factor(X_pd.values, i)
    for i in range(X.shape[1])
]

print(vif)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

regressor.fit(X_train,Y_train)
regressor.predict(X_test)

plt.scatter(Y_test, Y_pred)