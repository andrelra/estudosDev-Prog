#Seqüência de fibonacci
n = int(input('Digite um número para a seqüência: '))
# casos base:
faa = 0
fa = 1
res = 0
fx = 0
i = 1
print('{} - {}'.format(faa,fa), end= '')
while i != n:
    fx = (fa) + (faa)
    faa = fx + fa
    fa = faa + fx
    print('{} - {} - {}'.format(fx, fa, faa), end = '')
    i += 1 
