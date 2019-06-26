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
print(np_weight_lb[2])

# Print out sub-array of np_height_in: index 100 up to and including index 110
# start index : end index-1 (1:2)
print(np_height_in[1:2])


#2D NumPy Arrays
np_2d = np.array([[1.73,1.68,1.71,1.89,1.79],
                  [65.4,59.2,63.6,88.4,68.7]])
print(np_2d)

print(np_2d[0][2])
print(np_2d[0,2])
# row and column
print(np_2d.shape)

print(np_2d[:,1:3])
print(np_2d[1,:])
 
# mean

l = np.mean(np_2d[:,0])
print(l)
print(np.median(np_2d[:,0]))

# np_baseball is available
np_baseball = np.array([[2,3,4,5],
                       [6,7,8,9]])
# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))


# np_baseball is available


# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
x= np_baseball[:,0]
y = np_baseball[:,1]
corr = np.corrcoef(x,y)
print("Correlation: " + str(corr))











