#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metros = int(input('Digite o valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000

print(f'O valor em metros é: {metros} \n Em centimetros: {centimetros} \n Em milimetros: {milimetros}')