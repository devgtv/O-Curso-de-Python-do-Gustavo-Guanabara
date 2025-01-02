# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1843
# EXEMPLO :  Unidade: 3, Dezena: 4, Centena: 8, Milhar: 1

num = int(input('Informe  um número :'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10 
print(f' A unidade é {u}\n A dezena é {d}\n A centena é {c}\n milhar é {m}')