preco = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite o percentual do desconto: %'))
valor_final = preco - (preco * desconto / 100)

print('O produto que custava R$ {:.2f}, com desconto vai custar R$ {:.2f}.' .format(preco, valor_final))
