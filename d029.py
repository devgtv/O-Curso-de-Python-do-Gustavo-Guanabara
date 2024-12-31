#escreva um programa que leia a velocidade de uma carro.
# Se ele ultrapassar em 80km/h. mostre uma mensagem dizendo que ele foi multado.
# a multa vai custar 7 reais para cada km acima do limite.

velocidade = float(input('Informe a velocidade do veiculo: '))
preco = (velocidade - 80)*7
if velocidade <= 80 :
    print('Boa viagem')
else:
    print(f'voce foi multado por excesso de velocidade e tera que pagar {preco}')