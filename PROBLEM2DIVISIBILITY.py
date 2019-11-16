# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 22:43:07 2019

@author: Angela Leenzae Edang
"""

''' Create the following 10x10 ndarray, which is the squares of the first 100
positive integers. From this ndarray, determine all the elements that are
divisible by 3. Save the result as div_by_3.npy '''

import numpy as np

# Z - 10x10 ndarray from 1 to 10000
# Z - squares of the ndarray from 1 to 10000

Y = np.array(np.array([(np.linspace(1,10,10)), (np.linspace(11,20,10)), (np.linspace(21,30,10)), 
                       (np.linspace(31,40,10)), (np.linspace(41,50,10)), (np.linspace(51,60,10)), 
                       (np.linspace(61,70,10)), (np.linspace(71,80,10)), (np.linspace(81,90,10)), 
                       (np.linspace(91,100,10))]))
Z = np.multiply(Y,Y)

# modulo - checking for the divisibility by 3
# modulo_conv - converting the new ndarray to integer type from float type

modulo = np.array([(Z[Z%3 == 0])])
modulo_conv = modulo.astype(int)
print(modulo_conv)