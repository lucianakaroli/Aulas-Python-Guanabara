# Faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

salario = float(input('Digite seu salario: '))
porNovoSalario = (salario * 0.15)
novoSalario = salario + porNovoSalario

print(f'Seu salario era: {salario} \n Seu novo salário será: {novoSalario}')