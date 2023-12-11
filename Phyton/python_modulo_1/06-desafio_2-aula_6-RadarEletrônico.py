# Escreva um programa que leia a velocidade de um carro. Se ele
# ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi
# multado. O valor da múlta é de R$ 7,00 para cada km acima do limite.

vel = int(input('Digita a velocidade em que o carro estava, em km: '))
print('-=' * 30)
if vel > 80:
    print('Você excedeu o limite de velocidade de 80km.')
    print('Velocidade: {}km.\nMulta: R$ {}.' .format(vel, (vel - 80) * 7.00))
print('-=' * 30)
print('TENHA UM BOM DIA! Dirija com segurança.')
