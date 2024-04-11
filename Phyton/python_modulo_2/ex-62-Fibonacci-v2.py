#Seqüência de fibonacci - os 20 primeiros números.
n = int(input('\033[033mQuantos primeiros núemros da seqüência de Fibonacci você quer conferir? Digite aqui: \033[m '))
faa = 0
fa = 1
fx = 0
i = 0
print("\033[42m {} \033[m - \033[42m {} \033[m - " .format(faa, fa), end= '')
while i != (n - 2):
    fx = fa + faa
    faa = fa 
    fa = fx     
    print('\033[42m {} \033[m - ' .format(fx), end = '')
    i +=1
print(' \033[41m -- Fim -- \033[m')