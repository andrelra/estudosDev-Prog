# Escreva um programa que leia um ano qualquer e informe se ele é bissexto ou não.

## NOTA: Há duas condições:
## 1ª) O ano não pode terminar em 00;
## 2ª) O ano tem que ser divisível por 4;
## Assim, não importa se o ano é 00 somente: ele também tem que ser divisível por 4.

from datetime import date

ano = int(input('Digite um ano qualquer, ou digite 0 (zero) para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!' .format(ano))
else:
    print('O ano {} NÃO é bissexto!' .format(ano))

