"""
Agora que você sabe usar Python para fazer o trabalho para você, 
faça uma função que receba como entrada um texto e o número n de repetições 
desejado e retorne uma sequência de caracteres composta por n repetições deste 
texto.
"""


def entrada_texto(texto, repeticoes):
    for i in range(repeticoes):
        print(f"{i+1}.{texto}")


p = input("Diga: ")
q = int(input("Quantas vezes que repetir? "))
entrada_texto(p, q)