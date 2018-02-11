# Print
#from math import ceil
print('=-=-=-=-=-=- Verificador de IMC =-=-=-=-=-=-')

p = float(input('Peso = '))
a = float(input('Altura = '))

imc = p / (a**2)

if imc < 18.5:
	print('Seu imc é de {:.1f}, seu peso está abaixo do peso ideal.' .format(imc))
elif imc < 25:
	print('Seu imc é de {:.1f}, seu peso está ideal!' .format(imc))
elif imc < 30:
	print('Seu imc é de {:.1f}, seu peso está acima do peso ideal (Sobrepeso).' .format(imc))
elif imc < 40:
	print('Seu imc é de {:.1f}, seu peso está muito acima do peso ideal (Obesidade).' .format(imc))
else:
	print('Seu imc é de {:.1f}, você tem obesidade mórbida.' .format(imc))
