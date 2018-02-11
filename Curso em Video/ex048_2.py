print ('=-=-=-=-=- Números impares x3 de 1 a 500 -=-=-=-=-=')

soma = 0

for c in range(1, 500, 1):
	if c % 3 == 0 and c % 2 == 1:
		soma += c

print('\nA soma deles é {}' .format(soma))

