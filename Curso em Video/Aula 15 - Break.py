lista = []
while True:
	num = int(input('número = '))
	if num == 0:
		break
	lista.append(num)
	print(lista)

soma = 0
while True:
	num = int(input('número = '))
	if num == 999:
		break
	soma += num
print(f'A soma vale {soma}')


num = 0
i = 1

while i <= 5:
	num = int(input('n = '))
	if num == 999:
		break
	i += 1


while num !=999:
	num = int(input('n = '))

'''
x = int(input('Número: '))
i = 2
k = 0

print('')
while i <= x // 2:
	if x % i == 0:
		print('{} divide {}' .format(i, x))
		k = 1
		break
	i += 1
#	else:
#		continue
#	print(c)
if k == 1:
	print('{} não é primo' .format(x))
else:
	print('{} é primo' .format(x))

print('\nfim')
'''