# Comparação com o FOR
'''for c in range(1, 10):
    print(c)
print('Fim')'''
'''c = 0
while c < 10:
    c += 1
    print(c)
print('Fim')'''
# Quando se sabe o limite do laço, pode-se usar qualquer um, embora o 'for' se faz com poucas linhas
# Contudo, quando não se sabe o limite, somente o 'while' é a solução.
'''n = 0
r = ''
while r != 'N':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar [S/N]: ')).upper()
print('Fim!')'''

# Retornar o total de números pares digitados e de números ímpares digitados:

n = 1
par = impar = 0
while n !=0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Acabou!')
print('Total de números pares: {}\nTotal de números ímpares: {}'.format(par, impar))
        