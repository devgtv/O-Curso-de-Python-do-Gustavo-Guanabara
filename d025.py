#crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome  #
nome = str(input('Informe seu nome completo')).strip()
print(f'{('silva' in nome.lower())}')