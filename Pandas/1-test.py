import pandas as pd
import json

# Dois exemplos de bancos de dados
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

# Carregar o json
js = json.load("verifica_extensoes/Programming_Languages_Extensions.json")

print(js)
