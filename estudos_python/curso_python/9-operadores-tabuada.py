"""

Desafio 009
Faça um programa que leia um número inteiro qualquer e mostre
na tela a sua tabuada.

"""
t = int(input('Digite o número para ver sua tabuada: '))

risco = lambda r='-', q=13: print(f"{r}"*q) 

risco()

for sla in range(1, 11):
    print(f'{t} x {sla:2} = {t*sla}')

risco()
