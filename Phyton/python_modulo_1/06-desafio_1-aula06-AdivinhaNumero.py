# Escreva um programa que faça o computador pensar em um número inteiro
# entre 0 e 5, e peça ao usuário descobrir o valor escolhido pelo computador.
# O programa deverá escrever na tela se o usuário ganhou ou perdeu.

from random import randint
from time import sleep
print('-=' * 30)
print('Vou pensar num número. Tente adivinha-lo.')
print('-=' * 30)

num = int(input('Entre 0 e 5, adivinhe o número que eu pensei: '))
pc = randint(0, 5)
print('Processando...')
sleep(3)

if num == pc:
    print('Você digitou {}. Pensei no número {}. VOCÊ GANHOU! Parabéns!' .format(num, pc))
else:
    print('Você digitou {}. Pensei no número {}. VOCÊ PERDEU! Tente de novo.' .format(num, pc))
