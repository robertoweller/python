import random

def maior(s):
    return random.randint(51, 100)

def menor(s):
    return random.randint(0, 49)

def main(n = 50):
    entrada = ''
    l = [] 

    while entrada != 'correto':
        entrada = input(f'Seu número secreto é o {n}? ')

        if entrada == 'maior':
            n = maior(entrada)

        elif entrada == 'menor':
            n = menor(entrada)    
        

        elif entrada == 't':
            # Vai conter minha lista passada
            print(l)
    print('Que bom que achou!')
    

if __name__ == '__main__':
    main()
