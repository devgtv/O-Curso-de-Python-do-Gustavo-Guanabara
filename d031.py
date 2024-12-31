# desenvolva um programa que pergunte a distancia de uma viagem em km 
#calcule o preço da passagem, cobrando 0.50 po km para viagens de ate 200 km
# e 0.45 para viagens mais longas.
distancia = float(input('Informe a distancia de sua viagem em km '))
menor = distancia * 0.50
maior = distancia * 0.45
if distancia <= 200 :
    print(f'O valor da passagem será de R$ {menor:.2f}')
else: 
    print(f'O valor da passagem será de R$ {maior:.2f}') 

    # caso nao queria utilizar variveis 
    # preco = distancia 