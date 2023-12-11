# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA,
# A SACADA DA CASA,
# A TORRE DA DERROTA,
# O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.

########## MODO COM O LAÇO FOR #################

'''frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de \033[33m{}\033[m é \033[31m{}\033[m.' .format(frase, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo.')'''

#### OUTRO MODO, MAIS SIMPLES, DE FAZER: FATIAMENTO ######

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split() #DIVIDE A FRASE EM PALAVRAS E LANÇA-AS NUMA COLEÇÃO.
junto = ''.join(palavras) #JUNTA AS PALAVRAS SEM OS ESPAÇOS ENTRE ELAS
inverso = junto[::-1] # AQUI A DIFERENÇA: INÍCIO E FIM ZERADOS, MAS LÊ DE FRENTE PARA TRÁS (-1).
print('O inverso de \033[33m{}\033[m é \033[31m{}\033[m.' .format(frase, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo.')