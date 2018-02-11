print ('=-=-=-=-=- PA -=-=-=-=-=')

n0 = int(input('Primeiro termo: '))
r  = int(input('Razão: '))
s  = n0

for c in range(n0, n0 + 10, r):
	print(s)
	s += r

#print('A soma da PA é: {}' .format(s))
