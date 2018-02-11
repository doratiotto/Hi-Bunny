# Print
#from math import ceil
n1 = float(input('n1 = '))
n2 = float(input('n2 = '))
n3 = float(input('n3 = '))

m = (n1 + n2 + n3)/3

if 0 < m < 5:
	print('Média: {:.2f} - Reprovado' .format(m))
elif 5 <= m < 6:
	print('Média: {:.2f} - Recuperação' .format(m))
elif 6 <= m <= 10:
	print('Média: {:.2f} - Aprovado' .format(m))
else:
	print('Tem algo errado nessa nota final {:.2f}' .format(m))
