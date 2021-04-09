"""

Exercício :
- Leia e armazene em um dicionário o nome, a idade e o número do telefone de seus 
contatos, sendo que a chave deve ser o nome. 

- - Ao digitar uma string vazia para o nome, o 
programa interrompe a leitura e se encerra. 

- Apresente na tela os dados lidos em ordem 
alfabética pelo nome dos contatos.
 Uma possível solução de ordenar alfabeticamente é usar o método sort. 

- Em seguida, armazene os contatos em outros dois dicionários, utilizando como 
critério a idade: menores de 18 anos em um e os maiores em outro dicionário, 
eliminando 
o original. Apresente na tela os dois dicionários resultantes da separação.

"""
# Exemplo de um dicionario já cadastrados
# Se quiser deixar vazio, só para ilustrar
nomes = {
    "Zorro": [18, "47999051670"],
    "Maria": [15, "41991641670"],
}

# Outra forma de criar um dicionario é assim, dentro do parêntese
# vai o argumento de o que vai ter dentro do dicionario
# no caso aqui crio um dicionario vazio
maiores_18 = dict()
menores_18 = dict()


def apresentar(organizado):

    print("\nTodas as pessoas:\n")

    # Se não for casdastrado nenhum contato aqui vai dar um erro
    for ordem in organizado:
        # Vai procurar no dicionario o nome e separar idade e numero
        # nota: ordem é nome da pessoa
        idade = nomes[ordem][0]
        numero = nomes[ordem][1]

        if idade < 18:
            # Se a pessoa for de menor, salva nesse dicionario
            menores_18[ordem] = [int(idade), numero]

        else:
            # Caso contrario, salva aqui
            maiores_18[ordem] = [int(idade), numero]

        print(f"{ordem} tem {idade} anos e seu número é {numero}.")

    apresentacao_final("Esses são os menores de 18", menores_18)

    apresentacao_final("Esses são os maiores de 18", maiores_18)


def apresentacao_final(most, dicio):

    print(f"\n{most}")

    for rec in dicio:
        idade = dicio[rec][0]
        numero = dicio[rec][1]

        print(f"{rec} tem {idade} anos e seu número é {numero}.")

    print("\n")


def cadastro():
    while True:
        # Sempre atualizando cadastro
        ordem_alfa = sorted(nomes)

        # Vai deixar o nome com primeira maiuscula
        nome = input("Nome: ").title()

        if nome == "":
            print(f"\nDicionario puro: \n{nomes}")
            # Vai chamar a função e passar o dicionario já na ordem alfabetica
            apresentar(ordem_alfa)
            break

        idade = input("Idade: ")
        numero = input("Número de telefone: ")

        # Deixei numero igual uma string só para ilustrar
        # Aqui vai adicionar ao dicionario o cadastro
        nomes[nome] = [int(idade), numero]


cadastro()


# Esse é um jeito de apresentar um contado
# print(nomes["Jao"][1])


# cadastro()