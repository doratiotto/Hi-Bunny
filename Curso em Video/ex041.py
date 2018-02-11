
import datetime

ano = int(input('Ano de nascimento: '))
anoh = datetime.date.today().year

idade = anoh - ano


if idade > 0 and idade <= 9:
	print('{} Anos; Categoria: Mirim' .format(idade))

elif idade <= 14:
	print('{} Anos; Categoria: Infantil' .format(idade))

elif idade <= 19:
	print('{} Anos; Categoria: Junior' .format(idade))

elif idade <= 20:
	print('{} Anos; Categoria: Senior' .format(idade))

elif idade <= 200:
	print('{} Anos; Categoria: Master' .format(idade))

else:
	print('Essa é uma idade válida mesmo?')
