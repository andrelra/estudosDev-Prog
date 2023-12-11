# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

cont = 0
for i in range(1, 7 + 1):
    ano = int(input('Ano de nascimento da {}ª pessoa: ' .format(i)))
    idade = date.today().year - ano
    print('Idade: {}' .format(idade))
    if idade >= 18:
        cont += 1
print('Quantidade de maioridades: {}\nQuantidade de menoridades: {}' .format(cont, 7 - cont))
