# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Informe quanto de dinheiro voce tem para converter em dolares R$ '))
dolar = real/6.04
print(f'voce pode comprar US${dolar:.2f} dolares')