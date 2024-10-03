#Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
#desse angulo

import math
angulo = float(input('Digite o valor do angulo: '))

sen = math.sin(math.radians(angulo))

cos = math.cos(math.radians(angulo)) 

tg = math.tan(math.radians(angulo))

print(f'O angulo {angulo}, tem o seno: {sen:.2f}, o cosseno: {cos:.2f}, e a tangente: {tg:.2f}')