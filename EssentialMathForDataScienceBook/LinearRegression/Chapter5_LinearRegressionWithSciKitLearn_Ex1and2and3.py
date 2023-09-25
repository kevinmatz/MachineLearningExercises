# Chapter 5, Exercise 1 (p. 192)

# Chapter 5, Example 5-1 on p. 152:
# Using scikit-learn to perform a linear regression

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import t
from math import sqrt

# Import points:
df = pd.read_csv('https://bit.ly/3C8JzrM', delimiter=",")

# print(df)

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# print("Here is X:\n", X)

# Extract output column (all rows, last column)
Y = df.values[:, -1]

# print("Here is Y: ", Y)

# Fit a line to the points:
fit = LinearRegression().fit(X, Y)

m = fit.coef_.flatten()
b = fit.intercept_.flatten()
print("m = {0}".format(m))
print("b = {0}".format(b))

# Show in chart:
plt.plot(X, Y, 'ro')         # scatterplot
plt.plot(X, m*X+b, "g-")     # line
# plt.show()

# Calculate the correlation coefficient and statistical significance of this data
# at 95% confidence. Is the correlation useful?

print('Pearson correlation coefficient: r = ', df.corr(method='pearson'))
pearson_correlation_coefficient = 0.92421

# print("df.count: ", df.count)
print("df.shape: ", df.shape)
print("df.shape[0]: ", df.shape[0])
sample_size = df.shape[0]

# 95% confidence
tail_size = 0.025

# Find critical values for both ends of a T-distribution:
lower_critical_value = t(sample_size - 1).ppf(tail_size)
upper_critical_value = t(sample_size - 1).ppf(1 - tail_size)

# Perform the test (see p. 177):
test_value = pearson_correlation_coefficient / sqrt((1 - pearson_correlation_coefficient**2) / (sample_size - 2))

print("Test value: ", test_value)
print("Critical range: {}, {}".format(lower_critical_value, upper_critical_value))

if test_value < lower_critical_value or test_value > upper_critical_value:
    print("Correlation proven, reject H0")
else:
    print("Correlation not proven, failed to reject H0")

# Calculate p-value
if test_value > 0:
    p_value = 1.0 - t(sample_size - 1).cdf(test_value)
else:
    p_value = t(sample_size).cdf(test_value)

# Two-tailed, so multiply by 2
p_value = p_value * 2
print("p-value: {}".format(p_value))
print("p-value: ", p_value)


# Exercise 3
# If I predict where x = 50, what is the 95% prediction interval
# for the predicted value of y?

points = list(pd.read_csv('https://bit.ly/3C8JzrM', delimiter=",").itertuples())

# Calculate prediction interval for x = 50
x_0 = 50
x_mean = sum(p.x for p in points) / len(points)

t_value = t(sample_size - 2).ppf(.975)

print("t_value: ", t_value)

standard_error = sqrt(sum((p.y - (m * p.x +b))**2 for p in points) / (sample_size - 2))

print("standard_error: ", standard_error)

margin_of_error = t_value * standard_error * \
                  sqrt(1 + (1 / sample_size) + (sample_size * (x_0 - x_mean)**2) / \
                       (sample_size * sum(p.x ** 2 for p in points) - \
                            sum(p.x for p in points)**2))

print("margin_of_error: ", margin_of_error)

predicted_y = m*x_0 + b

# Calculate prediction interval
print("Prediction interval for y at x = 50:")
print(predicted_y - margin_of_error, predicted_y + margin_of_error)

# OK: interval 50.7920864 to 134.5144215
