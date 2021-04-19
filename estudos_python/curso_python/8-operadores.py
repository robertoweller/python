"""
Desafio 008
Escreva um programa que leia um valor em metros e mostre
e exiba convertido em centimetro e milimitros.
"""
metros = int(input("Digite o valor em mentros: "))

centimitros = metros*10**2
milimitros = metros*10**3

print(f'{centimitros=}\n{milimitros=}')
