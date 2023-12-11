#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Kilômetros percorridos: km'))
dias = int(input('Quantidade de dias de uso: '))

#Optei por usar duas variáveis para que os custos fossem retornados separadamente na tela para o usuário
#valorKm = 0.15 * km
#valorDias = 60.00 * dias

#print('Total por km rodado: R$ {:.2f};\nTotal por dias rodado: R${:.2f};\nTotal a pagar: R$ {:.2f}' .format(valorKm, valorDias, valorKm + valorDias))

#Forma com mesmos variáveis

valor = (0.15 * km) + (dias * 60)

print('Total a pagar: R$ {}.' .format(valor))


