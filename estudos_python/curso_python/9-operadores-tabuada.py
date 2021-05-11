"""

Desafio 009
Faça um programa que leia um número inteiro qualquer e mostre
na tela a sua tabuada.

"""
t = int(input('Digite o número para ver sua tabuada: '))

print('-'*13)
for sla in range(1, 11):
    print(f'{t} x {sla:2} = {t*sla}')

print('-'*13)