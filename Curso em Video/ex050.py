print ('=-=-=-=-=- Soma de Pares -=-=-=-=-=')
cont = 0
soma = 0

for c in range(1, 7, 1):
	x = int(input('Número {}: ' .format(c)))
	if x % 2 == 0:
		cont += 1
		soma += x

print('A soma dos números pares é {}. Foram {} números pares.' .format(soma, cont))
