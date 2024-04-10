# Fatorial de um número

n = int(input('Digite um número inteiro positivo: '))
num = n
f = 1
while n != 1:
    f = f * n * (n - 1)
    n -=2
    if n == 0:
       n = 1
print('o fatorial de {} é: {}'.format(num, f))
