# Depois de raciocinar sobre como criar os dois primeiros casos bases da série automaticamente
# cheguei neste resultado:
n = int(input('\033[033mQuantos primeiros núemros da seqüência de Fibonacci você quer conferir? Digite aqui: \033[m '))
#Casos bases:
faa = 0
fa = 0
fx = 0
# Contador:
i = 0
#laço:
while i != (n - 2):
    if i == 0:
        fx = 0
        fa = 1
        print('\033[42m {} \033[m - ' .format(fx), end = '')
    elif i == 1:
        fx = 1
        print('\033[42m {} \033[m - ' .format(fx), end = '')
        fa = 1 
    fx = fa + faa
    faa = fa 
    fa = fx     
    print('\033[42m {} \033[m - ' .format(fx), end = '')
    i +=1
print(' \033[41m -- Fim -- \033[m')