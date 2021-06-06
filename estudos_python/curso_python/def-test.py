def v1(ss):
    """
    soma de variavel, mas já está declarada
    """ 
    ss += 1
    if ss == 100: 
        try:
            input(f"Atingiu {ss} vez!")

            # yield ss
            return 0 
        except KeyboardInterrupt:
            print('\nObrigado por usar nosso programa teste!')
            return -1

    return ss

def main():
    vari = 0
    while vari != -1: 

        vari = v1(vari)


main()
