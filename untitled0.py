# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:24:14 2024

@author: Dell
"""

import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans

iris=datasets.load_iris()
X=iris.data
Y=iris.target

estimarors=[("k_means_iris_8",KMeans(n_clusters=8))]
