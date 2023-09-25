# Chapter 4, Ex. 5 (p. 146)
#
# Is this matrix linearly dependent?  Why or why not?
# 2 1
# 6 3

from numpy import array
from numpy.linalg import det

A = array([[2, 1], [6, 3]])
print(A)

determinant = det(A)
print(determinant)
# -3.330669073875464e-16
# --> floating-point artifact, it's effectively 0
# --> so therefore it is linearly dependent

# Let's try sympy:

import sympy as my_sympy

basis2 = my_sympy.Matrix([
    [2, 1],
    [6, 3]
])

det2 = my_sympy.det(basis2)
print(basis2)
print(det2)

basis3 = my_sympy.Matrix([
    [2, 6],
    [1, 3]
])
det3 = my_sympy.det(basis3)
print(basis3)
print(det3)


