# Faca um programa que leia um ano qualquer e mostre se é bissexto.

ano = int(input('Digite o ano: '))
 
if ano % 4 == 0:
    print(f'O ano {ano} é bixesto')
else:
    print(f'O ano {ano} não é bixesto')