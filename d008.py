# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = float(input('Digite a quantidade em metros que deseja converter para centimetros e para milimetros: '))
convertcenti = n1*100
convertmili = n1*1000
print(f'o valor de {n1} em metros para centimetros é {convertcenti} \nem milimetros{convertmili}')