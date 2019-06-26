# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 12:45:28 2019

@author: Asus
"""


#Script 
#Shell


#chapter - 1

## L - 1

# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)
 


## L - 2

# Create a variable savings
savings = 100

# Create a variable growth_multiplier
growth_multiplier =  1.1

# Calculate result
result = savings * growth_multiplier ** 7

# Print out result
print(result)


## L - 3


savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of growth_multiplier and savings to year1


# Note first write float then write integer value
year1 = growth_multiplier * savings

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc;
print(doubledesc)

## L - 4

# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = str("3.1415926")

# Convert pi_string into float: pi_float
pi_float = float("3.1415926")


# L -- 5

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas

areas = [hall,kit,liv,bed,bath]

# Print areas
print(areas)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area

eat_sleep_area =  areas[7] + areas[3] ;

# Print the variable eat_sleep_area
print(eat_sleep_area)


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
 
downstairs = areas[:6]

# Use slicing to create upstairs

upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs

downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]

#x = ["a", "b", "c", "d"]
#x[:2]
#x[2:]
#x[:]



#List Manipulation


#changing list elements
fam = ["liz",1.73,"emma",1.68,"mom",1.71,"dad",1.89]
print(fam)
fam[7] = 1.86
print(fam)

fam[0:2] = ["lisa",1.74]
print(fam)

#Adding & Removing elements 
fam_extra = fam + ["me",1.79]
print(fam_extra)

#Delete form the list
#remove "emma"
del(fam[2])
print(fam)
#remove emmas height 1.68
del(fam[2])
print(fam)

#problem of copying list because of references 
 
x = ["a","b","c"]
y = x #copy refferences to the list . not copy value the list. thats why if we change the "y" then "x" will be changed 
y[1] = "z"
print(y)

#the funky thing is this x will be changed
print(x) 

# Solve the provlem now

k = ["a","b","c"]
l = list(k)
l = k[:]
 
l[1] = "z"
 
print(l)
 
print(k)


#Chapter - 3

# l - 1

# Function
 
# max() function

fam1 = [1.73,1.68,1.71,1.89]
tallest = max(fam1)
print(tallest)

#round() function

help(round)

print(round(1.68,1)) #1.7

print(round(1.68)) #2

#Quiz - 1

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
#or out2 = round(var2)

# sorted() function

help(sorted)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full

full = first + second

# Sort full in descending order: full_sorted

full_sorted = sorted(full,reverse = True)

# Print out full_sorted

print(full_sorted)


# List Method 

fam = ["liz",1.73,"ema",1.68,"mom",1.71]
a = fam.index("mom")
print(a)
b = fam.count(1.73)
print(b)

# str method
sister = "liz"
print(sister)
print(sister.capitalize());

print(sister.replace("z","sa"))


#Everything = object
#Object have methods associated, depending on type

#hi
print(sister.index("i"))
 
print(fam.index("mom"))


print(fam)
fam.append("me")
fam.append(1.79)
print(fam)

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up

place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place

print(place.count("o"))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
a = areas.index(20.0)
print(a)
# Print out how often 9.50 appears in areas
b = areas.count(9.50)
print(b)

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size

areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)



