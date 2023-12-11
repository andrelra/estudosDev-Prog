#Crie um programa que leia o nome de uma cidade e diga se ela
#começa ou não com o nome 'santo'.

city = input('Digite um nome de cidade: ').strip()
nome = city[:5].upper() == 'SANTO'
#O código acima retorna 'True' independente de o usuário usar minúsculas no nome.
if nome == True:
    print('A cidade possui a palavra santo no 1º nome.')
else:
    print('A cidade não possui a palavra santo no 1º nome.')
