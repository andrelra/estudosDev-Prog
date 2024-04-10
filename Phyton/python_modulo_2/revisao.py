#Seqüência de fibonacci
n = int(input('Digite um número para a seqüência: '))
# casos base:
f1 = 0
fx = 0
i = 0
print('{}, {}'.format(f1,fx), end= ' | ')
while i != n:
    fx = (f1 + 1) + (fx) # 0 + 1 + 0 = 1;
    print('{}'.format(fx), end = ' | ')
    i += 1 
