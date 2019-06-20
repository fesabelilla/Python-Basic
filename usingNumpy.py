# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:34:19 2019

@author: Asus
"""

import numpy 
numpy.array([1,2,3])

#import numpy as np
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