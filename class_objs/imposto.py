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

class PessoaFisica:
    def __init__(self, nome, CPF, renda):
        
        self.rf = float(renda)
        self.nome = nome
        self.CPF = CPF

    def calculaImposto(self):
        # 2,5% de 75000 = 1875
        self.rf = (2.5/100)*self.rf

        return self.rf


class PessoaJuridica: 
    def __init__(self, razaoSocial, CNPJ, renda):

        self.rj = float(renda)
        self.razaoSocial = razaoSocial
        self.CNPJ = CNPJ

    def calculaImposto(self):
        # 7,5% de 2800000 = 210000
        self.rj = (7.5/100)*self.rj

        return self.rj


class Pessoa:
    renda = 0
    
    def __init__(self, usuario):
        if usuario == :   
            nome = input("Nome: ")
            CPF = input("CPF: ")
            renda = input("Renda: ")

            # Chama PessoaFisica
            self.__class__.renda += PessoaFisica(nome, CPF, renda).calculaImposto()
            # nome = "Fulano de Tal"
            # CPF = "123.456.789-10"
            # renda = 75000

        elif usuario == '2':    
            razaoSocial = input("Razão Social: ")
            CNPJ = input("CNPJ: ")
            renda = input("Renda: ")
            
            # Chama PessoaJuridica
            self.__class__.renda += PessoaJuridica(razaoSocial, CNPJ, renda).calculaImposto()
            # razaoSocial = "Beltrana Comércio de Alimentos LTDA"
            # CNPJ = "12.345.678/0009-10"
            # renda = 2800000


    def calculaImposto(self): 
        self.renda = self.__class__.renda
        print(f'Total de impostos recolhidos: {self.renda:.2f}')

        return self.renda


if __name__ == '__main__':
    print('--Recolhimento de Imposto--')

    b = "0"

    while b != "2":

        a = input("Digite o tipo de pessoa (1-Física/2-Juridica): ")
        pessoa = Pessoa(a)
        b = input("Deseja cadastrar nova pessoa? (1-Sim/2-Não): ")

    imposto = pessoa.calculaImposto()
