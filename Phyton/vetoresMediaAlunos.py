num_alunos = int(input('Quantidade total de alunos: '))
nomes = []
notas = []
media = 0

for i in range(num_alunos):
    nomes.append(input('Informe o nome do {}º aluno: ' .format(i + 1)))
    notas.append(float(input('Nota do aluno {}:'.format(nomes[i]))))
    media = media + notas[i]
media = media / num_alunos
print('A média da turma é: {:.2f}'.format(media))

for i in range(num_alunos):
    if notas[i] > media:
        print('Parabéns, {}!'.format(nomes[i]))
