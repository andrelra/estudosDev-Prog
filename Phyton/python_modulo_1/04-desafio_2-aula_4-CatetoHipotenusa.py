#Faça um programa que leia o comprimento do cateto oposto e
#do cateto adjacente de um triângulo retângulo. Calcule e
#mostre o comprimento da hipotenusa.

# MODO TRADICIONAL COM PYTHON:

#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}.' .format(hi))

# IMPORTANDO A BIBLIOTECA HYPOT DO MÓDULO MATH

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa vai medir {:.2f}.' .format(hypot(co, ca)))

