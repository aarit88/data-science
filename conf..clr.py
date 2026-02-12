# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:40:22 2024

@author: Dell
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score,mean_absoulte_error
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

diabetes=datasets.load_diabetes()
diabetes
print(diabetes.DESCR)
diabetes.feature_names

X = diabetes.data
Y = diabetes.target

print(X.shape)
print(Y.shape)
Y
train_x, test_x, train_y, test_y = train_test_split(X,Y,test_size=0.3,random_state=99)
train_x.shape, train_y.shape
le = LinearRegression()
le.fit(train_x,train_y)
y_pred = le.predict(test_x)
print(y_pred)
result = pd.DataFrame({'Actual': test_y, 'Predict' : y_pred})
result

print('coefficient', le.coef_)
print('intercept', le.intercept_)

print(mean_squared_error(test_y,y_pred))
print(mean_absolute_error(test_y,y_pred))

print(r2_score(test_y,y_pred))

plt.plot(test_y)
plt.plot(y_pred)
plt.show()

'''plt.scatter(train_x, train_y,color='g')
plt.plot(test_x, y_pred,color='k')

plt.show()'''