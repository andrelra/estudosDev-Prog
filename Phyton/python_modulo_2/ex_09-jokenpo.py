from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('''Escolha uma das opções: 
[0] Pedra;
[1] Papel;
[2] Tesoura.''')
jogador = int(input('\33[1;31m--->>\033[m '))
sleep(1)
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ')

print('\033[35mO computador escolheu:\033[m \033[1;33;40m {} \033[m.' .format(itens[pc]))

if pc == 0:
    if jogador == 0:
        print('\033[33mVocê escolheu: \33[m\033[1;32;40m {} \033[m.'.format(itens[jogador]))
        print('EMPATE!')
    elif jogador == 1:
        print('\033[33mVocê escolheu: \33[m\033[1;32;40m {} \033[m.'.format(itens[jogador]))
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('\033[33mVocê escolheu: \33[m\033[1;32;40m {} \033[m.'.format(itens[jogador]))
        print('EU VENCI!')
    else:
        print('Opção {} é inválida. Tente outra vez.' .format(jogador))
elif pc == 1:
    if jogador == 0:
        print('\033[33mVocê escolheu: \33[m\033[1;32;40m {} \033[m.'.format(itens[jogador]))
        print('EU GANHEI!')
    elif jogador == 1:
        print('\033[33mVocê escolheu: \33[m\033[1;32;40m {} \033[m.'.format(itens[jogador]))
        print('EMPATE!')
    elif jogador == 2:
        print('\033[33mVocê escolheu: \33[m\033[1;32;40m {} \033[m.'.format(itens[jogador]))
        print('VOCÊ VENCEU!')
    else:
        print('Opção  {} é inválida. Tente outra vez.' .format(jogador))
elif pc == 2:
    if jogador == 0:
        print('\033[33mVocê escolheu: \33[m\033[1;32;40m {} \033[m.'.format(itens[jogador]))
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('\033[33mVocê escolheu: \33[m\033[1;32;40m {} \033[m.'.format(itens[jogador]))
        print('EU GANHEI')
    elif jogador == 2:
        print('\033[33mVocê escolheu: \33[m\033[1;32;40m {} \033[m.'.format(itens[jogador]))
        print('EMPATAMOS!')
    else:
        print('Opção {} é inválida. Tente novamente.' .format(jogador))
