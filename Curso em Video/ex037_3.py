# Print
#from math import ceil
x = int(input('Digite un múmero inteiro a ser convertido: '))
i = 3
lista = []

if i == 3:
	while x > 0:
		y = x %  16
		if y == 10:
			y = 'a'
		elif y == 11:
			y = 'b'
		elif y == 12:
			y = 'c'	
		elif y == 13:
			y = 'd'
		elif y == 14:
			y = 'e'	
		elif y == 15:
			y = 'f'

		lista.append(y)
		x = x // 16		

		print(x, y)
	lista.reverse() 		
	print(lista)