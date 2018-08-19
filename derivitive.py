import pdb;

#String normalizer for more user friendly string inputs
def normalize_y_string(y_string):
	if y_string[0] not in ('-', '+'):# if sign not specified at the begining of the polynomial (term is +ve)
		y_string = '+'+y_string
	y_list = y_string.split()
	for i, term in enumerate(y_list):
		if term[1] is 'x':# coefficient specified (coefficient is 1)
			y_list[i] = f'{term[0]}1{term[1:]}'
		if 'x' not in y_list[i]:# x term not explicitly specified (exponent is 0)
			y_list[i] += 'x^0'
		if '^' not in y_list[i]:# exponent not explicitly specified (exponent is 1)
			y_list[i] += '^1'
	return ' '.join(y_list)

# Input must be formatted like '4x^5 -2x^2 +3'
# Output gives polynomial in processable list form [[4, 5], [-2, 2], [3, 1]]
def get_y_list(y_string):
	return [[int(num) for num in term.split('x^')] for term in normalize_y_string(y_string).split(' ') if term[0] is not '0']

# Input must be in processable list form
def get_y_string(y_list):
	return ' '.join([f'{"+" if term[0] > 0 else ""}{term[0]}x^{term[1]}' for term in y_list if term[0] != 0])

# Input must be the processable list form [[4, 5], [-2, 2], [3, 1]]
# Outputs pretty string form of polynomial '4x^5 -2x^2 +3'
def get_derivitive(y_list):
	return [[term[0]*term[1], term[1]-1] for term in y_list if not (term[1] == 0 or term[0] == 0)]

def get_value_at(x,y_list):
	print(f'eval {y_list} at {x}')
	return sum((x**term[1])*term[0] for term in y_list)

#Testing
y_string = '4x^5 -2x^2 +x +3'
y_list = get_y_list(y_string)

print('y:\n',y_string)
print(y_list)
print('y(0): ',get_value_at(0,y_list))
print('y(5): ',get_value_at(5,y_list))

yprime_list = get_derivitive(y_list)
yprime_string = get_y_string(yprime_list)

print('y\':\n',yprime_string)
print(yprime_list)
print('y(0): ',get_value_at(0,yprime_list))
pdb.set_trace()
print('y(5): ',get_value_at(5,yprime_list))

# y2 = [[20, 4], [-4, 1], [1, 0]]
# print('normalizing: ',[[20, 4], [-4, 1], [1, 0]])
# print('normalized_y_string: ',normalize_y_string([[20, 4], [-4, 1], [1, 0]]))
