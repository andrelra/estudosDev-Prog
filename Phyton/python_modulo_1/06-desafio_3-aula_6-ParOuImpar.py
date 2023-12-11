# Crie um programa que leia um número inteiro e
# mostre na tela se ele é par ou ímpar.

num = int(input("Digite um número inteiro: "))
resto = num % 2

if resto == 0:
    print('O número {} é um número PAR.' .format(num))
else:
    print('O número {} é um número ÍMPAR.' .format(num))
