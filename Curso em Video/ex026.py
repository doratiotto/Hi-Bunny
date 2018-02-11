'''
n = str(input(''))
nome = .strip()

print('palavra' in nome)
nome = nome.split()
print('palavra' in nome[1])

'''
frase = str(input('Digite uma frase: ')) .strip().lower()

print('A letra "a" aparece {} vezes na frase' .format(frase.count('a')))

print('Aparece a primeira vez no espaço {}' .format(frase.find('a',0,) + 1))

print('Aparece a última vez no espaço {}'  .format(frase.rfind('a',0,) + 1))


'''
nA = frase.count('a') + frase.count('A')

print('A letra "a" aparece {} vezes na frase' .format(nA))

print('Aparece a primeira vez no espaço {}' .format(frase.find('a',0,)))

print('Aparece a última vez no espaço {}'  .format(frase.rfind('a',0,)))
'''