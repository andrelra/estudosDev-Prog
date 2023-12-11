#Faça um programa que calcule a soma entre todos os números ÍMPARES que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        vla = s
        s += c
        cont += 1
        print('{} + {} = {}'.format(c, vla, s))
print('Total de múltiplos de 3: {}' .format(cont))
print('Total da soma dos múltiplos de 3: {}' .format(s))

# a variável 'vla' armazena o valor anterior (VaLorAnterior) da soma de 's' (s += c).
