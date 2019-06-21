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

weight_lb = [1,2,3]
height_in = [1,2,3]

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])


















