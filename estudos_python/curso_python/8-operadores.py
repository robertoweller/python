"""
Desafio 008
Escreva um programa que leia um valor em metros e mostre
e exiba convertido em centímetro e mililitros.
"""
metros = float(input("Um distância em metros: "))

km = metros/1000
hm = metros/100
dam = metros/10
dm = metros*10
centimitros = metros*100
milimitros = metros*1000

print(
    f'A medida de {metros}m corresponde a\n'
    f'{km}km\n'
    f'{hm}hm\n'
    f'{dam}dam\n'
    f'{dm}dm\n'
    f'{centimitros:.0f}cm\n'
    f'{milimitros:.0f}mm')
