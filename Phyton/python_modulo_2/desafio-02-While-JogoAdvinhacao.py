from random import randint
n = int(input('\033[46mEscolha um número de 1 a 10:\033[m '))
quant_palpites = 1
pc = randint(1,10)
while n != pc:
    if pc > n:
        print('\033[41m Baixo.\033[m')
        n = int(input("Tente outra fez: "))
        quant_palpites += 1
    elif pc < n:
        print('\033[41mAlto.\033[m')
        n = int(input("Tente outra fez: "))
        quant_palpites +=1

print('\033[30;43mVoce acertou! O número escolhido foi o \033[m \033[45m {} \033[m'.format(pc))
print('\033[33mQuantidade de palpites: \033[m \033[45m {} \033[m'.format(quant_palpites))
