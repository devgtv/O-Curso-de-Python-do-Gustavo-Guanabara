#desenvolva um programa que leia o commprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo
a = float(input('Informe o tamanho da base '))
b = float(input('Informe o tamanho da lado1 '))
c = float(input('Informe o tamanho do lado2 '))
if a + b > c and a + c > b and b + c > a:
    print('é possível formar um triângulo')
else : 
    print('Não é possível formar um triângulo')
