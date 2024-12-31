#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcula o preço a pagar,sabendo que o carro custa 60 por dia e 0.,15 por km rodado
dias =int(input('Informe qunatos dias ficou com o veiculo apos a locação : '))
km =float(input('Informe quantos km foram percorridos pelo veiculo : '))
preco = (60*dias)+(0.15*km)
print(f'Voce tera que pagar R${preco:.2f}')
