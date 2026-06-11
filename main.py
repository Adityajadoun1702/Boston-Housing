import pandas as pd
import numpy as np

df=pd.read_csv('Boston.csv')
X=df.iloc[:,1:-1].values
Y=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)

Y_pred=regressor.predict(X_test)

import matplotlib.pyplot as plt
plt.scatter(Y_test, Y_pred)
from sklearn.metrics import r2_score, mean_absolute_error
r2=r2_score(Y_pred,Y_test)
mae = mean_absolute_error(Y_test, Y_pred)
print(r2)
print(mae)



