# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
# Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
n1 = int(input('Informe um numero entre 0 e 5 '))
n2 = randint(0,5)
if n1 != n2: 
    print('Voce perdeu')
else:
    print('Voce ganhou')   
