# Chapter 3, Exercise 4 (p. 107)
#
# Past results: average of $10,345 of sales per day with standard deviation of $552
# New advertising campaign ran for 45 days and averaged $11,641 in sales per day
# Using a two-tailed test, determine: Did the campaign affect sales? why or why not?

from scipy.stats import norm

mean = 10345.00
std_dev = 552.00

new_sales = 11641.00

lower_bound_for_two_tail_test = mean - (new_sales - mean)

# Probability of new_sales (upper tail):
p1 = 1.0 - norm.cdf(new_sales, mean, std_dev)

# Probability of lower tail:
p2 = norm.cdf(lower_bound_for_two_tail_test, mean, std_dev)

p_value = p1 + p2

print("p value: ", p_value)

# p_value is 0.018883335964961383
# Because 0.01888 < 0.05, the change in sales is statistically significant
# so we reject the null hypothesis and accept the alternate hypothesis
# that the new marketing campaign has affected the average sales per day

