# -*- coding: utf-8 -*-
"""Larvae data Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZX7NmGwVhoW2SffNZh9ChPvMAySVuoXw
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
a=np.genfromtxt('california_housing_train.csv',delimiter=',',skip_header=1)
print(a.shape)

import matplotlib.pyplot as plt
# %matplotlib inline
import pandas as pd

#data=pd.read_csv("0509 5^1 Treatment Record Data.csv")
#print(data)
Result=pd.DataFrame(a)
Result.head()
#Result["Unnamed: 7"]
Result.plot(kind='bar',title='Result',figsize=[100,50])