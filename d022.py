# Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas,
# o nome com todas as letras minúsculas, quantas letras ao todo (sem considerar os espaços),
# e quantas letras tem o primeiro nome.

nomepessoa = str(input('Digite o nome completo de uma pessoa :')) .strip()
maiusculo = nomepessoa.upper()
minusculo = nomepessoa.lower()
totalletras = len(nomepessoa) - nomepessoa.count(' ')
primeironome = nomepessoa.find(' ')
print(f'Seu nome em maiusculas é {maiusculo}\n seu nome em minusculas é {minusculo}\n seu nome tem ao todo {totalletras}\n Seu primeiro nome tem {primeironome} letras')
