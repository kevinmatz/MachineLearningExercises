# Chapter 5, Example 5-1 on p. 152:
# Using scikit-learn to perform a linear regression

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Import points:
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

# print(df)

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

print("Here is X:\n", X)

# Extract output column (all rows, last column)
Y = df.values[:, -1]

print("Here is Y: ", Y)

# Fit a line to the points:
fit = LinearRegression().fit(X, Y)

m = fit.coef_.flatten()
b = fit.intercept_.flatten()
print("m = {0}".format(m))
print("b = {0}".format(b))

# Show in chart:
plt.plot(X, Y, 'o')    # scatterplot
plt.plot(X, m*X+b)     # line
plt.show()

