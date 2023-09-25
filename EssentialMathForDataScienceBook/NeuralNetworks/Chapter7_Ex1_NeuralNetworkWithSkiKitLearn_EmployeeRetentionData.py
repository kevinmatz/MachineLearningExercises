# Chapter 7, Exercise 1 (p. 256)
#
# Employee retention data set: https://tinyurl.com/y6r7qjrp
#
# SEX,AGE,PROMOTIONS,YEARS_EMPLOYED,DID_QUIT
# 0,25,2,3,0
# 1,29,2,5,1

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

data_frame = pd.read_csv("https://tinyurl.com/y6r7qjrp", delimiter=",")

X_values = data_frame.values[:, :-1]

# print(X_values)
# print(X_values.shape[0])

Y_values = data_frame.values[:, -1]

# print(Y_values)
# print(Y_values.shape[0])

X_train, X_test, Y_train, Y_test = train_test_split(X_values, Y_values, test_size=0.3)

neural_network = MLPClassifier(solver='sgd',
                               hidden_layer_sizes=(3, ),
                               activation='relu',
                               max_iter=100_000,
                               learning_rate_init=0.05)

neural_network.fit(X_train, Y_train)

print("Coefficients: ", neural_network.coefs_)
print("Intercepts: ", neural_network.intercepts_)
print("Training set score: %f" % neural_network.score(X_train, Y_train))
print("Test set score: %f" % neural_network.score(X_test, Y_test))

print("Confusion matrix:")
matrix = confusion_matrix(y_true=Y_test, y_pred=neural_network.predict(X_test))
print(matrix)

case1 = np.array([[0, 35, 3, 4]])
result1 = neural_network.predict(case1)
print("case1: ", case1)
print("result1: ", result1)

case2 = np.array([[1, 42, 0, 9]])
result2 = neural_network.predict(case2)
print("case2: ", case2)
print("result2: ", result2)

case3 = np.array([[1, 45, 3, 1]])
result3 = neural_network.predict(case3)
print("case3: ", case3)
print("result3: ", result3)

case4 = np.array([[1, 24, 0, 7]])
result4 = neural_network.predict(case4)
print("case4: ", case4)
print("result4: ", result4)
