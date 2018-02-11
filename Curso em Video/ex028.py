from random import randint
from time import sleep

#x = 1	
print('-=-' * 20)
print('Estou pensando num número inteiro de um a cinco... ')
print('-=-' * 20)
sleep(1)

x = randint(1, 5)
n = int(input('Tente adivinhar, qual número eu pensei? '))

print('PROCESSANDO...')
sleep(1)

if int(n) == x:
	print('Acertou! pensei no número', x)
else :
	print('ERROU!!! pensei no número', x)

#print('Último nome: {}' 	.format(nome[len(nome)-1]))