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
    print(f'fib({n})')
    if n <= 1:
        return n 
    else: 
        return  fib(n-1) + fib(n-2)



t = repr(s)
print(repr(s))
# 1 2\t 3\n 4

print(fib(5))
# Agora para texto puro

