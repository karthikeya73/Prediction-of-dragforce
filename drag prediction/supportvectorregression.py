# -*- coding: utf-8 -*-
"""SupportVectorRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rX-FQkckEP5In3kYIPq0XyLPUKowwBpM
"""

import pandas as pd

import numpy as np

df=pd.read_excel('dataset 2c.xlsx','Sheet1')


df['vehicle_tag']=(df['vehicle_tag']-df['vehicle_tag'].mean())/(df['vehicle_tag'].std())
df['inter-vehiclar distance']=(df['inter-vehiclar distance']-df['inter-vehiclar distance'].mean())/(df['inter-vehiclar distance'].std())
#df['a']=np.square(df['vehicle_tag'])
#df['b']=np.square(df['vehicle_tag'])

# df['c']=np.dot(np.square(df['inter-vehiclar distance']),np.transpose(df['inter-vehiclar distance']))

#df=pd.concat([df,df,df,df,df])
#df['c'].unique()

X=df.iloc[:,:-1].values
Y=df.iloc[:,-1]
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 0)

from sklearn.svm import SVR
regressor = SVR(kernel='linear')
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
y_pred_train = regressor.predict(X_train)

# print r_square_score
from sklearn.metrics import r2_score
print("R_square score: ", r2_score(y_test,y_pred))

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

print("Mean squared error : ",mean_squared_error(y_test,y_pred))
print("Mean abosolute error : ",mean_absolute_percentage_error(y_test,y_pred))

y_test









