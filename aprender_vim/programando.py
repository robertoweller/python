def html():
    return f'Olá, {nome}'


def google():
    return 'Olá, mundo!'

s =  '1 2\t 3\n 4'
# print(s)

# \t da tab e \n quebra linha
# 1 2	 3
#  4
def fib(n):
    # print(f'fib({n})')
    if n <= 1:
        return n 
    else: 
        return  fib(n-1) + fib(n-2)


t = repr(s)
# print(repr(s))
# 1 2\t 3\n 4

print(fib(15.5))
# Agora para texto puro


def fatorial(n):
    if not isinstance(n, int):
        raise Exception('No interable')

    elif n == 0:
      #Caso trivial

        return 1 #Solução direta

    return n*fatorial(n-1) #Chamada recursiva


print(fatorial(10.5))

