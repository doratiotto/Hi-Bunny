print ('=-=-=-=-=- Pessoas -=-=-=-=-=')

nomes  = []
idades = []
sexos  = []

homem  = []
homemid= []
mulher = []

for i in range(0, 4, 1):
	nomes.append(str(input('Nome da pessoa {}: ' .format(i+1))))
	idades.append(int(input('Idade da pessoa {}: ' .format(i+1))))
	sexos.append(int(input('Sexo da pessoa {}: \n1) Masculino \n2) Feminino\n' .format(i+1)) .strip() .lower()))
	print('')

med = ( idades[0] + idades[1] + idades[2] + idades[3] ) / 4
print('A média de idade é {}' .format(med))

for i in range(0, 4, 1):
	if sexos[i] == 1:
		homem.append(nomes[i])
		homemid.append(idades[i])
	else:
		if idades[i] < 20:
			mulher.append(nomes[i])
			
if len(homem) != 0:
	homemv = homem.index(max(homem))
	print('O homem mais velho é o {}' .format(homem[homemv]))
else:
	print('Não há homens para declarar o mais velho')

print('Mulheres com menos de 20 anos:', mulher)

	
	