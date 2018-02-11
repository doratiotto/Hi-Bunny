print('-=-=-=-=- FIBONACCI SEQ -=-=-=-=-\n')
user = 10
i = 3

n = int(input('Número de elementos: '))
num1 = 0
num2 = 1
soma = 0

print('')
if n <= 0:
	print('Nemhum elemento a ser mostrado')
elif n == 1:
	print(num1)
else:
	print('Sequência de Fibonacci com {} elementos: \n{} -> {}' .format(n, num1, num2), end=' ')
	while i <= n:
		soma = num1+ num2
		print('-> {}' .format(soma), end=' ')
		num1 = num2
		num2 = soma

		i = i + 1
print('-> THE END')
'''

while user != 0:
	i = 1
	while i <= user:	
		print(' {} ->' .format(res), end='')
		res += raz
		i 	+= 1
	print(' end')
	user = int(input('\nQuer adicionar mais termos? Digite o nº de termos ou 0 para sair. '))
	
print('Programa saiu com Sucesso!')
'''