# Repetir uma exibição na tela:

'''for l in range(1, 5):
    print('Oi')'''

# Marcando cada iteração:

'''for i in range(1, 5):
    print('Iteração: {} - Texto' .format(i))'''

#Contagem regressiva:

'''for r in range(6, 0, -1):
    print('Iteração: {} - Texto' .format(r))
print('Local para um comando fora da identação do laço. ')'''

#Pulando de 2 em dois:

'''for r in range(0, 12, 2):
    print('Iteração: {} - Texto' .format(r))
print('FIM')'''

#Laço baseado numa entrada do usuário.
#O laço terminará no antecessor do número digitado:
'''n = int(input('Digite um número: '))
for i in range(0, n):
    print('Iteração: {} - Texto' .format(i))'''

#Para o laço terminar exatamente no número digitado:
'''n = int(input('Digite um número: '))
for i in range(0, n + 1):
    print('Iteração: {} - Texto' .format(i))'''

#Para o laço parar no sucessor:
'''n = int(input('Digite um número: '))
for i in range(1, n + 2):
    print('Iteração: {} - Texto' .format(i))'''

#Usuário escolha 3 parâmetros: início, fim e o passo (pular ou seguir de quanto em quantos números.

'''i = int(input('Número inicial do intervalo: '))
f = int(input('Número final do intervalo: '))
p = int(input('Número do passo para o intervalo: '))

for c in range(i, f+1, p):
    print('Iteração: {} - Texto' .format(c))'''

# comando de leitura num laço:

'''for c in range(0, 3):
    n = int(input('Digite um número: '))
print('FIM')'''

# somando os valores lidos:

s = 0
for c in range(0,3):
    n = int(input('Digite um número: '))
    s += n
    print('Iteração: {} - Soma: {}' .format(c, s))
print('Total: {}' .format(s))

