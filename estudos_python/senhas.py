lista = []

beckup = []

#


while True:
    resposta = input("Login > ")
    lista.append(resposta)

    if len(beckup) == 4:
        print("adicionou 4")
        for login in beckup:
            print(login)

    if len(lista) == 2:
        print("adicionou 2")
        beckup.append(lista)
        lista.clear()
