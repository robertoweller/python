"""
Aqui vou testar o nuitka, com o comando:

pip install -U nuitka

python -m nuitka --follow-imports --standalone exe.py

"""

def talk(m):
    for i in 0..1000000:
        print(i)
    return ''


def main():
    print(talk('Roberto'))
    


main()
