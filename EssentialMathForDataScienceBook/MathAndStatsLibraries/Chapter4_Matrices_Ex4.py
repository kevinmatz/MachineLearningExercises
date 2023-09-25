# Chapter 4, Ex. 4 (p. 146)
#
# Solve this system of equations for x, y, z:
#
# 3x + 1y + 0z = 54
# 2x + 4y + 1z = 12
# 3x + 1y + 8z = 6

# Using numpy:
from numpy import array
from numpy.linalg import inv

A = array([
    [3, 1, 0],
    [2, 4, 1],
    [3, 1, 8]
])

B = array([54, 12, 6])
B2 = array([[54], [12], [6]])

X = inv(A).dot(B)
print(X)

X2 = inv(A).dot(B2)
print(X2)

print("A.shape: ", A.shape)
print("B.shape: ", B.shape)
print("X.shape: ", X.shape)
print("B2.shape: ", B2.shape)
print("X2.shape: ", X2.shape)
