print('-=-=-=-=- PA -=-=-=-=-\n')
num = int(input('Primeiro termo = '))
raz = int(input('Razão = '))
i = 1
user = 10
res = num
t = user
while user != 0:
	i = 1
	while i <= user:	
		print(' {} ->' .format(res), end='')
		res += raz
		i 	+= 1
	print(' pause')
	user = int(input('\nQuer adicionar quantos termos? '))
	t += user

print('Progressão finalizada com {} termos!' .format(t))
