print('-=-=-=-=- Fatorial -=-=-=-=-\n')
num0 = int(input('Número = '))
num = num0

if num0 < 0:
	num = - num0

fat = num
while num >= 3:	
	fat = fat * (num -1)
	num -= 1

if num0 < 0 and num0 % 2 == 1:
	print('{}! = {}' .format(num0, -fat))
else:
	print('{}! = {}' .format(num0, fat))
print('\n*** Saiu com sucesso! ***')


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