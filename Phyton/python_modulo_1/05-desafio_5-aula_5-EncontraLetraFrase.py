#Faça um programa que leia uma frase qualquer e mostre:
# 1º) Quantas vezes aparece a letra 'A';
# 2º) Qual a sua primeira posição;
# 3º) Qual a sua última posição.

#### PRIMEIRO MODO:

#frase = input('Digite uma frase: ').strip()
#print('A letra "a" aparece {} vezes na frase. ' .format(frase.upper().count('A')))
#print('A primeira posição é: {}.' .format(frase.upper().find('A')))
#print('A última posição é: {}.' .format((frase.upper().rfind('A'))))

### SEGUNDO MODO:

frase = input('Digite uma frase: ').upper().strip()
print('A letra "a" aparece {} vezes na frase.' .format(frase.count('A')))
print('A primeira posição é a: {}' .format(frase.find('A') + 1))
print('A última posição é: {}.' .format(frase.rfind('A') + 1))

#O '+1' mostra na tela a posição com base na contagem que começa com 1 ao invés da contagem
#do computado, que começa no índice zero (0).

