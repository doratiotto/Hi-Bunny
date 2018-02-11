print ('=-=-=-=-=- PA -=-=-=-=-=')

n0 = float(input('Primeiro termo: '))
r  = float(input('Razão: '))
soma = n0

for c in range(0, 10, 1):
	if c < 9:
		print('{:.0f} ->' .format(soma), end=' ')
	else:
		print('{:.0f}' .format(soma), end=' ')
	soma += r

print('-> fim')
#print('A soma da PA é: {}' .format(s))
