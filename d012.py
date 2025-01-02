# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Infome o preço do produto : '))
desconto = float(input('Informe quanto de desconto gostaria de dar : '))
preconovo = preco-(desconto/100 *preco)
print(f'o novo valor do produto é {preconovo}')