def c_primos(n):
    primos = []
    # n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for div in n:
        for n_div in n:
            if div % n_div != 0:

                primos.append(div)

    return primos

def veri_primo(num):
    tot = 0
    for c in range(1, num + 1):
        if num % c == 0:

            tot += 1

    if tot == 2:
        return True
        
    else:
        return False
        
def gera_l(n):
    n = [i for i in range(n)]
    return n


m = gera_l(9)
outra = [4, 9, 7, 1]
def acha(valor):
    primos = []
    for i in valor:
        if veri_primo(i):
            print(f"{i} está em {valor.index(i)}")
            primos.append(i)
    
    return primos

if __name__ == "__main__":
    # 	2	3	5	7
    p = acha([1, 7, 9])
    print(f'Esses são os números primos >>> {str(p).strip("[]")}')
