import ast


class Acha(ast.NodeVisitor):
    def generic_visit(self, node):

        nome_feio = str(type(node).__name__)
        print(nome_feio)

        # print(node)

        ast.NodeVisitor.generic_visit(self, node)


codigo = """

def sla(tan_faz):
    print(tan_faz)

"""


procura = Acha()
empa = ast.parse(codigo)
procura.visit(empa)


#############################################
def str_node(node):
    if isinstance(node, ast.AST):
        fields = [
            (name, str_node(val))
            for name, val in ast.iter_fields(node)
            if name not in ("left", "right")
        ]
        rv = "%s(%s" % (
            node.__class__.__name__,
            ", ".join("%s=%s" % field for field in fields),
        )
        return rv + ")"
    else:
        return repr(node)


def ast_visit(node, level=0):
    # Vai printar parecido com Árvores de Sintaxe Abstrata
    # https://docs.python.org/pt-br/3.8/library/ast.html#module-ast
    print("  " * level + str_node(node))
    print(str_node(node))
    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    ast_visit(item, level=level + 1)
        elif isinstance(value, ast.AST):
            ast_visit(value, level=level + 1)


codigo = """

def sla(tan_faz):
    print(tan_faz)

"""

# ast_visit(ast.parse(codigo))
