
import matplotlib.pyplot

"""
Polinômios
p(x) =  f(a) + f'(a) (x-a)¹/1! + f''(a) (x-a)²/2! + ...

fª(a) (x-a)ª/n!

É até onde o valor quer chegar?
a = 0

"""
# Função do polinômio linear
def f(x):
    vertor = []
    # Aqui onde (p) é x negativo
    p = -x
    """
    O while server para fazer laços infinitos, na mátematico é
    tipo simbolo de infinito, só que aqui é uma função definino 
    um limite
    """
    while p <= x:
        vertor.append(p)
        print(p)

        p += p/p*((x-p)**2)
    
    return vertor

# L(x) = f (p) + f' (p)(x − p)
p = 2
x = f(p)


# matplotlib.pyplot.plot(x, x)
# matplotlib.pyplot.show()