print ('=-=-=-=-=- Verificador de Palindromo -=-=-=-=-=')

text = str(input('Frase: ')) .strip() .replace(' ', '') .lower()
c = 1

while c <= len(text)//2 and text[c-1] == text[-c]:
	c += 1
c -= 1

if c == len(text)//2:
	print('A frase é um palíndromo')
else:
	print('A frase não é um palíndromo')

'''
for i in range(0, len(x), 1)
frase.replace('luana', 'bananinha')
print(frase)
'''
