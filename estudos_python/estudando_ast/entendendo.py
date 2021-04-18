import json


# ast = {"nome": "Renato Lelis", "profissao": "Desenvolvedor de sistemas"}

abrir = open("estudos_python/ast/ast.json", "r")

# xx = json.dump(ast, abrir)


x1 = json.load(abrir)

profissao = x1["profissao"]

print(profissao)
