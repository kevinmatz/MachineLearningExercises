# Chapter 6, Exercise 1 (p. 226)

# https://bit.ly/3imidqa
# RED,GREEN,BLUE,LIGHT_OR_DARK_FONT_IND
# 0,0,128,0
# 102,153,153,1
# 102,205,0,1

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

color_data = pd.read_csv("https://bit.ly/3imidqa", delimiter=",")

# Independent variable columns:
inputs = color_data.iloc[:, :-1]

print("inputs: ", inputs)

# Dependent variable column:
output = color_data.iloc[:, -1]

print("output: ", output)

kfold = KFold(n_splits=3, random_state=7, shuffle=True)
model1 = LogisticRegression(penalty=None)   # .fit(inputs, output))
results = cross_val_score(model1, inputs, output, cv=kfold)

accuracy_mean = results.mean()
accuracy_stddev = results.std()

print("Accuracy mean: ", accuracy_mean)
print("Accuracy stddev: ", accuracy_stddev)

# My testing -- also part of exercise 3

model1.fit(inputs, output)
result1 = model1.predict([[5, 5, 5]])
print("result1: ", result1)
result2 = model1.predict([[230, 240, 250]])
print("result2: ", result2)

# Exercise 2

model2 = LogisticRegression(solver='liblinear')

X_train, X_test, Y_train, T_test = train_test_split(inputs, output, test_size=0.33)
model2.fit(X_train, Y_train)

prediction = model2.predict(X_test)

"""
The confusion matrix evaluates accuracy within each category:
[[truepositives falsenegatives]
 [falsepositives truenegatives]]
The diagonal represents correct predictions, so we want those to be higher
"""

matrix = confusion_matrix(y_true=T_test, y_pred=prediction)
print("Confusion matrix:")
print(matrix)

"""
[[155   7]
 [  2 280]]
"""

# Exercise 3: interactive shell:

while True:
    n = input("Input a color {red}, {green}, {blue}: ")
    (r, g, b) = n.split(",")
    x = model2.predict(np.array([[int(r), int(g), int(b)]]))
    answer = x[0]
    if answer == 0.0:
        print("LIGHT")
    else:
        print("DARK")