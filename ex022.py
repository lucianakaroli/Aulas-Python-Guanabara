# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - o nome com todas as letras maiusculas.
# - o nome com todas minusculas.
# - quantas letras ao todo(sem considerar espacos).
# - quantas letras tem o primeiro nome.

nome = (input('Digite seu nome completo: '))

nomeMaiuscula = nome.upper()
nomeMinuscula = nome.lower()
nome.strip

espaco = nome.count(' ')
qtdLetras = len(nome)
qtdLetrasTotal = qtdLetras - espaco
primeiroNome = len(nome.split()[0])


print (nomeMaiuscula, nomeMinuscula, qtdLetrasTotal, primeiroNome)

