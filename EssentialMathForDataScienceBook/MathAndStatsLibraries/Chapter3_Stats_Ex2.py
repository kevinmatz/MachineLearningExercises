# Chapter 3, Exercise 2 (p. 107)
# Z-Phone maker claims mean consumer life of 42 months with
# standard deviation of 8 months
# Assuming a normal distribution, what is the probability a given Z-Phone
# will last between 20 and 30 months?
#
# See pattern on p. 85

from scipy.stats import norm

mean = 42.0
std_dev = 8.0

upper_cdf = norm.cdf(30, mean, std_dev)
lower_cdf = norm.cdf(20, mean, std_dev)

print("upper_cdf for x = 30: ", upper_cdf)
print("lower_cdf for x = 20: ", lower_cdf)

probability = upper_cdf - lower_cdf

print("probability: ", probability)
