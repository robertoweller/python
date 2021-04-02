trecho = "estrada"
posicao = 0

procura = 0
# Vai recer o cantor da letra
achou = ""

td_letras = ["era vez", "estrada vida"]
td_cantores = ["Zé da gaita", "João Bosco"]


i = trecho

for cc in td_letras:

    if trecho in cc:

        achou = td_cantores[procura]

        print(f"\nFoi {achou} que cantou esse trecho\n")

    procura += 1

    # posicao = conta

# print(td_letras[posicao])