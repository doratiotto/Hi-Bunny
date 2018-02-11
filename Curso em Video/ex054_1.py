print ('=-=-=-=-=- Verificador de MaiorIdade -=-=-=-=-=')
lista = []
maior = 0
menor = 0

for c in range(0, 7, 1):
	lista.append(int(input('Idade da pessoa {}: ' .format(c+1))))
	
	if lista[c] >= 18:
		maior += 1
	else:
		menor += 1

print(lista)
print('')
print('{} maiores de idade \n{} menores de idade' .format(maior, menor))

#print('{} maiores de idade \n{} menores de idade' .format(maior, menor))