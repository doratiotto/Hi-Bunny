print('-=-=-=-=- Produtos -=-=-=-=-\n')
i = 1
prod = proB ='produto'
preç = preF = preB = proK = 0
val1 = ['s', 'n']
user = 'nada'

while True:
	prod = str(input(f'Produto {i}: ')) .lower() .strip()
	preç = float(input('Preço: '))
	while preç < 0:
		preç = float(input('Preço: '))

	if preç > 1000:
		proK += 1

	preF += preç
	
	if i == 1:
		proB = prod
		preB = preç		
	if preç < preB:
		proB = prod
		preB = preç

	user = 'nada'
	while user not in val1:
		user = str(input('Outro produto? [s/n] \n')) .lower() .strip()
	if user =='n':
		print('Terminando a compra... \n')
		break
	i += 1

print(f'''Total a pagar: R${preF :.2f};
Cupons da promoção (Produtos de 1k ou mais): {proK};
Produto mais barato: {proB} custando {preB :.2f}''')
print('''^L^ valid''')

