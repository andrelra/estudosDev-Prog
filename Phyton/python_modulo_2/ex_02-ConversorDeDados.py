# Escreva um programa que leia um número inteiro qualquer e peça ao usuário escolher qual será a base
# de conversão: 1 para binário; 2 para octal e 3 para hexadecimal.

n = int(input('\033[7;33mDigite um número para a conversão:\033[m '))
e = int(input('\033[33mEscolha um número para base de conversão:\033[m\n(1) Binário;\n(2) Octal;\n(3) Hexadecimal.\nNúmero: '))
base = " "
conv = 0
if e != 1 and e != 2 and e != 3:
    print('\033[1;0;41mEntre com um número válido.\033[m')
    exit()
elif e == 1:
    base = "Binária"
    conv = format(n, "b")
elif e == 2:
    base = "Octal"
    conv = format(n, "o")
elif e == 3:
    base = "Hexadecimal"
    conv = format(n, "x")

print('A forma {} de {} é \033[1;33m{}\033[m' .format(base, n, conv))

