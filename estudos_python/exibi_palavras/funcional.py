def int_(a):
    a = str(a)

    if a.isnumeric():

        return int(a)
    else:
        return 3


def for_(tds, re=3):
    # Se que que mais palavras só adicionar a lista
    pp = re * tds

    for i in pp:
        if i != "":
            print(i)


palavra = input("Digite uma palavra: ")
palavra_2 = input("digite outra palavra: ")
rep = int_(input("Digite o número de repetições: "))

tds = [palavra]

for_(tds, rep)
