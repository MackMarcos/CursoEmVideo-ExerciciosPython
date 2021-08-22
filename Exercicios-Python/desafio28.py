# Escreva um programa que faça o computador "pensar"
# em um numero inteiro entre 0 e 5 e peça para o 
# usuario tentar descobrir qual foi o numero escolhido 
# O programa deverá escrever na tela se o usuário venceu
# ou perdeu
import random

numero = int(random.randint (1,5))

digitaNum = int(input('Tente adivinhar um numero de 1 até 5: '))

if digitaNum == numero:
    print(f"Parabéns você tem sorte!")
else:
    print(f'ERROUUUUU')