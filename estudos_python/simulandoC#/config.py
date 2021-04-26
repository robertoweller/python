# from os import system as roda

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
    try:
        import subprocess
        import os
        os.system(txt)
        # subprocess.call([txt], shell=True)
    
    except Exception as e:
        print(f"Errooooo >{e}")
    


def ru_(versao):
    pre = f"""
echo ""
ifconfigg
"""
    # Precisa passar por aqui tratar e não der erro
    conf(pre)


# Versão do scriptcs
v = "0.17.1"

ru_(v)

"""
Versões do scriptcs que da para escolher
  0.17.1
  0.17.0
  0.16.1
  0.16.0

"""

# Fonts usadas
# https://github.com/scriptcs/scriptcs
