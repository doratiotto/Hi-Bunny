print('-=-=-=-=- Soma -=-=-=-=-\n')
user = 'nada'
#sair = ['sair', 'exit', 'si', 'sair', 'terminar']
soma = i = 0

while True:
	user = int(input(f'Digite o {i+1}º número (ou 999 pasa sair): '))
	if user == 999:
		break
	soma += user	
	i = i + 1

print(f'\nA soma dos {i} valores é: {soma}')
