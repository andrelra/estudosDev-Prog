#Crie um programa que leia o nome de uma pessoa
#e diga se ela tem 'Silva' no nome.

nome = input('Digite um nome completo: ').strip()
proc = 'SILVA' in nome.upper()

if proc == True:
    print('Há Silva no nome? SIM')
else:
    print('Há Silva no nome? NÃO')
