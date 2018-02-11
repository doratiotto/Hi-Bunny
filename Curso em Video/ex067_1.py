print('-=-=-=-=- Tabuada -=-=-=-=-\n')
user = 'nada'
booo = True

while booo: #True
	user = int(input(f'Quer ver a tabuada de que valor? '))
	if user < 0:
		booo = False
	else:
		for i in range(1, 11, 1):
			print(f'{user} x {i :2} = {user*i}')

print('Você escolheu valor negativo - FIM!')
