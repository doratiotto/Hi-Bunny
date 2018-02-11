print ('=-=-=-=-=- Números pares de 1 a 50 -=-=-=-=-=')
s = 0

for c in range(2, 51, 2):
	if c % 2 == 0:
		print(c, end=' ')
		s += c

print('Soma =', s)
#print('\nCause baby you are a FIREWORK!!')