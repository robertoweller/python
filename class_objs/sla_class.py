sla = True

if sla:
    class PessoaFisica:
        def __init__(self, cpf, rg):
            self.cpf = cpf
            self.rg = rg
            # etc...

    class PessoaJuridica:
        def __init__(self, cnpj, rgi):
            self.cnpj = '...'
            self.registroImpresa = '...'
            # etc...

    print("sim")
    PessoaFisica('45', '69')

else:
    # Note que se sla for False vai dar um erro pq aqui não foi declarado as
    # classes
    # NameError: name 'PessoaFisica' is not defined
    # pq pessoa depois de else não foi definida só foi feito depois de if
    PessoaFisica('45', '69')
    print("não")