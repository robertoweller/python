def int_(a):
    a = str(a)

    if a.isdecimal():
        return int(a)
    if a == "":
        return 3
    return 0


def for_(tds, re):
    # Se que que mais palavras só adicionar a lista
    pp = re * tds

    for i in pp:
        if i != "":
            print(i)


palavra = input("Digite uma palavra: ")
palavra_2 = input("Digite outra palavra: ")
rep = int_(input("Digite o número de repetições: "))
# # Se que que mais palavras só adicionar a lista
tds = [palavra, palavra_2]

for_(tds, rep)
