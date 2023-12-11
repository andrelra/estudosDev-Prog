#Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a
#a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 
#2 metros quadrados.

#1º passo: receber valores de Altura, Largura, rendimento e demãos:
l = float(input("Largura: "))
a = float(input('Altura: '))
r = float(input('Rendimento de cada litro por metro quadrado: '))
d = int(input('Quantidade de demãos: '))

#2º passo: Cálcular a área da parede e multiplicá-la pelo número de demãos.
area = l * a * d

#3º passo: Calcular a quantidade de tinta, dividindo a área pelo valor do rendimento por metro quadrado.
q = area / r
#4º passo: mostrar o resultado na tela.
print('-' * 30)
print('Área: {}, Demãos: {}, Rendimento: {} metros quadrados por litro.' .format(area, d, r)) 
print('Serão precisos {} litros de tinta.' .format(q))