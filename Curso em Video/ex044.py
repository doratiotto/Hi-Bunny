# Print
#from math import ceil

print('=-=-=-=-=-=- Lojas LuLU =-=-=-=-=-=-')

p = float(input('Preço: R$'))
print('\n1) À vista (Dinheiro/Cheque); \n2) À vista (Cartão); \n3) 2x no Cartão; \n4) 3x (ou mais) no cartão.')
i = input('\nEscolha a forma de pagamento:')

if i == '1':
	print('\nPreço final (10% Desconto): R${:.2f}' .format(p - p*0.1))
elif i == '2':
	print('\nPreço final (5% Desconto): R${:.2f}' .format(p - p*0.05))
elif i == '3':
	print('\nPreço final (0% Desconto): R${:.2f}' .format(p))
elif i == '4':
	print('\nPreço final (20% Juros): R${:.2f}' .format(p + p*0.2))
else:
	print('\nEsolha uma forma de pagamento válida usando seu número correspondente')
