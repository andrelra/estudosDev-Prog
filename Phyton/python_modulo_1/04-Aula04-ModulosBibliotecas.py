#-------------------------------------------------------------#
#               importando módulos                            #
#-------------------------------------------------------------#
#Raiz quadrada

#from math import sqrt, floor
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)

#print('A raiz de {} é igual a {}.' .format(num, raiz))

#importando sem a especificar a função ao usá-la: altera-se para: form math import sqrt ao invés do módulo inteiro (import math)

#raiz = sqrt(num) #não precisa mais especificar o módulo, mas somente a função 'sqrt'.

#print('A raiz de {} é igual a {}.' .format(num, raiz))

#importanto dois métodos (sqrt e floor)

#raiz = sqrt(num)
#print('A razi de {} é igual a {}.' .format(num, floor(num))) # O 'floor' arredonda o valor.

# GERANDO NÚMEROS ALEATÓRIOS

import random
#num = random.random() # Gera de 0 a 1, com pontos flutuantes.
#print(num)

num = random.randint(1, 50) # Gera números inteiros dentro do intervalo especificado
print(num)