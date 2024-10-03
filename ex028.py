# Escreva um programa que faça o computador pensar em um numero inteiro de 0 a 5 e peca para o 
# usuario tentar descobrir qual foi o numero escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu.

import random


num = int(input('Descubra qual o numero de 0 a 5: '))
comp = random.randint(0,5)
if num == comp:
    print(f'Parabéns, você acertou o numero: {num}')
else:
    print(f'Voce errou, o numero escolhido pelo computador foi: {comp}')
    

