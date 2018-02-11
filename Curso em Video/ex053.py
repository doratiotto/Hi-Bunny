print ('=-=-=-=-=- Verificador de Palindromo -=-=-=-=-=')

text = str(input('Frase: ')) .strip() .replace(' ', '') .lower()
texti= text[::-1]
print('')

if text == texti:
	print('A frase é um palíndromo \n')
	print(text, '=', texti)
else:
	print('A frase não é um palíndromo \n')
	print(text, '!=', texti)
