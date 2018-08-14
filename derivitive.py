# from sympy import *
# import numpy as np

# x = Symbol('x')
# y = x**5 + 1
# yprime = y.diff(x)

# print(yprime)
# print(yprime(1))
import numpy

p = numpy.poly1d([2, 1, 3])
print(p)
  
q = p.deriv()
print(q)

print(q(5))
