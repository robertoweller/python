nome = input("Qual qual seu nome?")


# Um jeito de deixar no meio
meio = f"{nome:-^20}"

# Outro jeito de deixar no meio o nome

q = 11

sla = int(q / 2)

car = "-"

meio2 = car * sla + nome + car * sla

print(meio)

# print(type(t))