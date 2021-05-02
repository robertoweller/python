import subprocess
from time import sleep as s


def conf(txt):
    """
    Vai retorna o texto tratado e em forma de lista
    """
    txt = txt.split("\n")
    txt = txt[1 : len(txt) - 1]

    # Vai juntar a lista separado por &&
    txt = " && ".join(txt)

    print(txt)

    # Vai executar o comando no terminal
    subprocess.run(txt, shell=True)


def ru_():
    pre = f"""
sudo apt remove photon
rm photon.0.1.deb
dpkg -b Photon/ photon.0.1.deb
sudo dpkg -i photon.0.1.deb
photon -deb
"""
    # Precisa passar por aqui tratar e não der erro
    conf(pre)

ru_()