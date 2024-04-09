# Um programa que leia o sexo de uma pessoa, mas só aceita 'M' ou 'F'.
# Caso isso não ocorra, solicitar a digitação novamente, até obter o valor correto do usuário.

'''s = str(input('Digite o sexo [M/F]: ')).upper()
r = 0
while r != 1:
    if s == 'M' or s == 'F':
        r = 1
        print('Entrada válida.')
    else:
        s = str(input('Entrada inválida. Digite novamente [M/F]: ')).upper()
        r = 0   
print('O sexo escolhido: {}'.format(s))'''

# Outra Forma:

''''sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Entrada inválida. Digite novamente [M/f]: ')).strip().upper()[0]
print('Sexo {} digitado com sucesso!'.format(sexo))'''

# Outra forma feita em 9 de abril de 2024 (mais tardiamente as anteriores):

sexo = str(input("Digite M para masculino ou F para feminino: ")).strip().upper()
while sexo not in "FfMm":
    sexo = str(input('Digite a letra do sexo corretamente: ')).strip().upper()
if sexo == 'M':
    masc = 'masculino'
    print('Sexo escolhido: {}'.format(masc))
else:
    fem = 'feminino'
    print('Sexo escolhido: {}'.format(fem))

