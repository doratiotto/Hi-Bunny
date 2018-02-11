Dia = int(input('Quantos dias de aluguel? '))
Km  = int(input('Quantos kilometros foram rodados?'))

p = Dia*60 + Km*0.15

print('O valor a pagar é R${:.2f}' .format(p))
