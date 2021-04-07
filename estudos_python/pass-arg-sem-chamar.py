from functools import partial


def roda():
    """
    Eu quero passar a string, mas não quero chamar a função escreve
    """
    letras = ["c", "a", "d", "f", "b", "e"]
    procura = 0
    for achou in letras:
        if achou == "d":
            # Digamos que você precise passar agora, mas não que chamar a função
            passando = partial(escreve, f"Achou! estava na posição {procura} da lista!")
        procura += 1

    # Porque por exemplo essa função será chamada por outro chamada.
    # Tipo essa chamada:
    passando()


def escreve(arg):
    print(arg)


roda()