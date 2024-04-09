#Um programa que leia dois valores e mostre um menu
#na tela.

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite segundo valor: '))
menu = 0
while menu != 5:

    menu = int(input('''\033[33mEscolha uma das operações a seguir:

    MENU:

    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    \033[m
    '''
    ))
    if menu == 1:
        soma = v1 + v2
        print('Resultado da soma entre {} e {}: {}'.format(v1,v2,soma))
    elif menu == 2:
        mult = v1 * v2
        print('Produto dos números {} e {}: {}'.format(v1,v2,mult))
    elif menu == 3:
        if v1 > v2:
            maior = v1
            print('O número maior é o {}'.format(maior))
        elif v1 < v2:
            print('O número maior é o {}'.format(v2))
        else:
            print('Os números {} e {} são iguais.'.format(v1,v2))
    elif menu == 4:
        v1 = int(input('Digite outro valor: '))
        v2 = int(input('Degite o segundo valor: '))
print('Programa encerrado.')