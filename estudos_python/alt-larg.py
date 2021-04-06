def primeiro():
    largura = int(input("Digite a largura: ")) + 2

    altura = int(input("Digite a altura: "))
    caracter = str(input("Digite o carácter: "))
    linha = -1

    # Esse está fazendo impressão da altura
    while linha <= altura:

        print(caracter, end="")
        coluna = 2

        # Está fazendo a impressão da largura
        while coluna < largura:

            if linha == -1 or linha == altura or coluna == largura:
                print(caracter, end="")
            else:
                print(end=" ")

            coluna = coluna + 1

        linha = linha + 1

        print(caracter)


primeiro()
