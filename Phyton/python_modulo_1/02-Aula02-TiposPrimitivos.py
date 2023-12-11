#n1 = int(input('Primeiro número: '))
#n2 = int(input('Segundo número: '))
#soma = n1 + n2
#print('A soma de ' + str(n1) + ' e ' + str(n2) + ' é ' + str(soma) + '.')
#print('A soma vale, ', soma)
#print('A soma entre', n1, 'e', n2, 'é', soma)

#No primeiro caso, de concatenação, foi necessário converter as variáveis numéricas em strings na função print
#Usando o format
#----------------------------------------------------------------------#
#          SINTAXE NOVA - DO PYTHON 3 - USANDO MÁSCARAS (chaves {})    |
#----------------------------------------------------------------------#

#print('A soma de {} e {} é {}'.format(n1, n2, soma))

#A solução com format não precisou converter as variáveis de números de tipo inteiros em string

#------------------------------------ 
#Sem o especificar o tipo de variável, a soma vai concatenar

#n1 = input('Primeiro número: '))
#n2 = input('Segundo número: '))
#soma = n1 + n2

#print("A soma entre ", n1, 'e', n2, 'é', soma)

#----------------------------------------------------------------------#
#                      USANDO VARIÁVEL BOOLEANA                        |
#----------------------------------------------------------------------#

#n = bool(input('Degite um valor: v'))
#print(n)

#Se o usário digitar um valor, seja número ou letra, o python retorna 'true', se não, retorna 'false'

n = input("Digite um valor: ")
#print(n.isnumeric()) #Retornar 'True' se o usuário digitar um valor número, e 'false' para outros valores.
#print(n.isalpha()) #Retorna 'True' se o usuário digitou letra.
print(n.isalnum()) #Retorna 'True' para alfa-numéricos

