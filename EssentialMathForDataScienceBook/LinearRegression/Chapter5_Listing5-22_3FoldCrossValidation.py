# Chapter 5, Example 5-22
# Using three-fold cross-validation for a linear regression

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score
import matplotlib.pyplot as plt

# df = "data frame"
df = pd.read_csv('https://bit.ly/3cIH97A', delimiter=",")

# Extract input variables
X = df.values[:, :-1]

# Extract output column
Y = df.values[:, -1]

# Perform a simple linear regression
kfold = KFold(n_splits=3, random_state=7, shuffle=True)
model = LinearRegression()
results = cross_val_score(model, X, Y, cv=kfold)   # cv = "cross validator"
print(results)
print("Mean Sum of Squares (MSE): mean=%.3f (stdev=%.3f)" % (results.mean(), results.std()))

# But the above doesn't actually do a linear regression???

model.fit(X, Y)
m = model.coef_.flatten()
b = model.intercept_.flatten()
print("m: ", m)
print("b: ", b)

plt.plot(X, Y, 'ro')    # Scatterplot of training data: red dots
plt.plot(X, m*X+b, 'g-')
plt.show()
