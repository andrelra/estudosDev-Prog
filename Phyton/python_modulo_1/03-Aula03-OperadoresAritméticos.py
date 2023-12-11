#----------------------------------------------------------------------#
#                  Ordem de precedência dos Operadores                 |
#----------------------------------------------------------------------#

# (1º) - PARENTESES - ();
# (2º) - EXPONENCIAÇÃO - **;
# (3º) - MULTIPLICAÇÃO - *; DIVISÃO REAL - /; DIVISÃO INTEIRA - //; RESTO DA DIVISÃO - %;
# (4º) - SOMA - +; SUBTRAÇÃO - -.

#conta = 4 * 5 + 8 ** 2
#print(conta)

#conta_2 = 18 % 3 + (10 / 2) // 2
#print(conta_2)

#----------------------------------------------------------------------#
#                  Macetes com a função PRINT                          #
#----------------------------------------------------------------------#

#nome = input("Digite seu nome: ")
#print('Seu nome é {:^15}' .format(nome)) #Limita o texto a 15 caracteres e centraliza (^).
#print('Seu nome é {:>15}!' .format(nome)) #Alinha o texto à direita.
#print('Seu nome é {:<15}!' .format(nome)) #Alinha o texto à esquerda.
#print('=' * 30)

#----------------------------------------------------------------------#
#                  OPERAÇÃO DENTRO DO FORMAT                           #
#----------------------------------------------------------------------#

n1 = int(input("Digite um número: "))
n2 = int(input('Digite outro número: '))
#print('A soma de {} e {} é {}' .format(n1, n2, n1+n2))
#Faz-se isso quando não se precisa armazenar o valor de uma operação numa variável.

# outros recursos com print e operadores
soma = n1 + n2 #01
mult = n1 * n2 #02
div = n1 / n2 #03
div_i = n1 // n2 #04
exp = n1 ** n2 #05
exp_func = pow(n1, n2) #06

#print('A soma é {}, a multiplicação é {}, a divisão real é {}, a divisão inteira é {}, a exponenciação é {} e a exponenciação por função é {}.' .format(soma, mult, div, div_i, exp, exp_func))

#Pode-se limitar o número de casas decimais da divisão real, como em 4/3:

#print('A soma é {}, a multiplicação é {}, a divisão real é {:.3f}, a divisão inteira é {}, a exponenciação é {} e a exponenciação por função é {}.' .format(soma, mult, div, div_i, exp, exp_func))
#No exemplo ({:.3f}), limitamos a 3 casas decimais (após a vírgula);

# ---- QUEBRANDO A LINHA ( \n ) ------

print('A soma é {}; \n A multiplicação é {}; \n A divisão real é {:.3f}; \n A divisão inteira é {}; \n A exponenciação é {}; \n A exponenciação por função é {}.' .format(soma, mult, div, div_i, exp, exp_func))