sla = True

if sla:
    class PessoaFisica:
        def __init__(self):
            self.cpf = '000.000.0...-00'
            self.rg = '...'
            # etc..

    class PessoaJuridica:
        def __init__(self):
            self.cnpj = '...'
            self.registroImpresa = '...'
            # etc

    print("sim")

else:
    print("não")