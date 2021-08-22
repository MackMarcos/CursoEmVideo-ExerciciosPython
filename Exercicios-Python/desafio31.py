# Desenvolva um programa que pergunte a distância de uma viagem em KM
# Calcule o preço da passagem cobrando R$0.50 por km até 200KM
# e R$0.45 para viagens acima de 200km

import re

distancia = input('Digite a distância da sua viagem: ')

distancia = re.sub('[^0-9]', '' , distancia)

distancia = int(distancia)


if distancia <= 200:
    preco = distancia * 0.50
    print(f'O valor da passagem é: R$ {preco}')
else:
    preco = distancia * 0.45
    print(f'O valor da passagem é: R$ {preco}')