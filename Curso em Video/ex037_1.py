# Print
#from math import ceil
x = int(input('Digite un múmero inteiro a ser convertido: '))
i = 1
lista = []

if i == 1:
	while x > 0:
		y = x %  2
		lista.append(y)
		x = x // 2		

		print(x, y)
	lista.reverse() 		
	print(lista)