# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 para cada km acima do limite.


velocidade = float(input('Informe a velocidade do veiculo: '))
preco = (velocidade - 80)*7
if velocidade <= 80 :
    print('Boa viagem')
else:
    print(f'voce foi multado por excesso de velocidade e tera que pagar {preco}')