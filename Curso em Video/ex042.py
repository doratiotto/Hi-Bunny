# Print
#from math import ceil
print('Verificador de triângulos')

l1 = float(input('Lado 1 = '))
l2 = float(input('Lado 2 = '))
l3 = float(input('Lado 3 = '))

A = [l1, l2, l3]
# primeiro valor máximo
M = max(A)
A.remove(M)

if sum(A) > M:
	print('Existe um triângulo')
	
	if l1 == l2 == l3:
		print('É um triângulo equilátero de lado {}!' .format(l1))

	elif l2 == l3:
		print('É um triângulo isósceles de base {}!' .format(l1))
	elif l1 == l3:
		print('É um triângulo isósceles de base {}!' .format(l2))
	elif l1 == l2:
		print('É um triângulo isósceles de base {}!' .format(l3))
	
	else:
		print('É um triângulo escaleno!')

else:	
	print('Não existe um triângulo')
	