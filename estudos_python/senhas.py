#


def gerencia():
    """
    Aqui vai perguntar o login e senhar
    Também vai fazer o processo de salvar nas listas e exibir as senhas
    salvas
    """

    # Lista temporaria
    lista = []

    # Vai ficar salvo o beckup
    beckup = []

    while True:
        resposta = input("Login > ")
        senha = input("Pass> ")
        usuario_senha = f"{resposta}      {senha}"
        lista.append(usuario_senha)

        if len(lista) == 2:
            print("----------Salvo no beckup------------")
            # Desinpacotar a lista e adicionar ao beckup
            for cada in lista:
                beckup.append(cada)

            lista.clear()

        if len(beckup) == 4:

            print("\nLogin      Senha")
            for login in beckup:
                print(login)


# Se tiver 1 vai rodar o codigo, se 0 não
roda = 1

if __name__ == "__main__" and roda:

    gerencia()


# print(f"{beckup=}")
