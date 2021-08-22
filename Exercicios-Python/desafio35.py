# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS
# E DIGA SE ELAS PODEM FORMAR UM TRÂNGULO OU NÃO

# A SOMA DE DOIS LADOS TEM QUE SER MAIOR QUE O TERCEIRO LADO

reta1 = int(input("DIGITE O TAMANHO DA PRIMEIRA RETA: "))
reta2 = int(input("DIGITE O TAMANHO DA SEGUNDO RETA: "))
reta3 = int(input("DIGITE O TAMANHO DA TERCEIRO RETA: "))

lista = [reta1, reta2, reta3]

maior = max (lista)


if reta1 < maior and reta2 <maior:
    triangulo = reta1 + reta2
if reta2 <maior and reta3 < maior:
    triangulo = reta2 + reta3
if reta1 < maior and reta3<maior:
    triangulo = reta1 + reta3

if triangulo > maior:
    print(f'O trêngulo pode ser formado')
else:
    print(f'O triangulo não pode ser formado')
   