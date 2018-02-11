print('-=-=-=-=- Calculadora -=-=-=-=-\n')
num1 = float(input('n1 = '))
num2 = float(input('n2 = '))
opt  = ['1', '2', '3', '4', '5', '6', '7', '8']
i = 0
#i = input('Escolha a operação: \n1) + \n2) - \n3) x \n4) % \n5) Novos Números \n6) Sair \nR:')

while i != '7':	
	i = input('''\nEscolha a operação: 
	1) + 
	2) - 
	3) x 
	4) % 
	5) Maior número: 
	6) Menor Número:
	7) Novos Números: 
	8) Sair:
	R:''')
	
	while i not in opt:
		i = input('Opção Inválida! Digite novamente: ')

	if i == '1':
		print('\n{} + {} = {}' .format(num1, num2, num1 + num2))	
	elif i == '2':
		print('\n{} - {} = {}' .format(num1, num2, num1 - num2))	
	elif i == '3':
		print('\n{} x {} = {}' .format(num1, num2, num1 * num2))	
	elif i == '4':
		print('\n{} % {} = {}' .format(num1, num2, num1 / num2))	
	elif i == '5':
		print('\n O maior é {}' .format(max(num1, num2)))	
	elif i == '6':
		print('\n O menor é {}' .format(min(num1, num2)))	
	elif i == '7':
		print('')
		num1 = float(input('n1 = '))
		num2 = float(input('n2 = '))
	
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