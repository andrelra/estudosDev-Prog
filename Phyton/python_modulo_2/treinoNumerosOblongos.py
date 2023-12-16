#Números oblongos tem a forma n(n+1), e representam figuras retangulares.

multiplicando = int(input('Entre com um número natural qualquer: '))
multiplicador = multiplicando + 1
indice = (multiplicando * multiplicador) // 2
produto = multiplicador * multiplicando
for i in range(1, multiplicador + 1):
    print('* ' * multiplicando)

soma = (indice ** 2) + indice
print('Númbero oblongo: {};'.format(multiplicando * multiplicador))
print('O número {} é o {}º número natural par.'.format(produto, indice))
print('A soma dos {} primeiros números naturais pares é: {}'.format(indice, soma))
