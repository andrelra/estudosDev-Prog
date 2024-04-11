#Seqüência de fibonacci
n = int(input('Digite um número para n primeiras triplas de números da seqüência: '))
# casos base:
faa = 0
fa = 1
fx = 0
i = 0
print("{} - {} - " .format(faa, fa), end= '')
while i != (n - 2):
    fx = fa + faa
    faa = fx + fa
    fa = faa + fx
    print('{} - {} - {} - ' .format(fx, faa, fa), end = '')
    i += 1 
