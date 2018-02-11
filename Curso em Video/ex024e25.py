'''
n = str(input(''))
nome = .strip()

print('palavra' in nome)
nome = nome.split()
print('palavra' in nome[1])

'''
nome = str(input('Digite um nome: ')).strip()
#print('Tem lua no primeiro nome? {}' .format('lua' in nome[:3]))

nome = nome.lower().split()

print('Tem lua no nome? {}' .format('lua' in nome[0:3]))	
print('Tem lua no primeiro nome (incluso)? {}' .format('lua' in nome))