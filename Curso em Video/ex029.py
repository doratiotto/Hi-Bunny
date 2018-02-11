from random import randint

x = 80

n = float(input('Velocidade registrada: '))
m = (n - x)*7

if n > x :
	print('O veículo foi multado em R${:.2f}' .format(m))
print('Tenha um bom dia, dirija com segurança!')

#print('Último nome: {}' 	.format(nome[len(nome)-1]))