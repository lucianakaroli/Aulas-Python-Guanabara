# Faca um programa que leia uma frase pelo teclado e mostre:
# - quantas vezes aparece a letra "A"
# - em que posicao ela aparece a primeira vez
# - em que posição ela aparece a ultima vez

frase = input('Digite uma frase qualquer: ')

numerosA = frase.count('a')
primeiraPos = frase.find('a')
ultimaPos = frase.rfind('a')

print(f'Na frase: {frase},\n letra A aparece: {numerosA} vezes, \n Primeira Posicao: {primeiraPos}, \n Ultima Posicao: {ultimaPos} ')