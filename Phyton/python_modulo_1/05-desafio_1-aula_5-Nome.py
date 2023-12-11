#Crie um programa que leie o nome completo de uma pessoa e mostre:
# 1) O nome com todas as letras maiúsculas;
# 2) O nome com todas as letras minúsculas;
# 3) Quantidade total de letras (sem considerar os espaços);
# 5) Quantas letras tem o primeiro nome;
nome = str(input('Digite seu nome completo: ')).strip()

print("Se nome com todas as letras maiúsculas é: {} ." .format(nome.upper()))
print('Seu nome em letras minúsculas é: {}' . format(nome.lower()))
print('A quantidade total de caracteres dele, sem espaços, é: {}' .format(len(nome) - nome.count(' ')))

nome = nome.split()
print('Seu primeiro nome é {} e ele tem {} caracteres: ' .format(nome[0], len(nome[0])))



