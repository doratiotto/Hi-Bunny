
print ('=-=-=-=-=- Verificador de número Primo -=-=-=-=-=')

x = int(input('Número: '))
p = 0

for c in range(2, x, 1):
	if x % c == 0:
		p += 1
	else:
		continue
		
if p > 0:
	print('{} não é primo' .format(x))
else:
	print('{} é primo' .format(x))


print('\nfim')

#print('A soma da PA é: {}' .format(s))
