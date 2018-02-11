import math

a = float(input('Qual a altura da parede em metros? '))

l = float(input('Qual a largura da parede em metros? '))

area = a * l
tinta = area / 2

print('Sua parede tem {}x{} de dimensão e {} metros quadrados' .format(a, l, area))
print('Você precisa comprar {} litros de tinta' .format(tinta))
