#faça um programa que leia tres numeros e mostre qual e o maior e qual e o menor
n1  = float(input('Digite o primeiro número '))
n2  = float(input('Digite o segundo número '))
n3  = float(input('Digite o terceiro número '))
maior = max(n1,n2,n3)
menor = min(n1,n2,n3)
print(f'O maior número é {maior}\n O menor número é {menor}')