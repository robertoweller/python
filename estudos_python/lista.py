
'''

a = input('Digite o titulo do livro:')
b = input('Digite os autores do livro:')
c = input('Ano de publicação do livro:')
d = input('Cidade:')
e = input('Editora do livro:')



'''

# Digamos que essa sejaa a resposta
a = 'Perditubes'
b = 'Roberto Weller, Jao Solza'
c= '1996'
d= 'SFS'
e = 'EdMensoes'

# ??? Erro
autor_1, autor_2 = b.split(',')

nome, sobrenome = autor_1.split()
nome_2, sobrenome_2 = autor_2.split()

nome_com = [sobrenome, nome, sobrenome_2, nome_2]


# Desempacotar todos os nomes juntos
nom_lis = ' '.join(nome_com)

# A variavel b contém nome


resulado = f'{nom_lis}, {a}. {d}: {e}, {c}'



# Retorna uma tupla
print(resulado)