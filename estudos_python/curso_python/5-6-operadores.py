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
