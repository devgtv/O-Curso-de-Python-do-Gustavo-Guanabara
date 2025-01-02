#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
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
