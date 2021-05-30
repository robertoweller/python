import math

# n_cpf = "123456789" #09
# n_cpf = "111444777"
n_cpf = "557.103.470".replace('.', '')
# print(n_cpf)
for n_cont in range(1, 3):
    n_base = 10 + n_cont
    # ???
    n_produto = 0

    for n_pos in n_cpf:
        n_base -= 1
        n_produto = n_produto + int(n_pos) * n_base
    # ???
    else:
        n_p = str((11-(n_produto-(math.floor(n_produto/11)*11)))%11)
        n_cpf = n_cpf + str(n_p[len(n_p)-1])

print(f'{n_cpf[:3]}.{n_cpf[3:6]}.{n_cpf[6:9]}-{n_cpf[9:]}')