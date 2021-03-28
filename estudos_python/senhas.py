lista = []

beckup = []

#


while True:
    resposta = input("Login > ")
    senha = input("Pass> ")
    usuario_senha = f"{resposta}      {senha}"
    lista.append(usuario_senha)

    if len(lista) == 2:
        print("adicionou 2")
        for cada in lista:
            # Desinpacotar
            beckup.append(cada)

        lista.clear()

    if len(beckup) == 4:

        print("\nLogin      Senha")
        for login in beckup:
            print(login)

    # print(f"{beckup=}")
