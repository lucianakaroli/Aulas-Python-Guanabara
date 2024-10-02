# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porcao inteira
# ex: Digite um numero: 6.127. O numero 6.127 tem a parte inteira 6

import math

num = float(input('Digite qualquer numero real: '))
numInt = math.floor(num)

print(f'O número {num} tem a parte inteira: {numInt}')