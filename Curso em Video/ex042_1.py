
l1 = int(input('Lado 1 = '))
l2 = int(input('Lado 2 = '))
l3 = int(input('Lado 3 = '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
	print('Existe um triângulo. ' , end='')
	
	if l1 != l2 != l3 != l1:
		print('É um triângulo escaleno!')

	elif l1 == l2 == l3:
		print('É um triângulo equilátero de lado {}!' .format(l1))

	else:
		print('É um triângulo isósceles!')

else:
	print('Não existe um triângulo com os lados dados!')
