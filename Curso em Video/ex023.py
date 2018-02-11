n = int(input('Digite um ano de entre 0 e 9999 dígitos '))

#Forma de Texto, só aceita com 4 dígitos
#print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}' .format(ano[0], ano[1], ano[2], ano[3]))

u = n // 1    % 10
d = n // 10   % 10
c = n // 100  % 10
m = n // 1000 % 10

print('Unidade: {}' .format(u))
print('Unidade: {}' .format(d))
print('Unidade: {}' .format(c))
print('Unidade: {}' .format(m))

#print('Unidade: {}' .format(int(int(n)/1000)))
