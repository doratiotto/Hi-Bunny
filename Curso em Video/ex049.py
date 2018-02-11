print ('=-=-=-=-=- Tabuada -=-=-=-=-=')

x = int(input('Número: '))

for c in range(1, 11, 1):
	print('{} x {:2} = {:2}' .format(x, c, x * c))
