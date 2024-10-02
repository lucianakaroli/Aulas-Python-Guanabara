# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro 
# custa R$60 por dia e R$0,15 por Km rodado.

kmPercorrido = float(input('Digite a quantidade de Km percorridos: '))
qtdDias = int(input('Digite a quantidade de dias que o carro foi alugado: '))

custoDias= qtdDias * 60
custoKmPercorrido = kmPercorrido * 0.15
precoTotal = custoDias + custoKmPercorrido

print(f'Sabendo que o custo total de dias foi de: R$ {custoDias} e o de Km percorridos foi de: R$ {custoKmPercorrido}, O valor total do aluguel é de: {precoTotal}')