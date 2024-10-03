# Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# considere U$ 1.00 = R$ 3.27

valor = float(input('Digite quantos reais voce tem na carteira: '))
dolar = valor / 3.27

print(f'Voce pode comprar um total de U$: {dolar:.2f}')