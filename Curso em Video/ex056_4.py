print('=-=-=-=-=- Pessoas -=-=-=-=-=')
homem = ''
homemI = 0
mulher20 = 0
part = 4
somaI = 0
homemE= 0

for i in range(1, part + 1, 1):
	print('')
	nome = str(input('Nome da {}º pessoa: ' .format(i)))# .strip
	idade= int(input('Idade da {}º pessoa: ' .format(i)))
	sexo = str(input('Sexo da {}º pessoa (M/F): ' .format(i))) #.strip() .replace(' ', '') .lower()
	
	somaI+= idade
	
	if (sexo in 'Mm') and (idade > homemI): 
		homem = nome
		homemI= idade
		homemE+= 1

	elif sexo in 'Mm' and idade == homemI:	
		homem = [homem]
		homem.append(nome)
	
	if sexo in 'Ff' and idade < 20: # Contagem de f < 20
		mulher20 += 1

print('\nA médiaa de idade é: {:.1f} \n' .format(somaI/part))

print('{} mulhere(s) tem menos que 20 anos' .format(mulher20))

if homemE == 0:
	print('\nNão foram informados homens, não existe o mais velho!')
else:
	if type(homem) == str:
		print('O homem mais velho é o {}, ele tem {} anos! \n' .format(homem, homemI))
	else:
		print('Os homems mais velhos são: {}. Eles tem {} anos! \n' .format(homem, homemI))

