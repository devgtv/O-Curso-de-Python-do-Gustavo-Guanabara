#Faça um programa que leia uma frase pelo teclado e mostre : quantas vezses aparece a letra 'a' em que posição ela aprece a ultima vez e na primeira vez#
name = str(input('Informe seu nome completo : ')).upper().strip()
qtsA = name.count('A')
primeiroA = name.find('A') + 1
ultimoA = name.rfind('A') + 1
print(f'A letra A aprece {qtsA} vezes na frase')
print(f'A primeira letra A apareceu na posição {primeiroA}')
print(f'A ultima letra A apareceu na posição {ultimoA}')
