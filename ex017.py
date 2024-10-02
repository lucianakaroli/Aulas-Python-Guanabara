#Faca um programa que leia o comprimeiro do cateto oposto e do cateto adjacente de um triangulo,
#calcule e mostre o comprimento da hipotenusa

import math


catop = int(input('Digite o valor do cateto oposto: '))
catad = int(input('Digite o valor do cateto adjacente: '))
hipotenusa = (catad ** 2 + catop ** 2)

calculoHip = math.sqrt(hipotenusa)
print(f'O calculo do cateto oposto {catop} e cateto adjacente {catad}, dá o valor da hipotenusa: {calculoHip}')