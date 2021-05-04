""" Faça um sistema que permite cadastrar “pessoas” para recolhimento
de impostos. Toda Pessoa tem uma renda declarada e pode ser, ou do
tipo “pessoa física” ou do tipo “pessoa jurídica”. PessoaFisica tem,
além da renda, nome e CPF. PessoaJuridica tem, além da renda,
uma razaoSocial e um CNPJ. Pessoa tem também um método
calculaImposto que deve ser redefinido em PessoaFisica e
PessoaJuridica. PessoaFisica paga 2,5% da renda declarada,
enquanto que PessoaJuridica paga 7,5% da renda declarada.

    O sistema deve solicitar a inclusão dos dados de pessoas físicas e
jurídicas até que o usuário decida interromper o cadastro.

    Ao fim, o sistema deve indicar o total de imposto recolhido.
Modele Pessoa, PessoaFisica e PessoaJuridica usando os
conceitos de classes e herança.

Exemplo de saida:

______________________________________________________________________
                    --Recolhimento de imposto--
            Digite o tipo de pessoa (1-Fis/2-Jur): 1
            Nome: Fulano de Tal
            CPF: 123.456.789-10
            Renda: 75000.00
            Deseja cadastrar nova pessoa? (1-Sim/2-Não): 1
            Digite o tipo de pessoa (1-Fis/2-Jur): 2
            Razão Social: Beltrana Comércio de Alimentos LTDA
            CNPJ: 12.345.678/0009-10
            Renda: 2800000.00
            Deseja cadastrar nova pessoa? (1-Sim/2-Não): 2
            Total de impostos recolhidos: 211875.00
_________________________________________________________________________

"""


print("--Recolhimento de Imposto--")

while True:

    a = int(input("Digite o tipo de pessoa(1-Física/2-Juridica):"))

    class Pessoa:
        def _init_(self, renda):
            self.renda = renda

        def CalculaImposto(self):
            self.renda

    if a == 1:
        class PessoaFisíca(Pessoa):
            def __init__(self, nome, CPF):
                Pessoa._init_(self, renda)

                self.nome = nome
                self.CPF = CPF

        if __name__ == '__main__':
            nome = input("Nome: ")
            CPF = input("CPF: ")
            renda = input("Renda: ")
            info_pessoa_fis = PessoaFisíca(
                nome=nome,
                CPF=CPF,
                renda=renda)

    elif a == 2:
        class PessoaJuridica(Pessoa):
            def __init__(self, Razao_social, CNPJ):
                Pessoa.__init__(self, renda)

                self.Razao_social = Razao_social
                self.CNPJ = CNPJ

        if __name__ == '__main__':
            Razao_social = input("Razão Social: ")
            CNPJ = input("CNPJ: ")
            renda = input("Renda: ")
            info_pessoa_jur = PessoaJuridica(
                nome=nome,
                CNPJ=CNPJ,
                renda=renda,
            )