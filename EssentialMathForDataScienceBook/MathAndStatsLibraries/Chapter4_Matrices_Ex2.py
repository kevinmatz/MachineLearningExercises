# Chapter 4, Ex. 2 (p. 146)
#
# Vector v has a value of [1, 2].
# Transformation where i^ lands on [-2, 1] and j^ lands on [1, -2].
# Where does v land?

from numpy import array

i_hat = array([-2, 1])
j_hat = array([1, -2])
basis = array([i_hat, j_hat]).transpose()
v = array([1, 2])
new_v = basis.dot(v)
print(new_v)
