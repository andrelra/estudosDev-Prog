# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

colors = {'yel': '\033[33m', 'red': '\033[31m', 'fim': '\033[m'}

if r1 < r2 + r3 and r2 < r1 + r3:
    print('{}Os segmentos podem formar triângulo.{}'.format(colors['yel'], colors['fim']))
    if r1 == r2 == r3:
        print('{}Forma triangular: EQUILÁTERO{}' .format(colors['yel'], colors['fim']))
    elif r1 != r2 != r3 != r1:
        print('{}Forma triangular: ESCALENO{}' .format(colors['yel'], colors['fim']))
    else:
        print('{}Forma triangular: ISÓSCELES{}' .format(colors['yel'], colors['fim']))
else:
    print('{}Os segmentos não podem formar triângulo.{}' .format(colors['red'], colors['fim']))
