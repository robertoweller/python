# from os import system as roda
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


def ru_(versao):
    pre = f"""
cd
svm install -l
mkdir .svm/versions/sla
rm -r .svm/versions/*
svm install {versao}
echo '{versao}' > .svm/version
wget -c -P .svm/versions http://chocolatey.org/api/v2/package/ScriptCs/{versao}
cd .svm/versions
mv '{versao}' 'ScriptCs.{versao}.nupkg'
cd
svm install {versao} -from '.svm/versions/ScriptCs.{versao}.nupkg'
svm use {versao}
scriptcs -Version
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