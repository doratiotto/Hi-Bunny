print ('=-=-=-=-=- Números impares x3 de 1 a 500 -=-=-=-=-=')
list = []

for c in range(1, 500, 1):
	if c % 3 == 0 and c % 2 == 1:
		list.append(c) 

print(list)
print('\nA soma deles é {}' .format(sum(list)))
print('\nCause baby you are a FIREWORK!!')
