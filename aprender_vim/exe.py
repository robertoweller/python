"""
Aqui vou testar o nuitka, com o comando:

pip install -U nuitka

python -m nuitka --follow-imports --standalone exe.py

"""

def talk(m):
    for i in range(10000000):
        print(i)
    return f'Oi, {m} > rodou {i} vezes.'

def main():
    print(talk('Roberto'))
    

if __name__ == '__main__':
    main()
