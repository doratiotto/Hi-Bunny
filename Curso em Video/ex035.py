#Code1 - Se sim, se não 
r0 = float(input('reta 1: '))
r1 = float(input('reta 2: '))
r2 = float(input('reta 3: '))
lista = [r0, r1, r2]

M = max(lista)
#m = lista.index(max(lista))
#lista.pop(m)
lista.remove(M)

if sum(lista) > M:
	print('Existe um triângulo Euclidiano com os lados dados "Yeeey"')
else:
	print('Não existe um triângulo Euclidiano com os lados dados "ahhh!!"')

'''
if r0 + r1 < r2 and r0 + r2 < r1 and r1 + r2 < r0:
	print('Existe um triângulo Euclidiano com os lados dados "Yeeey"')
else:
	print('Não existe um triângulo Euclidiano com os lados dados "ahhh!!"')
'''