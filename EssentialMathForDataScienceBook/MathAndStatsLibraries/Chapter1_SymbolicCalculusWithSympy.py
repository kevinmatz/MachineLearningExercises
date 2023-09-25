from sympy import *
from sympy.plotting import plot3d

x = 5
f2 = x ** 2
print(f2)

x = symbols('x')

f = x ** 2
print(f)

# Calculate the derivative of the function:
dx_f = diff(f)
print(dx_f)

slope_at_2 = dx_f.subs(x, 2)
print (slope_at_2)

# Calculate a partial derivative:
x, y = symbols('x y')
f = 2*x**3 + 3*y**3
dx_f = diff(f, x)
dy_f = diff(f, y)

print('dx_f: ', dx_f)
print('dy_f: ', dy_f)

plot3d(f)

# Perform integration:
x = symbols('x')
f = x**2 + 1
# Integral of function f with respect to x for the area between x = 0 and 1
area = integrate(f, (x, 0, 1))
print(area)




