## Converter numeros positivos e negativos para qq base

x = int(input('Digite un múmero inteiro decimal a ser convertido: '))
i = int(input('Digite qual base você quer converter o número (ex: para binário digite 2, para base 3 digite 3: \n '))
lista = []

if x < 0:
	x = -x
	lista.append('-')
elif x > 0:
	lista.append('+')

while x > 0:
	y = x  % i
	lista.append(y)
	x = x // i		
	print(x, y)
lista.reverse() 		
print('Número {} convertido na base {} é: \n{}' .format(x, i, lista))
#print('{}' .format(lista))
