import numpy

media = [8, 7, 6]

velocidade = [99,86,87,88,111,86,103,87,94,78,77,85,86]

print(f'Usando Função Python {sum(media)/len(media):>20}')

print(f'Usando Numpy Média {numpy.mean(media):>22}\n')

print(sum(velocidade)/len(velocidade))

print(numpy.mean(velocidade))

# Testando para encontrar o valor mediano

mediana = velocidade 

# Para encotrar a medina é simples
# Primeiro vou deixar os números em ordem

m = sorted(mediana)
print(f'Em ordem crescente > {m}\nAgora vou rexolver segunda parte')

# Para encontrar a mediana é preciso achar o valor do meio
def median(n):
    n = sorted(n)
    if len(n) % 2 == 0:
        return (n[int(len(n)/2)] + n[int(len(n)/2)-1])/2
    
    return float(n[int(len(n)/2)])

mm = [5, 10, 15, 20]
print(f'No caso o valor do meio é {median(mm)}')

print(f'Com o Numpy tem o modulo Median {numpy.median(mediana)}')

## Tem os valores modas, são os valores que repete
