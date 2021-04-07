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
    # Porque a função escreve já esta sendo chamado por outra chamada
    # escreve()

    # E só agora você que chamar a função, mas não que passar argumento
    passando()


def escreve(arg):
    print(arg)


roda()
