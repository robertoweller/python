"""
Desafio 005
Faça um programa que leia um número
interio e mostre na tela o seu sucessor
e o seu antecessor
"""


n1 = input("Número: ")

# Se não digitar um número vai ser n1 vai ser 0.
n1 = int(n1) if n1.isnumeric() else 0

print(f"Seu sucessor é {n1 + 1} e seu antecesso é {n1 - 1}.")


"""

Desafio 006
Crie um algoritmo que leia um número e mostre o seu dobro,
triplo e raiz quadrada.


"""
print(
    f"""
E seu dobro é {n1 ** 2}, triplo é {n1**3} e 
sua raiz quadrada é {n1**.5}"""
)


"""


Desafio 007
Desenvolva um programa qu eleia as duas
notas de um aluno, calcule e mostre a média.


Desafio 008
Escreva um programa que leia um valor em metros e mostre
e exiba convertido em centimetro e milimitros.


Desafio 009
Faça um programa que leia um número inteiro qualquer e mostre
na tela a sua tabuada.


Desafio 010
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.

Considere
US$1.00 = 3.27


Desafio 011
Faça um programa que leia a largura e altura de
uma parede e mostre, calcule a sua área e a 
quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta um área de 2m².


Desafio 012
Faça um algoritimo que leia o preço de um produto
e mostre seu novo preço com 5% de desconto.


Desafio 013
Faça um algoritmo que leia o salário de um 
funcionário e mostre seu novo salário, com 15% de aumento.



"""