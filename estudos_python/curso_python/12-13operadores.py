"""
Desafio 012
Faça um algoritimo que leia o preço de um produto
e mostre seu novo preço com 5% de desconto.
"""

preco = input('Digite o preço do produto: ')
# Com desconto de 5%
produto = int(preco)-(int(preco)*5)/100

print(f'Produto com desconto de 5% ${produto}')

"""
Desafio 013
Faça um algoritmo que leia o salário de um 
funcionário e mostre seu novo salário, com 15% de aumento.

"""

salario  = input("Digite seu salário: ")
# Salário com 15% de almento
almento = int(salario) + (int(salario)*15)/100

print(f'Seu saláro com almento de 15% ${almento}')