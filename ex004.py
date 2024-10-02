# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as 
# informacoes possiveis sobre ele.

algo = input("Digite algo: ")
print('O tipo primitivo desse valor é: ', type(algo))
print('Só tem espaço? ', algo.isspace())
print('É um numero?', algo.isnumeric())
print('É alfabético? ', algo.isalpha())
print('É alfanumerico? ', algo.isalnum())
print('Está em maiusculas? ', algo.isupper())
print('Está em minusculas? ', algo.islower())
print('Está capitalizada? ', algo.istitle())