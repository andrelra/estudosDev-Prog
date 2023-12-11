# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nome = input('Digite o nome do aluno: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print("Aluno: {}\nMédia: {:.1f}\nStatus: APROVADO" .format(nome, media))
elif 7 > media >= 5.0:
    print("Aluno: {}\nMédia: {:.1f}\nStatus: RECUPERAÇÃO" .format(nome, media))
else:
    print("Aluno: {}\nMédia: {:.1f}\nStatus: REPROVADO" .format(nome, media))
