#A Confederação Nacional de Natação precisa de um programa que leia o
# ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date
ano = int(input("Ano de nascimento: "))
aHoje = date.today().year
idade = aHoje - ano
cores = {'limpa': '\033[m', 'amarelo': '\033[33m', 'verde': '\033[32m', 'azul': '\033[34m'}

if idade <= 9:
    cat = "MIRIM"
elif idade <= 14:
    cat = "INFANTIL"
elif idade <= 19:
    cat = "JÚNIOR"
elif idade <= 25:
    cat = "SENIOR"
else:
    cat = "MASTER"

print('{}Idade: {}{}\n{}Categoria: {}{}' .format(cores['azul'], idade, cores['limpa'], cores['amarelo'], cat, cores['limpa']))
