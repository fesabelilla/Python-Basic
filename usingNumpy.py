# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:34:19 2019

@author: Asus
"""


#Numeric Python

#import numpy 
#numpy.array([1,2,3])

import numpy as np
#np.array([1,2,3])

# only use array function in the numpy package 
#from numpy import array
#array([1,2,3])

# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r*radians(12)

# Print out dist
print(dist)

# NumPy Array calculation

np_height = np.array([1.73,1.68,1.71])
np_weight = np.array([65.4,59.2,63.6])

bmi = np_weight/np_height ** 2

print(bmi)

print(bmi[2])

print(bmi > 21) #it return bool values Ex. True or False

print(bmi[bmi > 21]) # it return value 

# different btw NumPy array and List

python_list = [1,2,3]

print(python_list + python_list)

numpy_array = np.array([1,2,3])

print(numpy_array + numpy_array)


















