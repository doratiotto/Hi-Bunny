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
	
	# Calculo da média a cada iteração com uma idade nova
	if i == 1:
		media = idade
	else:
		media = (media + idade) / 2

	# Calculo do homem mais velho
	if sexo == 'm' or sexo == 'M':
		if i == 1:
			homem = nome
			homemI= idade
		else:
			if idade > homemI:
				homem = nome
				homemI= idade
			elif idade == homemI:
				homem = [homem]
				homem.append(nome)
	# Calculando mulheres < 20 idade
	if (sexo == 'f' or sexo == 'F') and (idade < 20) :
		mulher20 += 1

print(media)
print('O homem mais velho (lista se tiver mais de um) é {}' .format(homem))
print(mulher20)
# print('{} {} {}' .format(nome, idade, sexo))
