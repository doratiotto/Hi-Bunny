import math #Importa biblioteca matemática mais avançada para Raiz

Preço = float(input('Preço de tabela R$'))
desconto = 0.05

Pdesconto = 0.05 * Preço
nPreço    = Preço - Pdesconto

print('Com desconto de {:.0f}% o preço é de R${:.2f}' .format((100*Pdesconto), nPreço))
