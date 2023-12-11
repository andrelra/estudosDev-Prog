#Faça um programa que leia o nome completo de uma pessoa
#mostrando, em seguida, o primeiro e o último nome separadamente.

nome = input('Digite um nome completo: ').strip()
divide = nome.split()
print('O primeiro nome é: {} ' .format(divide[0]))
print('O último nome é: {} ' .format(divide[-1]))

