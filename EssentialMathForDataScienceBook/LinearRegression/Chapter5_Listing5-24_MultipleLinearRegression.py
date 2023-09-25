# Chapter 5, Example 5-24
# Multiple linear regression (two input variables)

import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('https://bit.ly/2X1HWH7', delimiter=",")

# x1,x2,y
# 0,22,88
# 1,13,62
# ...

X = df.values[:, :-1]
Y = df.values[:, -1]

fit = LinearRegression().fit(X, Y)

print("Coefficients = {0}".format(fit.coef_))
print("Intercept = {0}".format(fit.intercept_))
print("z = {0} + {1}x + {2}y".format(fit.intercept_, fit.coef_[0], fit.coef_[1]))
