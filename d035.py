#desenvolva um programa que leia o commprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a = float(input('Informe o primeiro  segmento: '))
b = float(input('Informe o segundo segmento:'))
c = float(input('Informe o terceiro segmento:'))
if a  < b + c and b < a + c and c < a + c : 
    print('é possível formar um triângulo')
else : 
    print('Não é possível formar um triângulo')
