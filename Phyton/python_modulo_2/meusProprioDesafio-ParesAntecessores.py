# O programa gera números pares antecessores a um número par e calcula a soma
# de todos eles. A nomenclatura: P20 = Par + índice (2) de um número par.
print('#' * 30)
num = int(input('\033[1;33mDigite um número par:\033[m '))
print('#' * 30)
check = num % 2
if check != 0:
    print('\033[31mEsse número não é par. Tente de novo\033[m.')
    exit()
indice = num // 2
total = 0
par = num
soma = 0
for i in range(indice + 1, 0, -1):
    if par >= 2:
        total += 1
        soma += par
        print('\033[34mP{}|\033[m\033[33m{}\033[m' .format(i - 1, par), end=' | ')
        par -= 2
    else:
        print('\033[31mFIM\033[m')
print('-=' * 30)
print('\033[1;31;40mTotal de números pares antecessores de {}\033[m: {}' .format(num, total))
print('SOMA TOTAL DOS ANTECESSORES: \033[1;32m{}\033[m' .format(soma))
print('-=' * 30)
print('\033[4;36m{:^20}' .format('Programa criado por André Arôncio'))
