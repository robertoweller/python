from math import exp


def exp_(cima):
    # resul = 1
    base = 2.718281828459045
    
    # resul = pow(base, cima)
    resul = base ** cima

    return resul

nu = 20
e = 2.718281828459045

resu = 1

t = exp_(nu)
e = exp(nu)

print('t-', f'{t:.7f}')

print('e-', e)

"""
>>> from math import exp
>>> b = 2.718281828459045

>>> b**2
7.3890560989306495
>>> exp(2)
7.38905609893065
"""


# print(mult(b, t))
# print(exp(b))
#print(exp_(b))
