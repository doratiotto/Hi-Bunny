# Print
#from math import ceil
x = int(input('Digite un múmero inteiro a ser convertido: '))
i = 2
lista = []

if i == 2:
	while x > 0:
		y = x %  8
		lista.append(y)
		x = x // 8		

		print(x, y)
	lista.reverse() 		
	print(lista)