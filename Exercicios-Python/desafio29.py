# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km\h mostre uma mensagem dizendo 
# que ele foi multado
# A multa vai custar R$7,00 por cada KM acima do limite

velocidade = float(input('Digite a velocidade do carro: '))

if velocidade >80:
    print(f'Voê está acima do limite!')
    calculoMulta = velocidade - 80
    multa = calculoMulta*7.00
    print(f'A multa é : R$ {multa}')
elif velocidade == 80:

    print(f'Ciudado, você está no limite de velocidade e pode ser multado!')

else:

    print(f'Você esta abaixo do limite de velocidade!')
