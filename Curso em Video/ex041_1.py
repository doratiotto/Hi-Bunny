# Print
#from math import ceil
idade = int(input('Idade do nadador = '))

if idade >= 0 and idade < 9:
	print('Categoria: Mirim')

elif idade >= 9 and idade < 14:
	print('Categoria: Infantil')

elif idade >= 14 and idade < 19:
	print('Categoria: Junior')

elif idade >= 19 and idade < 20:
	print('Categoria: Senior')

elif idade >= 20 and idade < 200:
	print('Categoria: Master')

else:
	print('Essa é uma idade válida mesmo?')
