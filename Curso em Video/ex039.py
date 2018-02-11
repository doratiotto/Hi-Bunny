# Print
#from math import ceil
import datetime

'''
idade = int(input('Quantos anos você tem jovem?: '))

if idade = 18:
	print('Você deve se alistar esse ano!'))
elif idade < 18:
	print('Você é jovem ainda mas deverá se alistar quando tiver 18 anos (Em {} ano)!'))
'''

ano  = int(input('Ano de Nascimento: '))
#mes  = str(input('Mês de nascimento: ')) .strip()

anof = datetime.date.today().year
#mesf = datetime.date.today().month

dif = anof - ano

if dif == 18:
	print('Você tem que se alistar esse ano!!! Já se alistou??')
elif dif == 17:
	print('Você é jovem ainda mas deverá se alistar daqui a {} ano, em {}' .format(18 - dif, anof + 18 - dif))
elif dif < 17:
	print('Você é jovem ainda mas deverá se alistar daqui a {} anos, em {}' .format(18 - dif, anof + 18 - dif))
elif dif == 19:
	print('Você deveria ter se alstado ano passado, em {}' .format(anof - dif + 18))
else:
	print('Você deveria ter se alstado {} anos atrás, em {}' .format(dif - 18, anof - dif + 18))
