# Print
#from math import ceil
x = float(input('x = '))
y = float(input('y = '))

if x < y:
	print('{} < {}' .format(x, y))
elif y < x:
	print('{} < {}' .format(y, x))
else:
	print('{} = {}' .format(y, x))

