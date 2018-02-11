print ('=-=-=-=-=- Verificador de Palindromo -=-=-=-=-=')

text = str(input('Frase: ')) .strip() .replace(' ', '') .lower()

t = 0
for c in range(1, len(text)+1, 1):
	if text[c - 1] != text[-c]:
		t = 1
		break

print('')	
if t == 0:
	print('A frase é um palíndromo')
else:
	print('A frase não é um palíndromo')

'''
for i in range(0, len(x), 1)
frase.replace('luana', 'bananinha')
print(frase)
'''
