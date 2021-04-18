import ast


class RewriteSelf(ast.NodeVisitor):
    def generic_visit(self, node):
        print(node)
        if isinstance(node.value, ast.Name):  # s.x
            print(node.value.id)

            if node.value.id == "s":  # this is not optimized by "common writer"

                node.value.id = "hostobj"
            else:

                self.visit(node.value)

        rewriter = RewriteSelf()


codigo = """
def aaa():
    print("Socorrroooo")

aaa()
"""


RewriteSelf()