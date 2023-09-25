# Chapter 5, Example 5-21: Doing a train/test split on linear regression

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('https://bit.ly/3cIH97A', delimiter=",")

# Extract input variables (all rows, all columns but last column):
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

# Separate training and testing data
# This leave a third of the data out for testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1/3)

# print("X_train:")
# print(X_train)

model = LinearRegression()
model.fit(X_train, Y_train)

result = model.score(X_test, Y_test)
print("Coefficient of determination r^2: %.3f" % result)

plt.plot(X_train, Y_train, 'ro')    # Scatterplot of training data: red dots
plt.plot(X_test, Y_test, 'bs')    # Scatterplot of test data: blue squares

m = model.coef_.flatten()
b = model.intercept_.flatten()
plt.plot(X, m*X+b, 'g-')
plt.show()
