# Programa que ensina conquistar todos os seu desejos

desejos = ""

add = []

continua_rodando = True

print("Digite sair e de ENTER, para sair.")

while continua_rodando:
    desejos = input("Digite seu desejo. > ")
    # esse freio deve acontecer antes que o item seja adicionado a lista
    if desejos == "sair":
        break

    add.append(desejos)

for con in add:
    print(con)

print("Serão conquistados se esforçando muito!")

