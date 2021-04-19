"""

Desafio 009
Faça um programa que leia um número inteiro qualquer e mostre
na tela a sua tabuada.

"""
t = int(input('Digite o número para sua tabuada: '))

for sla in range(0, 11):
    print(f'{t} x {sla} = {t*sla}')

