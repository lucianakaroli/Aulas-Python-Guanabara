# O mesmo professor do desafio anterior quer sortear a ordem aleatoria de apresentacao dos alunos.
# Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 

import random

alunos= ['Felipe', 'Flavia', 'Gabriela', 'Miguel', 'Giovana']

random.shuffle(alunos)

print(f'A ordem dos alunos para a apresentacao é: {alunos}')