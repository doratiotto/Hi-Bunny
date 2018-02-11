print ('=-=-=-=-=- Números impares x3 de 1 a 500 -=-=-=-=-=')
soma = 0
cont = 0

for c in range(1, 501, 1):
	if c % 3 == 0 and c % 2 == 1:
		print(c, end=' ') 
		cont += 1
		soma += c		

print('\nA soma deles é {}. Foram {} valores!' .format(soma, cont))
#print('\nCause baby you are a FIREWORK!!')
