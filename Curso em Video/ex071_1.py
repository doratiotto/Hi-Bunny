from time import sleep

val0 = ['s', 'n']
val1 = ['1', '2', '3', '4']
user = 'nada'
no50 = no20 = no10 = no05 = no01 = 0
bunN = ['1010', '1111', '1212', '2424', 'lulu', 'luis']
bunS = ['1010', '1111', '1212', '2424', 'gotosa', 'bunitao']
sald = 0
i = 0

print('-♥--♥--♥- Banco da LULU BunnY -♥--♥--♥-\n')

while True:
	i = 0
	user = input('''Escolha uma opção:
		1) Login
		2) Cadastro de novo bunny \n''')

	if user == '2':
		print('♥ Seja vem vinda ao Banco BunnY! ♥')
		user = input('Digite seu bunnyNome: ') .strip() .lower()
		if user in bunN:
			input('Já existe esse bunnynome faça login: ')
			i = 1
		if i == 0 :
			bunN.append(user)
			user = input('Digite sua bunnySenha: ')
			bunS.append(user)
			print('Cadastrando')
			sleep(1)
			print('Agora você faz parte da família BunnY! :3 \n')
	elif user == '1':
		break		

buny = ''
while buny not in bunN:
	buny = input(' BunnY Nome do usuário ♥: ') .lower() .strip()

print('')

print(f'Seja ben vinda bunny {buny} ^L^')
senh = input('Digite sua bunnySenha: ')

while senh != bunS[bunN.index(buny)]:
	senh = input('Sua bunnySenha está errada, tente novamente -.- \n')

while True:
	user = input('''
Digite a opção desejada:
	[ 0 ] Ver Saldo:
	[ 1 ] Saque:
	[ 2 ] Depósito (ps: não funciona):
	[ 3 ] Ver piada:
	[ 4 ] Sair:
	''')

	if user == '0':
		user = input(f'Acho que esquecemos o seu saldo, aqui diz R${sald}. Está correto? [s/n] \n')  .strip() .lower()
		while user not in val0:
			user = input(f'Está certo ou não PORRA?! [s/n] \n') .strip() .lower()

		if user == 'n':
			sald = int(input(f'Qual era o saldo então??? \n'))
			print('Corrigindo... ou quase..')
			sleep(2)
			print(f'Novo saldo: {sald}')
			sleep(1)

		else:
			print('Sabia que estava certo, tenho ótima memória (°ʖ°)')
			sleep(2)

	if user == '1':
		saqu = int(input('Qual o valor do saque? (Não usamos moedas tá!) \nR$'))
		print('Verificando saldo na conta :3')
		sleep(1)
		if saqu < 0:
			print('Sacar um número negativo seria um Depósito! Use a opção correta bunny!')
		if saqu == 0:
			print('Parabéns: saque de zero reais feito com sucesso!')
		if sald >= saqu >= 0: 
			sald = sald - saqu
			while saqu > 0:
				if saqu > 50:
					no50 = saqu // 50
					saqu = saqu %  50
				if saqu > 20:
					no20 = saqu // 20
					saqu = saqu %  20
				if saqu > 10:
					no10 = saqu // 10
					saqu = saqu %  10
				if saqu > 5:
					no05 = saqu // 5
					saqu = saqu %  5
				if saqu < 5:
					no01 = saqu
					saqu = 0
			print('Saindo $ DINHEIROS $:')
			sleep(3)
			print('Calma! eu to contando aqui!!!')
			sleep(1)
			if no50 > 0:
				print(f'	Notas de R$50: {no50}')
			if no20 > 0:
				print(f'	Notas de R$20: {no20}')
			if no10 > 0:
				print(f'	Notas de R$10: {no10}')
			if no05 > 0:
				print(f'	Notas de R$5: {no05}')
			if no01 > 0:
				print(f'	Notas de R$1: {no01}')
			print(f'\n♥ Novo saldo: R${sald} ♥\n')
		else:
			print(f'Seu saldo de R${sald} é insuficiente para sacar R${saqu}, veja seu saldo novamente!')

	elif user == '2':
		print('Eu disse que não funcionava -.-" ')
		sleep(2)
		depo = int(input('Mentirinha! \nQual o valor quer depositar? R$'))
		sald += depo
		print('Conferindo depósito... peraí..')
		sleep(2)
		print(f'Certinho! Novo saldo: R${sald}')
		sleep(1)

	elif user == '3':
		print('toc toc... esqueci, deixa queto!')
		sleep(2)

	elif user == '4':
		break

print('♥ Saiu com sucesso, volte sempre ♥ ')
