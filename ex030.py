# Escreva um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.

num = int(input('Digite um numero: '))

if num % 2 == 0:
    print(f'O número escolhido foi: {num} \n Ele é um número par')
else:
    print(f'O numero escolhido foi: {num} \n Ele é um numero ímpar')