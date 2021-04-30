import json
import os

# procura = input("Digite: ")

local = os.getcwd() + "/Programming_Languages_Extensions.json"

print(local, '\n')

arq_jso = open(local, "r")

# Carregar arquivos json
arq_jso = json.load(arq_jso)


while True:

    procura = input("Digite: ")
    for i in range(len(arq_jso)):
        if "extensions" in arq_jso[i]:
            if procura in arq_jso[i]["extensions"]:
                print(arq_jso[i]["name"])
