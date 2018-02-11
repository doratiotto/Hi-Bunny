from time import sleep
from random import randint

print('-=-=-=-=- Par ou Impar -=-=-=-=-\n')
user = 'nada'
valid = [ 'p', 'i']
n = 0
pytho = randint(0, 5)
uNum = 0
#print(pytho)

while True:
	# Verifica se entradas são válidas
	user = str(input('Você escolhe par ou impar [p/i]? ')) .lower() .strip() [0]
	while user not in valid:
		user = str(input('Escolha direito! Você escolhe par ou impar [p/i]? ')) .lower() .strip() [0]
	uNum = int(input('Qual número vai jogar de 0 a 5? '))
	while uNum < 0 or uNum > 5:
		user = int(input('Escolha direito! Qual número vai jogar de 0 a 5? ')) 
	# Verifica se o usuário ganhou e continua // Caso não para
	print('JO')
	sleep(1)
	print('KEN')
	sleep(1)
	print('PO!!!')

	if (user == 'p' and (uNum + pytho) % 2 == 0) or (user == 'i' and (uNum + pytho) % 2 == 1):
		print(f'Você ganhou! Eu tinha escolhido {pytho}')
		print(f'{uNum} + {pytho} = {uNum + pytho} que é par' if (uNum + pytho) % 2 == 0 else f'{uNum} + {pytho} = {uNum + pytho} que é impar')
		print('')
		print('Vamos de novo!!! (^L^)')
		n += 1
	else:
		print(f'Você perdeu! Eu tinha escolhido {pytho}')
		print(f'{uNum} + {pytho} = {uNum + pytho} que é par!' if (uNum + pytho) % 2 == 0 else f'{uNum} + {pytho} = {uNum + pytho} que é impar!')
		break

print('')
if n == 0:
	print(f'Você não me venceu nenhuma vez (^L^)')
elif n == 1:
	print(f'Você me venceu {n} vez (^L^)')
else:
	print(f'Você me venceu {n} vezes (^L^)')