# https://pt.stackoverflow.com/questions/505580/como-usar-while-e-if-no-python#505600

# Outro modo de resolver
while True:
    nome_lutador = input('Digite o nome do lutador: ')
    peso_lutador = float(input('Digite o peso do lutador: '))

    if peso_lutador > 0:
        # Vai ser 'Pena' se for menor que 65
        categoria = 'Pena'

        if peso_lutador >= 65 < 72:
             categoria = 'Leve'
             print(categoria)
        if peso_lutador >= 72 < 79:
            categoria = 'Ligeiro'
            print(categoria)
        if peso_lutador >= 79 < 86:
            categoria = 'Meio-medio'
            print(categoria)
        if peso_lutador >= 86 < 93:
            categoria = 'Medio'
            print(categoria)
        if peso_lutador >= 93 < 100:
            categoria = 'Meio-pesado'
            print(categoria)
        if peso_lutador >= 100:
            categoria = 'Pesado'
            print(categoria)

        print(
            f'O lutador {nome_lutador} pesa {peso_lutador:.1f}', 
            f'Kg e se enquadra na categoria {categoria}')
    else:
        print('Peso Inválido!')
        break