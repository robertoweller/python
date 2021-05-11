"""
Desafio 008
Escreva um programa que leia um valor em metros e mostre
e exiba convertido em centimetro e milimitros.
"""
metros = float(input("Digite o valor em mentros: "))

km = metros/1000
hm = metros/100
dam = metros/10
dm = metros*10
centimitros = metros*10**2
milimitros = metros*10**3

print(
    f'A medida de {metros:.1f}m corresponde a\n'
    f'{km}km\n'
    f'{hm}hm\n'
    f'{dam}dam\n'
    f'{dm}dm\n'
    f'{centimitros}cm\n'
    f'{milimitros}mm')
