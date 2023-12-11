# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

altura = float(input('Altura: '))
peso = float(input('Peso: '))

colors = {'yel': '\033[33m', 'red': '\033[31m', 'fim': '\033[m'}

imc = peso / (altura ** 2)

print('{}IMC:{} {}{:.2f}{}' .format(colors['yel'], colors['fim'], colors['red'], imc, colors['fim']))

if imc <= 18.5:
    cat = 'Abaixo do Peso.'
elif 25 > imc > 18.5:
    cat = 'Peso Ideal!'
elif 30 > imc > 25:
    cat = 'Sobrepeso.'
elif 40 > imc >= 30:
    cat = 'Obesidade.'
else:
    cat = 'Obesidade Mórbida'

print('Categoria de IMC: {}{}{}' .format(colors['yel'], cat, colors['fim']))
