# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:53:40 2024

@author: Dell
"""

import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

x=[2,3,5,7,8,9,10]
y=[4,5,7,8,1,2,3]
classes=[0,1,0,0,1,1,0]

data=list(zip(x,y))

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(data,classes)

new_x=4
new_y=7
new_p=[(new_x,new_y)]

pred=knn.predict(new_p)
print(pred)