# -*- coding: utf-8 -*-
"""PolynomialRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lqHHl-ZzrTqWjDyO_fgnYOD6gz8kySLz
"""

import pandas as pd

import numpy as np

datas=pd.read_excel('dataset 2c.xlsx','Sheet1')
datas['vehicle_tag']=(datas['vehicle_tag']-datas['vehicle_tag'].min())/(datas['vehicle_tag'].max()-datas['vehicle_tag'].min())
datas['inter-vehiclar distance']=(datas['inter-vehiclar distance']-datas['inter-vehiclar distance'].min())/(datas['inter-vehiclar distance'].max()-datas['inter-vehiclar distance'].min())

X = datas.iloc[:, :-1].values
y = datas.iloc[:, -1].values

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
 
poly = PolynomialFeatures(degree = 5)
X_poly = poly.fit_transform(X)
 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size = 0.1)

poly.fit(X_poly, y)
lin2 = LinearRegression()
lin2.fit(X_poly, y)

regressor=lin2

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

y_pred

