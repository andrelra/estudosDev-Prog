#Seqüência de fibonacci - os 20 primeiros números.
# Nomenclatura: 'fx' = último número; 'fa' = antecessor imediato; 'faa' = antecessor do antecessor imediato
# Assim temos as posições ordenadas: faa, fa, fx ....
n = int(input('\033[033mQuantos primeiros núemros da seqüência de Fibonacci você quer conferir? Digite aqui: \033[m '))
#Casos bases:
faa = 0
fa = 1
fx = 0
# Contador:
i = 0
#imprime casos básicos
print("\033[42m {} \033[m - \033[42m {} \033[m - " .format(faa, fa), end= '')
#laço:
while i != (n - 2):
    fx = fa + faa
    faa = fa 
    fa = fx     
    print('\033[42m {} \033[m - ' .format(fx), end = '')
    i +=1
print(' \033[41m -- Fim -- \033[m')

# algorítimo:
#
# 1º Passo: Determinar uma variável (n) para a entrada de quantidade numérica escolhida pelo usário;
# 2º Passo: Determinar duas variáveis para os casos báses (os dois primeiros número da seqüência de Fibonacci);
# 3° Passo: Determinar uma variável para cada último número (fx) no processo da seqüência;
# 4º Passo: Determinar uma variável contator para comparar com o valor de entrada (n).
# 5º Passo: Iniciar laço while comparando o contador com a variável de entrada de dados do 1º passo;
# 6º Passo: Somar os dois primeiros casos bases armazenado o resultado na variável de último número (fx);
# 7º Passo: Recuar o valor do antecessor de 'fx' (fa) para o antecessor deste (faa). Assim: faa <-- fa;
# 8º Passo: Recuar o valor de fx para a posição de seu antecessor (fa). Assim: faa <-- fa <--- fx;
# 9º Passo: Imprimir na tela o valor do último fx;
# 10º Psso: Fazer o próximo laço de n laços escolhidos no primeiro passo para o próximo calculo de fx;
# 11º Passo: Incrementar o contator (Progressão aritimética de razão 1);
# 12º Passo: Ao cabo do último laço, imprimir na tela a falavra 'Fim'.