#import random
from random import choice

a1 = str(input('Aluno 1: '))

a2 = str(input('Aluno 2: '))

a3 = str(input('Aluno 3: ')) 

lista = [a1, a2, a3]
#n = random.choice(lista)
n = choice(lista)

#print('{}, {}, {}' .format(a1, a2, a3))
print('O aluno escolhido foi:', n)
