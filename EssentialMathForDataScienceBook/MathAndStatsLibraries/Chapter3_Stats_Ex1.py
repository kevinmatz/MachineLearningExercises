# Chapter 3, Exercise 1 (p. 107)
# 5 data points:
# 1.78, 1.75, 1.72, 1.74, 1.77
# How close are these to the spec of 1.75mm?
# Calculate the mean and standard deviation for this set of values.

# from scipy.stats import *
from math import sqrt

sample = [1.78, 1.75, 1.72, 1.74, 1.77]

sum1 = sum(sample)
print("sum1: ", sum1)

mean = sum1 / len(sample)
print("mean: ", mean)

def variance(values, is_sample : bool = False):
    mean = sum(values) / len(values)
    sum_of_squares = sum((v - mean)**2 for v in values)
    _variance = sum_of_squares / (len(values) - (1 if is_sample else 0))
    return _variance

def std_dev(values, is_sample : bool = False):
    return sqrt(variance(values, is_sample))

print("Standard deviation: ", std_dev(sample, is_sample=True))
