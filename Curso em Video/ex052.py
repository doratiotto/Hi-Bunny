print ('=-=-=-=-=- Verificador de número Primo -=-=-=-=-=')

x = int(input('Número: '))
k = 0

print('')
for c in range(2, x // 2, 1):
	if x % c == 0:
		print('Div:', c)
		k = 1
		break
#	else:
#		continue
#	print(c)
if k == 1:
	print('{} não é primo' .format(x))
else:
	print('{} é primo' .format(x))

print('\nfim')
