print('=-=-=-=-=- Pessoas -=-=-=-=-=')
media = 0
homem = ''
homemI = 0
mulher20 = 0


for i in range(1, 4, 1):
	print('')
	nome = str(input('Nome da {}º pessoa: ' .format(i)))# .strip
	idade= int(input('Idade da {}º pessoa: ' .format(i)))
	sexo = str(input('Sexo da {}º pessoa (M/F): ' .format(i))) #.strip() .replace(' ', '') .lower()
	
	if i == 1:
		media = idade 					# Idade Inicial p/ média
		if sexo in 'Mm':
			homem = nome 				# Homem mais velho Inicial: Nome
			homemI= idade 				# Homem mais velho Inicial: Idade
	
	else:
		media = (media + idade) / 2		# Média a cada nova entrada/iteração
		if sexo in 'Mm':
			if idade > homemI:			# Homem mais velho novo maior
				homem = nome
				homemI= idade
			elif idade == homemI:		# Homem mais velho novo igual
				homem = [homem]
				homem.append(nome)
	
	if sexo in 'Ff' and idade < 20: # Contagem de f < 20
		mulher20 += 1

print('')
print('A média de idade é {} \n' .format(media))
print('O(s) homem(s) mais velho(s) é(são): {} \n' .format(homem))
print('{} mulhere(s) tem menos que 20 anos' .format(mulher20))
# print('{} {} {}' .format(nome, idade, sexo))
