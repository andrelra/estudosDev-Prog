#Seqüência de fibonacci
n = int(input('Digite um número para a seqüência: '))
# casos base:
faa = 0
fa = 1
res = 0
fx = 0
i = 0
print('{} - {}'.format(faa,fa), end= '')
while i < n:
    fx = fa + faa # 1; 5; 21
    faa = fx + fa # 2; 8; 34
    fa = faa + fx # 3; 13; 55
    print('{} - {} - {}'.format(fx, fa, faa), end = '')
    i += 1 
