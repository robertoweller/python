
print('DNA contem A, C, G, e T, acho kk')

# O dna é A, C, G, e T
dn = ['A', 'C', 'G', 'T']

dna = input('Digite o dna: ')

manipular = list()

for d in dna:
    
    # Vai deixar a string em letra maiuscula
    d = d.capitalize()
    # print(d)
    # Para começar entender vou usar if, mas recomendavel usar um dicionario
    if d in dn:
        manipular.append(d)

# manipular vai ser que será usada
# juntar vai deixar de ser uma lista para virar uma string
junta = ''.join(manipular)

# junta vai ser o DNA, não sei de DNA, mas acho que é o q pede no exercicio
print(f'\n {junta=}')