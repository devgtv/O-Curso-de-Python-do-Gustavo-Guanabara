# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.


from math import hypot
co = float(input('Digite um número: '))
ca = float(input('Digite outro número : '))
hi = hypot(co,ca)
print(f'O valor da hipotenusa é :{hi:.2f}') #


#ou
#cateto1 = float(input('Digite um número: '))
#cateto2 = float(input('Digite outro número : '))
#hipotenusa = ((cateto1**2) +(cateto2**2))**(0.5) 
#print(f'O valor da hipotenusa é {hipotenusa}')