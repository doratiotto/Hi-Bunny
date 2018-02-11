#Code1 - Se sim, se não 
from datetime import date

ano = int(input('Digite o Ano desejado (Digite zero para o ano atual): '))
if ano == 0:
	ano = date.today().year

if (ano %4 == 0 and ano % 100 != 0) or ano % 400 == 0:
	print('O ano {} é bissesto'   .format(ano))
else: 
	print('O ano de {} NÂO é bissesto'   .format(ano))
	
#Code2 - Se não, se sim
n = int(input('Ano: '))

if (n % 100 == 0 and n % 400 != 0) or n%4 != 0:
	print('O ano {} não é bissesto' .format(n))
else:	
	print('O ano {} é bissesto' .format(n))

