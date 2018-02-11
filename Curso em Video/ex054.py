from datetime import date

print ('=-=-=-=-=- Verificador de MaiorIdade -=-=-=-=-=')
maior = 0
menor = 0

for c in range(0, 7, 1):
	n = int(input('Ano de Nascimento da {}º pessoa : ' .format(c+1)))
	
	if date.today().year - n >= 18:
		maior += 1
	else:
		menor += 1

print('')
print('{} maiores de idade \n{} menores de idade' .format(maior, menor))

#print('{} maiores de idade \n{} menores de idade' .format(maior, menor))