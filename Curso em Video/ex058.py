from random import randint
# from datetime import sleep
palp = 0
num  = randint(1,10)
c = 0
print('Vou pensar em um número de 1 a 10, tente descobrir...')
print('PENSEI!!!')

palp = int(input('\n Qual seu palpite? '))

while palp != num:
	if palp < num:
		palp = int(input('\n ERROU! Qual seu próximo palpite? Dica: mais...'))
	else: 
		palp = int(input('\n ERROU! Qual seu próximo palpite? Dica: menos...'))
	c += 1


print('\n Acertou! Você errou {} vezes haha!' .format(c))