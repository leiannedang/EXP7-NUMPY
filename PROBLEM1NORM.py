
"""
Created on Sat Nov 16 12:15:26 2019

@author: Angela Leenzae Edang
"""

''' Normalization is one of the most basic preprocessing techniques in data 
analytics. In this problem, create a random 5x5 ndarray and store it to 
variable X. Normalize X. Save your normalized ndarray as X_normalized.npy '''

import numpy as np

X = np.random.random((5,5))
print('Random Array:\n')
print(X)
print('\n')

mean = X.mean() #mean of the array
std = X.std() #standard deviation of the array

norm = np.divide((np.subtract(X, mean)), std) #normalization 
norm_conv = norm.astype(int) #converting float to int

print('Float Format of Norm: \n')
print(norm)

print('\n')

print('Integer Format of Norm: \n')
print(norm_conv)