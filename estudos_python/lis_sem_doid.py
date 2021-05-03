
endif = "endif"

endwhile = "endwhile"

MAXTAM = 100

n = 0

while ((n < 2) or (n > MAXTAM)):
    n = int(input(f'Digite o tamanho do vetor [2 - {MAXTAM}]: '))

endwhile
j = 1
ListNum = []

while (j <= n):
    Num = int(input("Digite um número: "))
    ListNum.append(Num)
    # Verifica repetições
    Vezes = ListNum.count(Num)

    if (Vezes > 1):
        print("Repetido!, Tente outro número!")
        ListNum.remove(Num) #remove item repetido
        j = j - 1

    endif
    j = j + 1

endwhile # fim do loop orientação da lista
print("\n")
# Exibe a lista com seus elementos
print(ListNum)
