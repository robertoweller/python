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

    tocadas = {}

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
    continua = input("Deseja cadastrar outra música? (1 - sim. Outro - não ): > ")

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

                # Se a mpusica estive cadastrada, exiba ela
                if achar_nome in letras:

                    # Mostra para o usuário a música já com todas as informações
                    print(letras[achar_nome])

                    # Se o nome estiver já nas tocadas
                    if achar_nome in tocadas:

                        tocadas[achar_nome] += 1

                    else:

                        tocadas[achar_nome] = 1

                # Não estando cadastrado, volte ao menu principal
                else:
                    print("Essa música não está cadastrada.")

                ##Fim do item b)
            elif opcao == 2:
                """
                -----    Exemplo de saída no terminal:    -----

                Nome: Nome1. Audiência de: 50.00 %
                Nome: Nome2. Audiência de: 50.00 %

                -----  Aqui vai o ocorrer o cálculo da audiência  -----
                """
                ##Inicio do item c)

                # Extraindo todas músicas tocadas e quantidade que foram
                for musica, quantidade in tocadas.items():
                    # Tira a pocentagem de vezes tocadas
                    ibope = (quantidade * 100) / len(tocadas)

                    print(f"{musica}. Audiência de: {ibope} %.")

                ##fim do item c)
            elif opcao == 3:

                # Vai procurar a música

                pass
                ##Inicio do item d)

                ##Fim do item d)
            elif opcao == 0:
                quit()

            else:
                print("Opção incorreta. Opções disponiveis")
                print("1 - Tocar música")
                print("2 - Calcular audiência")
                print("3 - Qual é a música?")
                print("0 - sair.")
