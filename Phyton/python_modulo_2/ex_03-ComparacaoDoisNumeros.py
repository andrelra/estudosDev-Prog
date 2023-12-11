num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro número ({}) é maior que o segundo número ({}).' .format(num1, num2))
elif num2 < num1:
    print('O primeiro número ({}) é menor que o segundo número ({}).' .format(num1, num2))
else:
    print('Os números são iguais!')
