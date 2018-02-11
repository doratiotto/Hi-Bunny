import random

a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: ')) 
a4 = str(input('Aluno 4: ')) 

lista = [a1, a2, a3, a4]
n = random.choices(lista, [1, 2, 3, 4], k=4) 	#A sequência das entradas, peso da escolha, quantidade de escolhas
#Vish dá repetição
m = random.sample(lista, k=4) 					#A sequência das entradas, quantidade de escolhas
#Agora sem repetição 

print('A ordem de alunos com repetição é:', n)
print('A ordem de alunos sem repetição é:', m)

#random.choices([a1, a2, a3], [1, 1, 1], k=3)

# random.shuffle(lista)
# print(lista)
