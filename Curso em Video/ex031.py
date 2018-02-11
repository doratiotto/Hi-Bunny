km = float(input('km da viagem: '))

if km <= 200 :
	pr = km * 0.50
else :
	pr = km * 0.45

#pr = km * 0.50 if km <= 200 else km * 0.45

print('O preço a da passagem é R${:.2f}'   .format(pr))

#print('Último nome: {}' 	.format(nome[len(nome)-1]))