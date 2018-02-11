print('-=-=-=-=- Fatorial -=-=-=-=-\n')
num0 = int(input('Número = '))

if num0 < 0:
	num = - num0
	print('O número dado é negativo, continuaremos com seu módulo: |{}| = {}' .format(num0, num))
	num0 = num

fat = 1
print('{}! = ' .format(num0), end='')

for num in range(num0, 0, - 1):	
	fat = fat * num
	print('{}' .format(num), end='')
	print(' x ' if num > 1 else '', end='')
	num += - 1

print(' = {}' .format(fat))

'''	

	if i == '1':
		print('{} + {} = {}' .format(num1, num2, num1 + num2))	
	elif i == '2':
		print('{} - {} = {}' .format(num1, num2, num1 - num2))	
	elif i == '3':
		print('{} x {} = {}' .format(num1, num2, num1 * num2))	
	else:
		print('{} % {} = {}' .format(num1, num2, num1 / num2))	
'''