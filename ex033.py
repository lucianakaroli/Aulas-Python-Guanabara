# Faca um programa que leia 3 numeros e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero diferente: '))
num3 = int(input('Digite outro numero diferente: '))


if num1 < num2 and num3:
    menor = num1
if num2 < num1 and num3:
    menor = num2
if num3 < num1 and num3:
    menor = num3

if num2 < num1 and num2 > num3:
    meio = num2
if num2 < num3 and num2 > num1:
    meio = num2
if num1 < num2 and num1 > num3:
    meio = num1
if num1 < num3 and num1 > num2:
    meio = num1
if num3 < num2 and num3 > num1:
    meio = num3
if num3 < num1 and num3 > num2:
    meio = num3

if num3 > num1 and num3 > num2:
    maior = num3
if num2 > num1 and num2 > num3:
    maior = num2
if num1 > num2 and num1 > num3:
    maior = num1

print(f'Os numeros escolhidos foram: {num1}, {num2} e {num3} \n Menor numero: {menor} \n Numero do meio: {meio} \n Maior numero: {maior}' )