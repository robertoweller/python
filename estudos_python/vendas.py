dicio = {
    "0": False,
    "1":True,}


# Vai procurar o que tem dentro da biblioteca
usu = dicio[input("Digite algo: ")]


while usu:
    print(f"{usu=}")
    # Vai procurar o que tem dentro da biblioteca
    usu = dicio[input("Digite algo: ")]

