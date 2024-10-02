# Faca um algoritmo que leia o preco de um produto e mostre seu novo preco com 5% de desconto

preco = float(input('Digite o preco do produto: '))
semdesc = preco
porDesc = (preco * 0.05)
comDesc = preco - porDesc
print(f'O preço total do produto é: {semdesc} \n Com desconto é: {comDesc}')