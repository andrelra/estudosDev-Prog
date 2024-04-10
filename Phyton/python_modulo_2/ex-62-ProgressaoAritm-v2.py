# Progressão aritmética
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n = 1
pa = 0

while n < 11:
    pa = t + r
    print('\033[32mP{}:\033[m \033[43m {} \033[m'.format(n, pa), end=' | ')
    t += r
    n += 1
resposta = ''
c = 0
i = 0
d = 0
resposta = str(input('\nDeseja calcular mais termos? [S/N] ')).upper()
while not resposta=='N':
    i = int(input('Digite a quantidade de termos a mostrar: '))
    for c in range(1, i+1):
        pa = t + r
        print('\033[32mP{}:\033[m \033[43m {} \033[m'.format(d + c + (n -1), pa))
        t += r
        c += 1
    resposta = str(input('\nDeseja calcular mais termos? [S/N] ')).strip().upper()
    d = d + c - 1 #para continuar a contagem de 'Pn', que é posição na progressão.
