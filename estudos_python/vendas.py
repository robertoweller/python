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
        # Vai procurar dentro da lista qual é para chamar!
            lista[int(usuario)-1]()
        
        z = int(usuario)

        xxt = 1

        
    
        return z
    
    # Se for um caracter normal tipo uma letrar só vai escrever essa mensagem
    # e continuar rodando normalmente
    except ValueError:
        # Sla, resolver aqui
        
        while True:
            
            if usuario == '0':
                print('é 000000000000000')
                break
            # Vai procurar o que tem dentro da biblioteca
            usuario = processar()
    

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

while usu:
        
    print(f"{usu=}")
    # Vai procurar o que tem dentro da biblioteca
    usu = processar()




    

