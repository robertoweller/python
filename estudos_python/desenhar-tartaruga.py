def roda():
    """
    Eu quero passar a string, mas não quero chamar a função escreve
    """
    escreve("String como argumento!")

    # Porque a função escreve já esta sendo chamado por outra chamada
    escreve()


def escreve(arg):
    print(arg)


roda()
