from abc import abstractproperty


def processar():
    
    try:

        print('Processando programa...')

        # O usuario digitou
        usuario = input('Digite! ')

        # Listas de funções
        lista = [chama, chamouN, ira]

        # Se usuario digitar 0 ou o que digitar for maior q a lista, 
        # não vai chamar a função, isso para evitar bug
        
        if int(usuario) <= len(lista) and usuario not in '0':
        # Vai procurar dentro da lista qual é a função para chamar e efetua!
            lista[int(usuario)-1]()

        return usuario
    
    # Se for um caracter normal tipo uma letrar só vai escrever essa mensagem
    # e continuar rodando normalmente
    except ValueError:
        # Sla, resolver aqui
        print('Erro 404!')
        # processar()
    

def chama():
    print('Chamou???')
    pass

def chamouN():
    print('Não chamou?')
    pass

def ira():
    print('irar chamarrrr!')
    pass


usu = True

while usu != '0':
        
    # print(f"{usu=}")
    # Vai processar e aderir a variavel
    usu = processar()




    

