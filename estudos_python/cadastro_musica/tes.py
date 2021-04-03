def index(palavra, lista):
    """
    Vai procurar na lista a palavra e retorna a posição.
    """
    procura = 0

    for cc in lista:

        if palavra in cc:

            return procura

        procura += 1


trecho = "vida"

td_letras = ["era vez", "estrada vida"]
td_cantores = ["Zé da gaita", "João Bosco"]

achou = index(trecho, td_letras)
achou = td_cantores[achou]

print(achou)
