from functools import partial


class Testando:
    def pati(self, fun, arg):

        if arg and self.chamou:

            return fun(arg)

        self.chamou = 1

    def roda(self):
        """
        Eu quero passar a string, mas não quero chamar a função escreve
        """
        letras = ["c", "a", "d", "f", "b", "e"]

        self.chamou = 0

        self.procura = 0

        for achou in letras:
            if achou == "d":
                # Digamos que você precise passar agora, mas não que chamar a função
                passando = self.pati(
                    self.escreve, f"Achou! estava na posição {self.procura} da lista!"
                )
            self.procura += 1
        # Porque a função escreve já esta sendo chamado por outra chamada
        # escreve()

        # E só agora você que chamar a função, mas não que passar argumento
        self.pati()

    def escreve(arg):

        print(arg)


if __name__ == "__main__":
    Testando()
