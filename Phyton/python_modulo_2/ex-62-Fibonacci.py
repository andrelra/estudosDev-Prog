#Seqüência de fibonacci - os 20 primeiros números.
n = 8
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
