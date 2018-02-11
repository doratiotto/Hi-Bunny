print('-=-=-=-=- Tabuada -=-=-=-=-\n')
user = 'nada'

while True:
	user = int(input(f'Quer ver a tabuada de qual valor? '))
	if user < 0:
		break
	for i in range(1, 11, 1):
		print(f'{user} x {i :2} = {user*i}')

print('Você escolheu um número negativo - FIM!')
