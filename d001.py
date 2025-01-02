#crie uma simples calculadora
n1 = int(input('Digite um número'))
n2 = int(input('Digite mais um número:'))
s = n1+n2
m = n1*n2
d = n1/n2
di =n1//n2
e =n1** n2
print(f'A soma é {s}, \n o produto é {m} \n e a divisão é {d:.3f}',end= ' ')
print(f'Divisão inteira {di} e potência {e}')