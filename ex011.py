#Faca um programa que leia a largura e a altura de uma parede em metros, calcule sua área e 
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma area
# de 2m**2

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = 0

if area <= 2:
    print(f'Será preciso apenas 1 tinta')
if area > 2:
    print(f'Sera necessário: {area * 1/2} tintas')