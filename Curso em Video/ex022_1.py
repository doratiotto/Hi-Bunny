'''lista = nome.split( )

print(nome.upper())
print(nome.lower())
print(lista)
'''
nome = input('Digite o nome completo da Crush: ').strip()

print(nome.upper())
print(nome.lower())

print('Todo o  nome tem {} cursh letras' .format(len(nome) - nome.count(' ')))

print('Primeiro nome tem {} cursh letras' .format(nome.find(' ')))

nome = nome.split()

#print(len(''.join(nome))

#print('Todo o  nome tem {} cursh letras' .format(len(''.join(nome))))


#print('Primeiro nome tem {} cursh letras' .format(len(nome[0])))
