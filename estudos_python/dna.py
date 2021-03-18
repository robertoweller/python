
print('Nesse exemplo contem A, C, G, e T \n')



"""
No exemplo:

AATCTGCAC virou TTAGACGTG

TATGCGCAC virou ATACGCGTG


Pesquisando na internet sobre DNA é tipo assim que funciona:

Olhando para baixo da para começar enteder

A - T
T - A
T - A
G - C
C - G
A - T
T - A
G - C
C - G
G - C
C - G
A - T
T - A
T - A
A - T
C - G
G - C

"""

# O dna é A, C, G, e T
# Mas o exercio não pede uma estrutura tão complexa igual então
# Esse dicionario resolve
complementar = {
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C',
}

dna = input('Digite uma sequência de DNA: ')

corrigido = []

manipular = list()

for d in dna:
    
    # Vai deixar a string em letra maiuscula
    d = d.upper()
    # print(d)
    # Para começar entender vou usar if, mas recomendavel usar um dicionario
    if d in complementar:
        corrigido.append(d)
        # print(f'{d=}')
        # Vai no dicionario e muda a letra
        # e adiciona a lista 
        manipular.append(complementar[d])

# manipular vai ser que será usada
# juntar vai deixar de ser uma lista para virar uma string
junta = ''.join(manipular)
corrigido = ''.join(corrigido)

# junta vai ser o DNA, não sei de DNA, mas acho que é o q pede no exercicio
print(f'\n A cadeia complementar de {corrigido} é {junta}')