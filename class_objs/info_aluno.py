"""
Crie uma classe Aluno contendo nome, idade e gênero. Além
disso, crie uma subclasse AlunoEscolaridade que contemple 
informações sobre sua escolaridade tais como: curso, e data
de conclusão. Peça que o usuário informe todos esses dados e 
os atribua em um objeto de AlunoEscolaridade. Use _str_ para
imprimir esses dados de forma adequada.

O programa deve garantir que a média geral acumulada (MGA) não
seja acessada fora da classe.

Exemplo de saida:

-------------------------------------------------------------
Aluno: Adalberto da Silva
Idade: 25
Gênero: M
Curso: Ciência da Computação
Universidade: UFRGS
MGA: 7.12
Data de conclusão: 25/12/2005
-------------------------------------------------------------


"""


class Aluno:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero


class AlunoEscolaridade(Aluno):
    def __init__(self, curso, data, MGA, universidade, nome, idade, genero):
        Aluno.__init__(self, nome, idade, genero)

        self.curso = curso
        self.universidade = universidade
        self.__MGA = MGA
        self.data_de_conclusão = data

    def __str__(self):
        self.geral = f"""
Aluno: {self.nome}
Idade: {self.idade}
Gênero: {self.genero}
Curso: {self.curso}
Universidade: {self.universidade}
MGA: {self.__MGA}
Data de conclusão: {self.data_de_conclusão}
"""
        return self.geral


if __name__ == '__main__':

    info_aluno = AlunoEscolaridade(
        nome ='Adalberto da Silva', 
        idade = 25, 
        genero ='M', 
        curso = 'Artes', 
        universidade = 'UFRGS', 
        MGA = 7.12, 
        data = '25/12/2005')

    print(info_aluno)