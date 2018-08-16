# from sympy import *
# import numpy as np

# x = Symbol('x')
# y = x**5 + 1
# yprime = y.diff(x)

# print(yprime)
# print(yprime(1))
# import numpy

# p = numpy.poly1d([2, 1, 3])
# print(p)
  
# q = p.deriv()
# print(q)

# print(q(5))

##Can't have numpy on micropython, so...

# Input must be formatted like '4x^5 -2x^2 +3'
# Output gives polynomial in processable list form [[4, 5], [-2, 2], [3, 1]]
def y_list(y_string):
	return [[int(num) for num in term.split('x^')] for term in y_string.split(' ') if term[0] is not '0']
	# y_list = []


	# for term in y_string.split(' '):
	# 	x_pos = term.find('x')
	# 	y_list.append(int([term[:x_pos]]), int(term[x_pos+1:]))

	# return y_list

# Input must be in processable list form
def y_string(y_list):
	return ' '.join([f'{term[0]}x^{term[1]}' for term in y_list if term[0] != 0])


# Input must be the processable list form [[4, 5], [-2, 2], [3, 1]]
# Outputs pretty string form of polynomial '4x^5 -2x^2 +3'
def derivitive(y_list):#
	return [[y[0]*y[1], y[1]-1] for term in y if y[0] != 1]