"""
    Escreva um programa que receba com parâmetro
de entrada um número inteiro de 5 dígito no 
intervalo fechado [10000, 3000] que represente 
código de produtos vendidos em uma loja. Crie uma
funçao para validar os dados de entrada, obrigando
o usuário a respeitar o intervalo e o tipo de 
dado (inteiro).
    Crie uma função que calcule e retorne o dígito
veridicador do código, utilizando a regra de 
cáculo explicada a seguir. Por exemplo, considere
o código 21853, em que cada dígito é multiplicado
por um peso começando em 2, os valores obtidos são,
e do total obtido calcula-se o resto de sua divisão 
por 7.
--------------------------------------------------------------------------------
    Dígito     |   2   |   1   |   8    |   5   |   3   |
     Peso      |   2   |   3   |   4    |   5   |   6   |
 Multiplicação |   4   |   3   |   32   |   25  |   18  | Soma total = 82
               |       |       |        |       |       | Resto de 82 por 7 = 5
--------------------------------------------------------------------------------
    Retorne na função o valor do dígito verificador
calculado e imprima na tela o código do produto dígito
verificador sepado por hífen, como: 21853-5.
"""


def validated(e):
    # Se for número.
    if e.isnumeric():

        if int(e) >= 10000 and int(e) <= 30000:

            # Os prints são opcionais, porque o exercicio não pede
            # print("Valor está dentro do aceitavel")

            return True
    
    return False

def main(code=21853):

    # Deixando como o exercicio pede
    code = str(code)
    total = 0

    # Entrada do usuario também é opcional, porque o exercicio não pede
    # codigo = input("Digite o código: ")

    # Se validou.
    if validated(code):
        for i in range(2, 7):
            # Vai multiplicar cada um dos caracteres
            # e acrescentar ao valor total
            total += int(code[(i - 2)]) * i

        # código do produto
        p = f"{code}-{total % 7}"
        print(p)

        return total


if __name__ == "__main__":
    main('11166')
