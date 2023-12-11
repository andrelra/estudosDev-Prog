# Escreva um programa que leia o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a
# R$ 1.250,00 calcule um aumento de 10%; para inferiores ou iguais
# o aumento é de 15%.

##############################################
#                   MODO 1                   #
##############################################
'''salario = float(input('Salário: '))

if salario > 1.250:
    percentual = 10
else:
    percentual = 15

percentual = percentual / 100
aumento = percentual * salario
print('O valor do novo salário será de R$ {:.2f} reais.' .format(salario + aumento))'''

##############################################
#                   MODO 2                   #
##############################################
salario = float(input('Digite o salário atual: R$ '))
if salario <= 1250:
    novoSal = salario + (salario * 15 / 100)
else:
    novoSal = salario + (salario * 10 / 100)
print('O novo salário é de: R$', novoSal)

###### MEU COMENTÁRIO SOBRE O EXERCÍCIO:

# O percentual de aumento para ambos gera uma ilusão: quem tem menor percentual de reajuste
# ganhará mais do que o outro, que tem maior percentual.