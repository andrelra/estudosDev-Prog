#Faça um algorítimo que leia um número de 0 a 9999 e mostre na
#tela cada um dos dígitos separados (Unidade; Dezena; Centena; Milhar)

#### MODO MATEMÁTICO DE FATIAMENTO DO NÚMERO
#num = int(input('Digite um número de 0 a 9999: '))
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10

#print('Unidade: {}' .format(u))
#print('Dezena: {}' .format(d))
#print('Centena: {}' .format(c))
#print('Milhar: {}' .format(m))

# Modo com estrutura condicional

num = str(input('Digite um número 0 a 9999: '))
t = len(num)
print('O número {} tem {} caracteres.' .format(num,t))

if num == ' ':
    print('Você não digitou.')
elif t == 1:
    print('Unidade: ', num[0])
elif t == 2:
    print('Unidade: {};\nDezena: {}.' .format(num[1], num[0]))
elif t == 3:
    print('Unidade: {};\nDezena: {};\nCentena: {}.' .format(num[2], num[1], num[0]))
elif t == 4:
    print('Unidade: {};\nDezena: {};\nCentena: {};\nMilhar: {}. ' .format(num[3], num[2], num[1], num[0]))
else:
    print('Digite um número válido, de até 4 dígitos.')


