import json

# procura = input("Digite: ")

local = "Programming_Languages_Extensions.json"

arq_jso = open(local, "r")

# Carregar arquivos json
arq_jso = json.load(arq_jso)

print("Digite o final do formato junto com o ponto, exemplo '.p'")
print("Type the ending, the format with just the dot, example '.p'\n")


while True:

    achou = False
    procura = input("Digite: ")
    for i in arq_jso:

        if procura in i["extensions"]:
            print(i["name"])
            achou = True

    # Se não achou
    if achou != True:
        print("Não achou nenhum formato.")
        print("Did not find any format.")
