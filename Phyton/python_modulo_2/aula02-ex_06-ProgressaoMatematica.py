# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))

decTermo = t + (10-1) * r
for i in range(t, decTermo + r, r):
    print(i, end=' ')
