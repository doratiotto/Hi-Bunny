print ('=-=-=-=-=- Verificador de Maior/Menor Peso -=-=-=-=-=')
lista = []

for c in range(0, 5, 1):
	lista.append(float(input('Peso da pessoa {}: ' .format(c+1))))

print('')
print('Maior peso: {}kg \nMenor peso: {}kg' .format(max(lista), min(lista)))
