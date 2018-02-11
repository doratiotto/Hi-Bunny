print('-=-=-=-=- Média -=-=-=-=-\n')
user = 'sim'
sair = ['s', 'si', 'sim', 'outro', 'continuar']
soma = i = max = min = 0

print('Digite números para a média')
while user in sair:
	i = i + 1
	user = int(input('Digite o {}º número: ' .format(i)))
	soma += user

	if i == 1:
		max = user
		min = user
	else:
		if user > max:
			max = user
		elif user < min:
			min = user
	user = str(input('Quer digitar outro número [s/n]? ' .format(i))) .lower() .strip()

print('')
print('Foram digitados {} números' .format(i))
print('A média deles é: {:.2f}' .format(soma/i))
print('A maior foi {} e o menor foi {}' .format(max, min))
