print('-=-=-=-=- Somatório -=-=-=-=-\n')
user = soma = i = 0

print('Digite números ou 999 para sair')
while user != 999:
	i = i + 1
	soma += user
	user = int(input('Digite o {}º número: ' .format(i)))
i = i - 1	# Não contando 999

print('')
print('Foram digitados {} números' .format(i))
print('O Somatório é: {}' .format(soma))