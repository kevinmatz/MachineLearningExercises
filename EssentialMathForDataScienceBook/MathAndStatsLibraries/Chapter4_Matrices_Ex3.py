# Chapter 4, Ex. 3 (p. 146)
#
# A transformation: i^ lands at [1, 0] and j^ lands at [2, 2]
# What is the determinant of this transformation?

from numpy import array
from numpy.linalg import det

i_hat = array([1, 0])
j_hat = array([2, 2])
basis = array([i_hat, j_hat]).transpose()
determinant = det(basis)
print(determinant)
