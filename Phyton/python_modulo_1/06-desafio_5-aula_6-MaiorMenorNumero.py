# Faça um programa que leia três número e mostre-nos qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite um terceiro número: '))
##############################################
#               SOLUÇÃO LONGA                #
##############################################
#checa o maior
'''if n1 > n2 and n1 > n3:
    print('O maior número é o: ', n1)
elif n2 > n1 and n2 > n3:
    print('O maior número é o: ', n2)
else:
    print('O maior número é o: ', n3)
#checa o menor
if n1 < n2 and n1 < n3:
    print('O menor é ', n1)
elif n2 < n1 and n2 < n3:
    print('O menor é o ', n2)
else:
    print('O menor é o ', n3)'''
##############################################
#               SOLUÇÃO CURTA                #
##############################################
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('O maior número é o ', maior)
print('O menor número é o ', menor)
