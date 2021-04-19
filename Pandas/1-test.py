import pandas as pd

# Dois exemplos de bancos de dados
# Exemplo 1, criando aqui mesmo o banco
df = pd.DataFrame(     
  {
   "Name": [
    "Braund, Mr. Owen Harris",
    "Allen, Mr. William Henry",
    "Bonnell, Miss. Elizabeth",
   ],
   "Age": [22, 35, 58],
   "Sex": ["male", "male", "female"],
  }
 )


# Exemplo 2 abrindo um externo, Pandas aceita diversos tipo até json
# Agora simplificando o banco de dados com Pandas
simple = pd.read_json("verifica_extensoes/Programming_Languages_Extensions.json")

# Exibindo o banco simplificado num iterrows
for a, b in simple.iterrows():
    # print('--------------------------------\n', a,)
    if '.pas' in b['extensions']:

        print(b, end="\n\n")


# Outro modo de abrir json
# Carregar o json
# abre = open("verifica_extensoes/Programming_Languages_Extensions.json", "r")
# js = json.load(abre)
