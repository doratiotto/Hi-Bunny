'''
co = float(input('cateto op = '))
ca = float(input('cateto ad = '))

#hip = sqrt(co**2 + ca**2)
hip = (co**2 + ca**2)**(1/2)

print('Cateto op = {} \nCateto ad = {}\nHipotenusa = {:.2f}' .format(co, ca, hip))
'''

import math

co = float(input('cateto op = '))
ca = float(input('cateto ad = '))

hip = math.hypot(co, ca)

print('Cateto op = {} \nCateto ad = {}\nHipotenusa = {:.2f}' .format(co, ca, hip))
