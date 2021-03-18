
def processar():
    """
    Função criada para processar pedido do usuario e disignar
    para suas devidas ações
    """
    
    try:

        # O usuario digitou
        usuario = input('Digite! ')

        # Listas de funções
        lista = [cadastrar, vender, exibir]

        # Se usuario digitar 0 ou o que digitar for maior q a lista, 
        # não vai chamar a função, isso foi feito para evitar bug
        if int(usuario) <= len(lista) and usuario not in '0':
        # Vai procurar dentro da lista qual é a função para chamar e chama ela!
            lista[int(usuario)-1]()

        return usuario
    
    # Se for um caracter normal tipo uma letrar só vai escrever essa mensagem
    # e continuar rodando normalmente
    except ValueError:
        # Sla, resolver aqui
        print('Opção não válida! ')
        # processar()
    

def cadastrar():
    """
    Precisa resolver como vai efeturar cadastro
    """
    nome = input('Nome: ')
    quantidade = input('Quantidade: ')
    valor_unidade = input('Valor Unitário: ')
    print('')

    pass

def vender():
    """
    Precisa resolver como os desconto do produto na lista que será feito
    """
    id = input('Código do produto: ')
    # Talvez deva escolher outra variavel para facilitar
    quantidade = input('Quantidade: ')
    # Talve nem vá precisar, só se tiver desconto.
    valor_total = input('Valor total da compra: ')
    pass

def exibir():
    """
    Provavelmente terá q ser feito um for nos cadastro produtos q vc criou
    """
    print('Exibira quantos produtos tem!\n')
    pass


usu = True

# Quando usuario digitar 0 vai parar o luping e sair do programa
while usu != '0':
    print(
        f'-----------------------------------------------'
        '--------------------------\n'
        'Sistema de vendas online:',
        '1-Cadastrar, 2-Vender, '
        '3-Exibir, 0-Finalizar: ')
    # print(f"{usu=}")
    # Vai processar e aderir a variavel
    usu = processar()
