# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
print('\033[34m{:=^90}\033[m' .format(' LOJA ANDRÉ ARÔNCIO '))
vl_produto = float(input('Valor das compras: R$ '))
frm_pgto = int(input('Forma de pagamento:\n(1) À vista em dinheiro\n(2) À vista no cartão\n(3) Parcelado no Cartão: '))

if frm_pgto == 1:
    desc = (vl_produto * 10) / 100
    total = vl_produto - desc
    print('Desconto: R$ {}\nTotal a pagar: R$ {:.2f}' .format(desc, total))
elif frm_pgto == 2:
    desc = (vl_produto * 5) / 100
    total = vl_produto - desc
    print('Desconto: R$ {:.2f}\nTotal a pagar: R$ {:.2f}' .format(desc, total))
elif frm_pgto == 3:
    qParc = int(input('Quantidade de Parcelas no cartão: '))
    if qParc <= 2:
        vl_parc = vl_produto / qParc
        print('''Desconto: \033[31mSem desconto\033[m
        Quantidade de Parcelas: {}
        Valor das parcelas: R$ {:.2f}
        Total a pagar: R$ {:.2f}''' .format(qParc, vl_parc, vl_produto))
    if qParc > 2:
        juros = (vl_produto * 20) / 100
        total = vl_produto + juros
        vl_parc = total / qParc
        print('''Quantidade de Parcelas: {}
        \033[31mJuros: R$ {}\033[m
        Valor das parcelas: R$ {:.2f}
        Total a pagar: R$ {:.2f}''' .format(qParc, juros, vl_parc, total))
else:
    print('\033[1;31mDigite uma opção válida.\033[m')
