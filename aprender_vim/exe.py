"""
Aqui vou testar o nuitka, com o comando:

pip install -U nuitka
"""

def talk(m):
    for i in range(10000000):
        print(i)
    return f'Oi, {m} > rodou {i} vezes.'

def main():
    print(talk('Roberto'))
    

if __name__ == '__main__':
    main()
