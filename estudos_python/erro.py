from datetime import date

hoje = date.today()

print("\n Bem-vindo à Loja")
print(
    "Vejo que precisa de ajuda com crédito, para isso "
    "isso é necessário seu cargo  e salário atuais junto "
    "do seu ano de nascimento"
)
print(
    "Seu pedido será processado após o preenchimento "
    "do formulário abaixo com os dados solicitados:\n"
)

# cargo = input('Qual é seu cargo atual? ')
cargo = "Programador"
# salario = float(input('Qual é o seu salário atual?: '))
salario = 1200
# dataa = int(input('Qual é o ano de nascimento?: '))
dataa = 1996
idade = hoje.year - dataa
credito = int(salario * (idade / 1000)) +100


print(
    "\n" "Estes são seus dados:\n Profissão:",
    cargo,
    "\n Salário: R$",
    salario,
    "\n Ano de nascimento:",
    dataa,
    "\n",
)

print("Por favor siga as etapas abaixo: \n")
# nomep = input('Digite o nome do produto: ')
nomep = "Carro"
# valorp = float(input('Digite o preço do produto: '))
valorp = 5000



parcelar = (credito * 60) / 100
parcelar2 = float(credito * 89.9 / 100)
blq = (credito * 90) / 100
blq2 = float(credito * 99.9 / 100)

aprovar = valorp / credito


print(
    f'Se {aprovar} maior que {parcelar} e menor que {parcelar2}\n'
    '**Pedido Liberado ao parcelar em 2x**')

print(
    f'\nSe {aprovar} maior que {blq} e menor que {blq2}\n'
    '**Credido Bloqueado**')



if aprovar < float((credito * 60 / 100)):
    print("\nPredido Liberado")

elif aprovar > float(credito * 60 / 100) and aprovar < float(credito * 89.9 / 100):
    print("\nPedido Liberado ao parcelar em 2x")

elif aprovar > float(credito * 99.9 / 100):
    print("\nCredido Bloqueado")

# input()
