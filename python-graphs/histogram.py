#!/usr/bin/env python
# *********************************************************************
# Simple histogram python program
# *********************************************************************
import matplotlib.pyplot as plt

# frequencies
ages = [2,5,70,40,30,45,50,45,43,40,44, 60,7,13,57,18,90,77,32,21,20,40]

# setting the ranges and no. of intervals
range = (0, 100)
bins = 10

# plotting a histogram
plt.hist(ages, bins, range, color = 'green', histtype = 'bar', rwidth = 0.8)

# Set x and y labels
plt.xlabel('age')
plt.ylabel('No. of people')
plt.title('My histogram')

# function to show the plot
plt.show()
