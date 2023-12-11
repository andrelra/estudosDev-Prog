#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.

# (1º) Usando a função floor, que arredonda para baixo um número com casas decimais.

#from math import floor

#num = float(input('Digite um número de tipo real: '))
#print('O número {} arredondado é {:.0f}.' .format(num, floor(num)))

# (2º) Usando a função trunc

#from math import trunc

#num = float(input('Digite um número de tipo real: '))
#print('O número {} arredondado é {}.' .format(num, trunc(num)))

# (3º) SEM IMPORTAR MÓDULO

num = float(input('Digite um número de tipo real: '))
print('A parte inteira do número {} é  {}.' .format(num, int(num)))




