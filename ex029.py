# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$ 7.00 por cada Km acima da velocidade.

vel = float(input('Digite a velocidade do carro: '))
multa = (vel - 80) * 7 

if vel > 80:
    print(f'Velocidade acima do permitido! Sua velocidade é: {vel} \n Multa de R$ {multa}')
else: 
    print('Dentro da velocidade permitida!')