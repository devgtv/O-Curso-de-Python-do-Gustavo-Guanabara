# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

preco = float(input('Infome salário do funcionário :  '))
desconto = float(input('Informe quanto de aumento em %  gostaria de dar ao funcionario : '))
preconovo = preco+(desconto/100 *preco)
print(f'o novo valor do produto é {preconovo:.2f}')
