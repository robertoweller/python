# Variaveis principais
nomes = []
cantores = []
n_tocadas = []
letras = {}
opcao = -1

print("---ProgFy: O melhor streaming de música---")
print("---Cadastro de músicas---")

while True:
    """
    -----    Essa vai ser a saida do no terminal:    -----

        Dígite o nome da música:
        Dígite o cantor da música:
        Dígite a letra da música:
        Deseja cadastrar outra música? (1 - sim. Outro - não ): >

        Essa é a idéia, jogar no dicionario com todas as informações
        Música tocada. Nome: {nome_musica}. Cantor: {nome_cantor}. Letra: {letra_cantor}


    """
    ##Inicio do item a)
    # Perguntas do cadastros para o usuário
    nome_musica = input("Dígite o nome da música: ")
    nomes.append(nome_musica)

    nome_cantor = input("Dígite o cantor da música: ")
    cantores.append(nome_cantor)

    letra_cantor = input("Dígite a letra da música: ")

    # Vai com todas as informações da musa para o dicionário junto com a letra
    letras[
        nome_musica
    ] = f"Música tocada. Nome: {nome_musica}. Cantor: {nome_cantor}. Letra: {letra_cantor}"

    # Confirma se tem mais cadastros
    continua = input("Deseja cadastrar outra música? (1 - sim. Outro - não ): >")

    # Se não tem mais cadastros à fazer, analize os que já tem
    if continua != "1":
        ##Fim do item b)
        print("---Menu principal---")
        print("1 - Tocar música")
        print("2 - Calcular audiência")
        print("3 - Qual é a música?")
        print("0 - sair.")

        while opcao != 0:
            """
            -----    Essa vai ser a saida do no terminal:    -----

            Digite a opção desejada: > 1
            Dígite o nome de uma música: >
            ... Vai mostra a música

            """
            opcao = int(input("Digite a opção desejada: > "))
            if opcao == 1:

                ##inicio do item b)
                achar_nome = input("Dígite o nome de uma música: > ")

                # Mostra para o usuário a música já com todas as informações
                print(letras[achar_nome])

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
                quit()

            else:
                print("Opção incorreta. Opções disponiveis")
                print("1 - Tocar música")
                print("2 - Calcular audiência")
                print("3 - Qual é a música?")
                print("0 - sair.")
