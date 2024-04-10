# Progressão aritmética
# Os 10 primeiros números
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n = 1
pa = 0
while n < 11:
    pa = t + r
    print('\033[32mP{}:\033[m \033[43m {} \033[m'.format(n, pa), end=' | ')
    t += r
    n += 1