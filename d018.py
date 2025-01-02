# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

num = float(input('Digite um número : '))
from math import sin,cos,tan,radians    
num_rad = radians(num)
seno = sin(num_rad)
cosseno = cos(num_rad)
tangente = tan(num_rad)
print(f'O valor do seno {seno:.2f}\n cosseno {cosseno:.2f} \n tangente {tangente:.2f}') 