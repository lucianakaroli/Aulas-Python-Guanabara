# Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o 
# ultimo nome separadamente

nome = input('Digite o nome completo: ')

divisaoNome = nome.split()
primeiroNome = divisaoNome[0]
ultimoNome = divisaoNome[-1]

print(f'Primeiro Nome: {primeiroNome} \n Ultimo Nome: {ultimoNome}')