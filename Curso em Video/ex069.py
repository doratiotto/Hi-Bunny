print('-=-=-=-=- Cadastro de Usuários -=-=-=-=-\n')
user = 'nada'
i = 1
id18 = home =  mu20 = 0
val1 = ['f', 'm']
val0 = ['s', 'n']

while True:
	nome = str(input(f'Pessoa {i}: ')) .lower() .strip()
	idad = int(input('Idade: '))
	sexo = str(input('Sexo: ')) .lower() .strip() [0]
	while sexo not in val1:
		sexo = str(input('Sexo: ')) .lower() .strip() [0]
		 
	if idad > 18:
		id18 += 1
	if sexo == 'm':
		home += 1
	if sexo == 'f' and idad < 20:
		mu20 += 1
	
	user = ''
	while user not in val0:
		user = str(input('Cadastrar outra pessoa? [s/n] \n')) .lower() .strip()
	if user =='n':
		print('Fim de Cadastro! \n')
		break
	i += 1
		
print(f'''Pessoas com mais de 18 anos: {id18} 
Homens: {home}
Mulheres com menos de 20 anos: {mu20} 

^L^ valid''')

