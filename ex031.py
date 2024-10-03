# Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preco da passagem
# cobrando R$ 0.50 por km para viagens até 200km e R$ 0.45 para viagens mais longa.

dist = float(input('Digite a distancia de uma viagem em km: '))

if dist <= 200:
    precoPassagem1 = dist * 0.50
    print(f'O valor da passagem será de: R$ {precoPassagem1}')
elif dist > 200:
    precoPassagem2 = dist * 0.45
    print(f'O valor da passagem será de: R$: {precoPassagem2}')
