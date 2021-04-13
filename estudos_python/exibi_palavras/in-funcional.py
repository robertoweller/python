palavra = str(input("Digite uma palavra: "))
palavra_2 = str(input("digite outra palavra: "))
rep = input("Digite o número de repetições: ")
p = bool(rep)

if p == 0:
    for i in range(3):
        if palavra_2 == "":
            print(palavra)
        elif palavra == "":
            print(palavra_2)
        else:
            print(palavra)
            print(palavra_2)

if rep.isnumeric():
    rep = int(rep)

    if rep > 0:
        for i in range(rep):
            if palavra_2 == "":
                print(palavra)
            elif palavra == "":
                print(palavra_2)
            else:
                print(palavra)
                print(palavra_2)