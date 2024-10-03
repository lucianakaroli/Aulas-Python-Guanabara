# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome. 

nome = input('Digite o seu nome completo: ')

temSilva = 'Silva'
if temSilva in nome:
    print(f'O nome possui Silva')
else:
    print(f'O nome não possui Silva')