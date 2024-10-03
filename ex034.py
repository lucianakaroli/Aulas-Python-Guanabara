# Calcule um programa que pergunte o salario deum funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$ 1250.00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual o valor do seu salario? '))

if salario > 1250:
    novosalario = (10/100 * salario) + salario
elif salario <= 1250:
    novosalario = (15/100 * salario) + salario

print(f'Seu salario era: {salario} e com reajuste subiu para: {novosalario}')