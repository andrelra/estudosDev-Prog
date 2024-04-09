# PRIMEIRO PASSO:
# PEGAR AS NOTAS.
# SEGUNDO PASSO:
# PROCESSAR A MÉDIA.
# TERCEIRO PASSO:
# ANALISAR SE O ALUNO PASSOU OU REPROVOU E MOSTRAR NA TELA (PRINT)

Nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
média = (nota1 + nota2) / 2
if média >= 7:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')

