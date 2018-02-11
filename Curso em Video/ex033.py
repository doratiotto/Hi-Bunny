#Code1 - usando max e min
n1 = float(input('n1: '))
n2 = float(input('n2: '))
n3 = float(input('n3: '))

print('Mínimo: ', min(n1,n2,n3))
print('Máximo: ', max(n1,n2,n3))

#Code4 - usando if em estrutura de while
menor = n1
if n2 <= menor:
	menor = n2
if n3 <= menor:
	menor = n3

maior = n1
if n2 >= maior:
	maior = n2
if n3 >= maior:
	maior = n3

print('Menor: {}\nMaior: {}' .format(menor, maior))



#Code 2 - usando if completo
if n1<=n2 and n1<=n3:
	print('menor número: {}' .format(n1))
if n2<=n1 and n2<=n3:
	print('menor número: {}' .format(n2))
if n3<=n1 and n3<=n2:
	print('menor número: {}' .format(n3))


if n1>=n2 and n1>=n3:
	print('maior número: {}' .format(n1))
if n2>=n1 and n2>=n3:
	print('maior número: {}' .format(n2))
if n3>=n1 and n3>=n2:
	print('maior número: {}' .format(n3))


#Code3 if parcial
menor = n1
if n2<=n1 and n2<=n3:
	menor = n2
if n3<=n1 and n3<=n2:
	menor = n3

maior = n1
if n2>=n1 and n2>=n3:
	maior = n2
if n3>=n1 and n3>=n2:
	maior = n3

print('Menor número: {}\nMaior número: {}' .format(menor, maior))
