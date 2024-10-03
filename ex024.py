# Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "Santo"

cidade = input('Digite o nome da cidade: ')
cidadeSanto = cidade.find('Santo')

if cidadeSanto == 0:
    print(f'A cidade {cidade} começa com o nome Santo')
else:
    print(f'A cidade {cidade} não começa com o nome Santo')

