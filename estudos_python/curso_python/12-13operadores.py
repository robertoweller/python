"""
Desafio 012
Faça um algoritimo que leia o preço de um produto
e mostre seu novo preço com 5% de desconto.
"""

preco = float(input('Qual o preço do produto? R$'))
# Com desconto de 5%
produto = preco * 0.95

print(f'Produto que custava R${preco:.2f}, na promoção com desconto 5% vai custar R${produto:.2f}')

"""
Desafio 013
Faça um algoritmo que leia o salário de um 
funcionário e mostre seu novo salário, com 15% de aumento.

"""

salario  = float(input("Digite seu salário: R$"))
# Salário com 15% de almento
# almento = salario + (salario*15)/100
almento = salario * 1.15
print(f'Seu saláro de {salario:.2f}, com almento de 15% vai para R${almento:.2f}')