"""
Desafio 011
Faça um programa que leia a largura e altura de
uma parede e mostre, calcule a sua área e a 
quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta um área de 2m².

"""
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

area = altura*largura

quant = area/2

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {quant}l de tinta')
