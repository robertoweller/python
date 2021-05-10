"""
Pares e Ímpares
Faça um programa que leia um arquivo texto contendo uma lista de número
inteiros separados por "\n" e gerente dois outros arquivos, um contendo
os números pares e o outros os números ímpares. No programa principal
deve ser lido um arquivo de entrada e deve ser chamada função que receba
uma lista contendo cada linha do arquivo e entrada. Esta função deve criar
duas listas, uma contendo os números pares e outra contendo os números ímapres.
Ao final, cada lista deve ser armazenada em um arquivo onde cada número deve 
estar separado por ",".

Exemplos:

Arquivo de entrada:
------------------------
200
197
564
351
765
466
17
------------------------


Arquivos de saída:
---------------------------------------------------
200,564,466            | 197,351,765,17           |
                       |                          |
                       |                          |
                       |                          |
                       |                          |
---------------------------------------------------

Saída:
-----------------------------------------------------
Dígite o nome do arquivo: inteiros.txt

Arquivos pares.txt e impares.txt criados com sucesso!
-----------------------------------------------------

"""
inteiros = ['200\n197\n564\n351\n765\n466\n17']

impares = open('impares.txt', 'w')
pares = open('pares.txt', 'w')

with open('inteiros', 'r') as arquivo:
    for n in arquivo:
         if n % 2 == 0:
             pares.write(str(n) + ',')
         else:
             impares.write(str(n) + ',')
    impares.close()
    pares.close()