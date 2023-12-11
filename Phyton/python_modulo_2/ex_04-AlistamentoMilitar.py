# Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade:
# - Se ele ainda vai se alistar ao serviço;
# - Se é a hora de se alistar;
# - Se já passou do tempo do alistamento.
# Mostrar, também, o tempo que passou ou faltou do prazo para o alistamento.
from datetime import date
atual = date.today().year
a = int(input('Ano do teu nascimento: '))
idade = atual - a
if idade == 18:
    print('\033[34mIdade: {}\033[m\n\033[33mIdade de alistamento militar:\033[m \033[32mVIGENTE\033[m.' .format(idade))
elif idade < 18:
    saldo = 18 - idade
    print('\033[34mIdade: {}\033[m\n\033[33mIdade de alistamento militar:\033[m \033[32mFALTA(M) {} ANO(S)\033[m.' .format(idade, saldo))
    anoAlist = a + 18
    print('\033[32mAno do alistamento: {}\033[m' .format(anoAlist))
else:
    saldo = idade - 18
    print('\033[34mIdade: {}\33[m\n\033[33mIdade de alistamento militar:\033[m \033[31mHá {} ano(s).\033[m' .format(idade, saldo))
    anoAlist = a + 18

    print('\033[32mAno de alistamento: {}\033[m' .format(anoAlist))

