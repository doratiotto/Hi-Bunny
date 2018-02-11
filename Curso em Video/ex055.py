print ('=-=-=-=-=- Verificador de Maior/Menor Peso -=-=-=-=-=')
#maior = 0
#menor = 0

for c in range(0, 5, 1):
	x = float(input('Peso da pessoa {}: kg ' .format(c+1)))
	if c == 0:
		menor = x
		maior = x
	
	if x > maior:
		maior = x
	if x < menor:
		menor = x

print('')
print('Maior peso: {}kg \nMenor peso: {}kg' .format(maior, menor))
