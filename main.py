

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