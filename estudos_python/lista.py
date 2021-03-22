def empacotar(nomes):
    """
    Essa função aceita até dois autores
    Exemplo:

    nomes = "Roberto weller, Caiu Vitoga Silvia"
    """

    nomes = nomes
    nome = nomes.split(", ")

    nome_p = nome[0].split()

    formatado = list()

    # inverte o nome e sobrenome
    nome_p = f"{nome_p[len(nome_p)-1][0].title()}.{nome_p[0].title()}"

    formatado.append(nome_p)
    # print(f"{nome=} Tamanho >{len(nome)}")

    if len(nome) > 1:

        nome_se = nome[1].split()

        # Acha o sobre nome
        nome_sobre = f"{nome_se[len(nome_se)-1]}"

        # Resolve o nome mudando-o nome de lugar
        nome_se = f"{nome_sobre[0].title()}.{nome_se[0].title()}"

        formatado.append(nome_se)
        # print(f"{nome_se=}")

    formatado = " e ".join(formatado)

    return formatado


# Pergunta pro usuários
p = input('Escreva o(s) nome(s) do(s) autor(es) separado por ",": ')

print(empacotar(p))