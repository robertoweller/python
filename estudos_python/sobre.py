import sys

ar = sys.argv

def soma(n1, n2):
    return n1 + n2

def subt(n1, n2):
    return n1 - n2

if ar[1] == 'soma':
    r = soma(float(ar[2]), float(ar[3]))

elif ar[1] == 'subt':

    r = subt(float(ar[2]), float(ar[3]))

print(r)
