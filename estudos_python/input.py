from datetime import date

nome = input("Qual seu nome? ")
hoje = date.today()

dia = input("Qual o dia do seu aniversário? ")
mes = input("Qual o mês do seu aniverssário? ")
ano = input("Qual o ano do seu aniversario? ")

hoje = str(hoje)

dia_h = int(hoje[8:])
mes_h = int(hoje[5:7])
ano_h = int(hoje[:4])

sua_idade = ano_h - int(ano)

if int(mes_h) < int(mes):

    sua_idade = sua_idade - 1

if int(mes_h) == int(mes):
    if dia_h < int(dia):
        sua_idade = sua_idade - 1

print(f"{nome.title()}, você tem {sua_idade} anos.")
