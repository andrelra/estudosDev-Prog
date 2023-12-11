sal = float(input('Qual o salário do funcionário: R$'))
perc = float(input('Digite o percentual de aumento: %'))
novo_sal = sal + (sal * perc / 100)
print('O salário de R${:.2f}, com {} porcento de aumento, agora será no valor de R${:.2f}.' .format(sal, perc, novo_sal))
