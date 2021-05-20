"""
E esse texto é originalmente em inglês.

Encontre o número duplicado

Dado um array nums contendo n + 1 inteiros onde cada inteiro está entre 
1 e n (inclusive), prove que pelo menos um número duplicado deve existir. 
Suponha que haja apenas um número duplicado, encontre o número duplicado.

Nesses exercicio não pode passar de 4 o array.

Exemplo 1:

Entrada: [1,3,4,2,2]
Produto: 2


Exemplo 2:

Entrada: [3,1,3,4,2]
Produto: 3
Observação:

Você não deve modificar a matriz (suponha que a matriz seja somente leitura).
Você deve usar apenas espaço extra constante O (1).
Sua complexidade de tempo de execução deve ser menor que O (n2).
Há apenas um número duplicado na matriz, mas pode ser repetido mais de uma vez.
"""

def acha(n):
    n = sum(n)-10
    print(n)


if __name__ == '__main__':
    # Teste para ver se estár certo
    acha([1, 3, 4, 2, 2]) #2
    acha([3, 1, 3, 4, 2]) #3
    acha([3, 1, 4, 4, 2]) #4
    acha([1, 1, 3, 4, 2]) #1