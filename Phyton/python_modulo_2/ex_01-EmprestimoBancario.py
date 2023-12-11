# Escreva um programa que avalia as condições de aprovação de um empréstimo bancário a uma pessoa para
# a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar. Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário, pois,
# do contrário, o programa negará o empréstimo.

vl_casa = float(input("Digite o valor da casa:R$ "))
sal = float(input("Digite o salário do cliente:R$ "))
tempo = int(input("Quantidade de anos para o pagamento: "))

vl_parc = vl_casa / (12 * tempo)
limite = (sal * 30) / 100

if vl_parc > limite:
    print('\033[1;31mNegado!\n\033[m Valor das parcelas: \033[1;32m R$ {:.2f}\033[m.\n Quantidade de parcelas:\033[33m {}\033[m.\033[1;31m\nLimite de 30% (R$ {})do salário excedido.\033[m' .format(vl_parc, 12 * tempo, limite))

else:
    print('\033[1;33m APROVADO! \033[m Parcelas mensais de \033[1;32m R$ {:.2f}\033[m; Quantidade de parcelas: \033[1;32m{}\033[m.' .format(vl_parc, 12 * tempo))
