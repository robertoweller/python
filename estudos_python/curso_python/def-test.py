def v1(ss):
    """
    soma de variavel, mas já está declarada
    """
    var = ss
    outra = 0

    if var == 5:
        outra += 1
        var = 0
        input(f"Atingiu {outra} vez! Parabéns!")
        vari = 0

        return vari


def main():
    vari = v1()

    while True:
        vari += 1

        v1(vari)


main()