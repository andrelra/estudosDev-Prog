##############################################
#                   NOTAS                    #
##############################################

# Código ANSI (Scape Sequence):
# Começar o código de cor: \033[
# Fechar o código de cor: \0033[m
# Entre o colchete ([) e o 'm' ficará o código da cor.
# EXEMPLO:
#   \033[CÓDIGO DO ESTILO;CÓDIGO DO TEXTO; CÓGIDO DO BACKGROUNDm
#   \033[0;33;44m        - '0' indica 'sem estilo;
# CÓDIGOS PARA ESTILO NO PYTHON: 0 (nenhum), 1 (negrito - bold), 4 (underline) e 7 (inverte - negativo)
# CÓDIGOS PARA CORES NO PYTHON: 30 (Branco), 31 (Vermelho),32 (verde), 33 (amarelo, 34 (azul), 35 (magenta)
# 36 (ciano), 37 (o padrão: cinza).

# 1ª FORMA: DIRETO NO TEXTO OU VARIÁVEL:
'''print('\033[1;30;41mOLá mundo!\033[m')
print('\033[33mOlá MUndo!\033[m') #penas cor amarela ao texto.

a = 10
b = 8
print('Os valores são \033[34m{}\033[m e \033[34m{}\033[m.' .format(a, b))

nome = 'André Luiz'
print('Olá, seja bem vindo, {}{}{}!' .format('\033[4;33m', nome, '\033[m'))'''

# 2ª FORMA: DICIONÁRIO (LISTA)
cores = {'limpa': '\033[m', 'amarelo_sublinhado': '\033[4;33m', 'verde': '\033[32m', 'azul': '\033[34m'}
nome = 'André Luiz'
print('Olá! Seja Bem Vindo, {}{}{}!' .format(cores['amarelo_sublinhado'], nome, cores['limpa']))

