def ideia():
    # Variaveis principais
    nomes = []
    cantores = []
    n_tocadas = []
    letras = {}
    opcao = -1

    print("---ProgFy: O melhor streaming de música---")
    print("---Cadastro de músicas---")

    while True:
        ##Inicio do item a)

        ##Fim do item b)
        print("---Menu principal---")
        print("1 - Tocar música")
        print("2 - Calcular audiência")
        print("3 - Qual é a música?")
        print("0 - sair.")

        while opcao != 0:
            opcao = int(input("Digite a opção desejada:>"))
            if opcao == 1:
                pass
                ##inicio do item b)

                ##Fim do item b)
            elif opcao == 2:
                pass
                ##Inicio do item c)

                ##fim do item c)
            elif opcao == 3:
                pass
                ##Inicio do item d)

                ##Fim do item d)
            elif opcao == 0:
                print("Encerando a execução...")
            else:
                print("Opção incorreta. Opções disponiveis")
                print("1 - Tocar música")
                print("2 - Calcular audiência")
                print("3 - Qual é a música?")
                print("0 - sair.")


def letra():
    print("Digite Crtl+C para parar de digitar:\n")

    # Cada linha será um item da lista
    musica = []
    try:
        while True:
            digitando = input("")
            musica.append(digitando)

    except KeyboardInterrupt:

        print("\n\nDocumento salvo a lista de musicas!")

    return musica


def nomes(usuario):
    non = []
    # non vai ter todos os cantores
    non.append(usuario)
    pass


def menu():
    """
    Onde sempre vai estar rodando
    """
    opcoes = [letra]
    while True:

        print(
            """
        Digite uma opção por favor:
        1 - Tocar música
        2 - Calcular audiência
        3 - Qual é a música?
        0 - sair.
        
        """
        )

    pass


# print(letra())


# letra_musica = input("")

# linhas = letra_musica.split()

# todas_linhas = map("\n", linhas)

# print(linhas)
