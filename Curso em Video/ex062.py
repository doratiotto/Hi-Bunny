print('-=-=-=-=- PA -=-=-=-=-\n')
num = int(input('Primeiro termo = '))
raz = int(input('Razão = '))
i = 1
user = 10
res = num

while user != 0:
	i = 1
	while i <= user:	
		print(' {} ->' .format(res), end='')
		res += raz
		i 	+= 1
	print(' end')
	user = int(input('\nQuer adicionar mais termos? Digite o nº de termos ou 0 para sair. '))
	
print('Programa saiu com Sucesso!')