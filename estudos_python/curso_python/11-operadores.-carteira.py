"""
Desafio 011
Faça um programa que leia a largura e altura de
uma parede e mostre, calcule a sua área e a 
quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta um área de 2m².

"""
altura = float(input("Altura: "))
largura = float(input("Largura: "))

area = altura*largura


quant = area*4

print(f'Tem uma area de {area} metros, vai precisa de {quant} litros para pintar')
