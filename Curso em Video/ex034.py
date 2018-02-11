#Code1 - Usando max e min de uma lista de valores 
sal = float(input('Salário: '))

if sal<=1250:
	print('(15%) Com aumento de R${:.2f}´, o novo Salário é: R${:.2f}' .format(sal*0.15, sal +sal*0.15))
else:
	print('(10%) Com aumento de R${:.2f}´, o novo Salário é: R${:.2f}' .format(sal*0.1, sal +sal*0.1))
