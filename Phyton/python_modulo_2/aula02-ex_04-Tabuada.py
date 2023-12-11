#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

n = int(input('\033[0;32;40m Digite um número para a tabuada: \033[m '))
print( '=' * 10 + ' TABUADA DE ', n, '=' * 10)
for a in range(1, 11):
    print('\033[32m{} x {:2}\033[m = \033[33m{:>3}\033[m' .format(n, a, n * a))
print('=' * 35)
