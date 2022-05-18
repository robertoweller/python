from time import sleep as s
import pyautogui as py

l = ['Eu', 'amo!'] 

j = ' '.join(map(str, l))


def esc(tex = 'Te amo!', tem=.1, q = 10):
    # Vai esperar até dar ok
    py.alert('Programinha, feito por Roberto, Clique Ok para dar todo o seu amor a sua dona! <3')

    for i in range(q):

        s(tem)
        print(tex)
        py.write(tex, interval=0.1)
        py.press('enter')

# como argumeento passar texto, tempo e quantidade de vezes
esc(q = 100, tex = 'VITORIA')
