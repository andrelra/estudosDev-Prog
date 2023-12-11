# Escreva um programa que pergunta a distância de uma viagem em km;
# Calcule o preço da passagem, cobrando R$, 0,50 por km para viagens de
# até 200km, e R$ 0,45 para viagens mais longas.

km = int(input('Digite a distância em km: '))

'''if km <= 200:
    preco = 0.50
else:
    preco = 0.45
print('Distância: {}km.\nPreço: R$ {}.' .format(km, km * preco))'''

############## IF SIMPLIFICADO - (MODO TERNÁRIO) #########################
preco = km * 0.50 if km <=200 else km * 0.45
print('Distância: {}km.\nPreço: R$ {}.' .format(km, preco))
