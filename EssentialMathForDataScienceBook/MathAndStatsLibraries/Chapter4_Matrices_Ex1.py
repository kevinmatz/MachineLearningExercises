from numpy import array

# Examples from the chapter first...

# v = array([3, 2])
# w = array([2, -1])
# v_plus_w = v + w
# print(v_plus_w)
# scaled_v = 2.0 * v
# print(scaled_v)


# # basis = array(
# #     [[3, 0],
# #      [0, 2]]
# # )

# i_hat = array([3, 0])
# j_hat = array([0, 2])
# basis = array([i_hat, j_hat]).transpose()

# v = array([1, 1])

# new_v = basis.dot(v)
# print(new_v)



# Chapter 4, Ex. 1 (p. 146)
#
# Vector v has a value of [1, 2].
# A transformation happens.
# i^ lands at [2, 0] and j^ lands at [0, 1.5]. Where does v land?

i_hat = array([2, 0])
j_hat = array([0, 1.5])
basis = array([i_hat, j_hat]).transpose()
v = array([1, 2])
new_v = basis.dot(v)
print(new_v)
