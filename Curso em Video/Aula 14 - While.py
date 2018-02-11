# While
'''
c = 1
while c < 5:
	print('oi'*c)
	c = c + 1
print('bye ヾ(°∇°*)')

x = ''
while x != 'xau':
	x = input('oi ヾ(°∇°*) \n')
print('bye ヾ(^_^) ')
'''
n = 1
par = impar = 0
'''
while n != 0:
	n = int(input('Digite um valor (digite 0 para terminar): '))
	if n!= 0:
		if n % 2 == 0:
			par += 1
		else:
			impar += 1
'''
while n != 0:
	n = int(input('Digite um valor (digite 0 para terminar): '))
	if n % 2 == 0:
		par += 1
	else:
		impar += 1
par -= 1

print(par, impar)
