# Abrir arquivo
arquivoB = open("estudos_python/raspa.txt", "r")

# Le tudo em forma e deixa tudo tentro de uma lista
arquivo = arquivoB.readlines()

# Fecha o arquivoB
arquivoB.close()

print(arquivo)
