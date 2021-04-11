from time import sleep as s


def loading(ca):
    saida = "Loading... (OK)...."
    # A linha vai se adptar ao tamanho da saida
    for i in range(len(saida)):
        s(0.1)
        print(f"{ca}", flush=True, end="")

    print(f"\n{saida}")


loading(".")