# ESCREVA UM PROGRAMA QUE PERGUNTA O SALÁRIO DE UM FUNCIONARIO E CALCULE O VALOR DO SEU AUMENTO
# PARA SALÁRIOS SUPERIORES A R$1.250,00 CALCULE UM AUMENTO DE 10%
# PARA SALARIOS INFERIOR OU IGUAL A 1.250.00 O AUMENTO É DE 15%

salario = float(input('Digite o seu Salário: '))

if salario <= 1.250:
    reajuste = salario * 0.15
    aumento = salario + reajuste
    print(f'SEU SALÁRIO COM ALMENTO É: R${aumento}')
else:
    reajuste = salario * 0.10
    aumento = salario + reajuste
    print(f'SEU SALÁRIO COM ALMENTO É: R${aumento}')







