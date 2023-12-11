#Nessa aula, vamos aprender operações com String no Python.
# As principais operações que vamos aprender são o Fatiamento de String,
# Análise com len(), count(), find(), transformações com replace(), upper(),
# lower(), capitalize(), title(), strip(), junção com join().

### imprimeito texto na tela

#print("""Nessa aula, vamos aprender operações com String no Python.
#As principais operações que vamos aprender são o Fatiamento de String,
#Análise com len(), count(), find(), transformações com replace(), upper(),
#lower(), capitalize(), title(), strip(), junção com join().""")

### FATIAMENTO

#frase = 'André Luiz Ribeiro'

#print(frase[0::2])

### COUNT

#frase = 'André Luiz Ribeiro Arôncio'

#print(frase.count('A'))
#print(len(frase))

#Conta quantos caracteres tem na frase e exclui os espaços na contagem:

#frase = "    André Luiz Ribeiro Arôncio   "
#print('Quantidade de caracteres com os espaço é {}. ' .format(len(frase)))
#print('Quantidade de caracteres excluídos os espaços é {}' .format(len(frase.strip())))

### usando o 'REPLACE' para alterar dados da variável

#frase = 'André Luiz Ribeiro Aron'

#print(frase.replace('Aron', 'Arôncio' ))

#Alterando a variável:
#frase = frase.replace('Aron', 'Arôncio')
#print(frase)

### COMANDO 'IN' - Verifica se um ou mais caractere está na frase:

frase = 'André Luiz Ribeiro Arôncio'
print('Luiz' in frase)
print('Feio' in frase)

### COMANDO 'FIND' - retorna a posição (índice) em que o caracetere está:

#frase = 'André Luiz Ribeiro Arôncio'
#print('A palavra selecionada está na posição {}.' .format(frase.find('Luiz')))

#retornando o índice de caractere em minúscula ou maiúscula:

#print(frase.lower().find('luiz')) # sem o 'lower()' o programa retorna '-1' (como 'false');

### COMANDO SPLIT: Dividindo os elementos e criando uma lista:

#frase = 'André Luiz Ribeiro Arôncio'
#print(frase.split())

# outro recurso com split + consulta a lista criada por este comando:

#frase = 'André Luiz Ribeiro Arôncio'
#dividido = frase.split()
#print(dividido)
#print(dividido[2][3]) # Pega o terceiro ítém da lista e retorna somente o caractere '3' do ítem.
