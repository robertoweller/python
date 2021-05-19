from time import sleep
from random import randint

print("\033[33m-=-" * 54)
jo = ("\033[34m Jogo de batalha")
print(jo.center(170))
print("\033[33m-=-" * 54)
#----------------------------------------------------------------------------------------------------------------------
inicio = input("Pressione enter para começar...")
print("Iniciando...")
sleep(1)

#---------------------------------------------------------------------Introdução-------------------------------------------------------------------------------
print("\033[36m\nBem vindo ao sistema de batalha em Pycharm, o jogo a seguir consiste em batalha entre personagens, onda de inimigos, armas para o personagem e Loja de armas.")
print("OBS: Jogo feito em Python por programador iniciante!")
inicio = input("\nPressione enter para começar...")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------Criação de Personagem-------------------------------------------------------------------
print("\n\033[32m[Escolha um nome para seu personagem]\033[m")
NomeDePersonagem = str(input("\n\033[36mDigite o nome do personagem:\033[m "))
while NomeDePersonagem == "":
    print("\n\033[31m[Nome invalido, tente novamente]\033[m")
    NomeDePersonagem = str(input("\n\033[36mDigite o nome do personagem: "))
EscolhaDeArma = int(input(f"\n\033[36mOlá {NomeDePersonagem},escolha uma arma para começar:\n[1]Arco - ATA = (Min 3 a Max 5)\n[2]Adaga - ATA = (Min 2 a Max 4)\n[3]Espada - ATA = (Min 1 a Max 7)\nEscolha = "))
inicio = input("\nPressione enter para começar...")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------Armas-----------------------------------------------------------------------------------

#ARMAS INICIO
Arco = randint(3, 5)
Adaga = randint(2, 4)
Espada = randint(1, 7)

#LOJA DE ARMAS
Katana_Simples = randint(2, 9)
Katana_SimplesPreço = 100
Katana_Afiada = randint(3,10)
Katana_AfiadaPreço = 170
Katana_Espiritual = randint(5,11)
Katana_EspiritualPreço = 300
Besta_Simples = randint(4,6)
Besta_SimplesPreço = 120
Besta_Imperial = randint(5,8)
Besta_ImperialPreço = 170
Besta_Selvagem = randint(6,10)
Besta_SelvagemPreço = 250
Sabre_de_Luz = randint(20,45)
Sabre_de_LuzPreço = 600
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------Inimigos--------------------------------------------------------------------------------
Zumbi = 12
Nzumbi = 12
ResVidaIni = randint(1,5)
AtaqIni = randint(1,3)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------Variaveis do jogo-----------------------------------------------------------------------
Vida = 15
ResVida = randint(1,3)
Nvida = 15
Moeda = 0
MoedaMais = randint(5,20)
Nivel = 0
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------Caso Arco-------------------------------------------------------------------------------
while True:
    if EscolhaDeArma == 1:
        while Nivel < 10:
            print("\033[32m-=-" * 54)
            primeira = ("\033[34mBATALHA")
            print(primeira.center(170),"\n")
            DesqNivel = (f"\033[32:7mNIVEL = {Nivel}\033[m \033[33:7mMOEDAS = {Moeda}\033[m")
            print(DesqNivel.center(187))
            Loja = int(input("\033[33mPressione \n\033[33:7m[1]\033[m \033[33mpara acessar a loja\033[n\n\033[32:7m[2]\033[m \033[33mPara ir para o jogo\033[m\n\033[33mEscolha =\033[m "))
            if Loja == 1:
                print("\033[33:7m-=-\033[m" * 54)
                print(f"\033[36mBem vindo a loja de armas, aqui encontrara armas para melhorar a batalha, quando quiser comprar uma arma veja o numero dela e digite para comprar\nIMPORTANTE: se voce comprar alguma, ela ira substituir a anterior e não podera ser capaz de usar a anterior novamente ao menos que a compre novamente\n\033[33:7mMOEDAS = {Moeda}\033[m")
                DentroLoja = int(input("\n\033[36m[1] Katana Simples (Min 2 a Max 9) Preço = R$100\n[2] Katana Afiada (Min 3 a Max 10) Preço = R$170\n[3] Katana Espiritual (Min 5 a Max 11) Preço = R$300\n[4] Besta Simples (Min 4 a Max 6) Preço = R$120\n[5] Besta Imperial (Min 5 a Max 8) Preço = R$170\n[6] Besta Selvagem (Min 6 a Max 10) Preço = R$250\n[7] Sabre de Luz (Min 20 a 45) Preço = R$600\n[0]Para Sair da loja pressione 0(zero)\nEscolha = "))
                print("\033[33:7m-=-\033[m" * 54)
                if DentroLoja == 1:
                    if Moeda >= Katana_SimplesPreço:
                        Moeda -= Katana_SimplesPreço
                        Arco = Katana_Simples
                        print("\n\033[32:7mAgora sua arma é uma Katana Simples\033[m")
                    else:
                        print("Voce não tem dinheiro suficiente para comprar esta arma.")
                elif DentroLoja == 2:
                    if Moeda >= Katana_AfiadaPreço:
                        Moeda -= Katana_AfiadaPreço
                        Arco = Katana_Afiada
                        print("\n\033[32:7mAgora sua arma é uma Katana Afiada\033[m")
                    else:
                        print("Voce não tem dinheiro suficiente para comprar esta arma.")
                elif DentroLoja == 3:
                    if Moeda >= Katana_EspiritualPreço:
                        Moeda -= Katana_EspiritualPreço
                        Arco = Katana_Espiritual
                        print("\n\033[32:7mAgora sua arma é uma Katana Espiritual\033[m")
                    else:
                        print("Voce não tem dinheiro suficiente para comprar esta arma.")
                elif DentroLoja == 4:
                    if Moeda >= Besta_SimplesPreço:
                        Moeda -= Besta_SimplesPreço
                        Arco = Besta_Simples
                        print("\n\033[32:7mAgora sua arma é uma Besta Simples\033[m")
                    else:
                        print("Voce não tem dinheiro suficiente para comprar esta arma.")
                elif DentroLoja == 5:
                    if Moeda >= Besta_ImperialPreço:
                        Moeda -= Besta_ImperialPreço
                        Arco = Besta_Imperial
                        print("\n\033[32:7mAgora sua arma é uma Besta Imperial\033[m")
                    else:
                        print("Voce não tem dinheiro suficiente para comprar esta arma.")
                elif DentroLoja == 6:
                    if Moeda >= Besta_SelvagemPreço:
                        Moeda -= Besta_SelvagemPreço
                        Arco = Besta_Selvagem
                        print("\n\033[32:7mAgora sua arma é uma Besta Selvagem\033[m")
                    else:
                        print("Voce não tem dinheiro suficiente para comprar esta arma.")
                elif DentroLoja == 7:
                    if Moeda >= Sabre_de_LuzPreço:
                        Moeda -= Sabre_de_LuzPreço
                        Arco = Sabre_de_Luz
                        print("\n\033[37:7mAgora sua arma é um Sabre de luz! QUE A FORÇA ESTEJA COM VOCÊ!\033[m")
                    else:
                        print("Voce não tem dinheiro suficiente para comprar esta arma.")
                elif DentroLoja == 0:
                    print("Saindo da loja...")
                    sleep(1)


                inicio = input("\n\033[33mPressione enter para começar o jogo...\033[m")
            elif Loja == 2:
                print("Iniciando jogo...")
                sleep(1)
            print(f"\n\033[33mVamos começar a batalha! {NomeDePersonagem} a frente existe um inimigo com {Zumbi} de vida, role o dado para saber quem atacara primeiro...(1 Voce ataca primeiro | 2 O inimigo ataca primeiro)\033[m\n\033[34mTente chegar ao Nivel 100, quanto maior o nivel mais dificil é! A cada 10 niveis voce ganha mais vida e dano! e os inimigos tambem\033[m")
            Vida = Nvida
            Zumbi = Nzumbi
            if Nivel >= 10 and Nivel <= 15:
                Vida = Nvida + ResVida
                Zumbi = Nzumbi + ResVidaIni
                Arco += 1
            print(f"\033[33mVida de inimigo =\033[m \033[31m{Zumbi}\033[m \033[33m|| || || Vida {NomeDePersonagem} =\033[m \033[31m{Vida}\033[m")
            while True:
                    RolarDados = input("\n\033[33mPressione enter para rolar o dado...\033[m")
                    print("\033[31mRolando dados...\033[m")
                    sleep(1)
                    Dado = randint(1,2)
                    print(f"\033[33mO dado foi de =\033[m \033[32m{Dado}\033[m ")
                    sleep(1)
                    if Dado == 1:
                        print("\033[32mVoce ira atacar primeiro!\033[m")
                        PreAtaq = str(input("\033[33mEscreva Atacar para atacar:\033[m "))
                        if PreAtaq == "Atacar" or PreAtaq == "atacar":
                            AtaqPersonagem = Arco
                            Zumbi -= AtaqPersonagem
                            print(f"\033[33mInimigo =\033[m \033[31m{Zumbi}\033[m\n\033[33m{NomeDePersonagem}=\033[m \033[31m{Vida}\033[m")
                            if Zumbi == 0:
                                print(f"\033[33mParabens {NomeDePersonagem} voce derrotou o inimigo !\033[m")
                                Nivel += 1
                                Moeda += MoedaMais
                                print(f"\033[33mPersonagem subiu de nivel + 1 || Nivel =\033[m \033[32:7m{Nivel}\033[m")
                                break
                    if Dado == 2:
                        print("\033[31mO inimigo ira atacar primeiro!\033[m")
                        Vida -= AtaqIni
                        print(f"\033[33m{NomeDePersonagem} =\033[m \033[31m{Vida}\033[m\n\033[33mInimigo =\033[m \033[31m{Zumbi}\033[m")
                        if Vida <= 0:
                            print("\033[31mQue pena :( voce perdeu, mas não se preocupe tente novamente\033[m")
                            break
        while Nivel >= 10:
            print("\033[32m-=-" * 54)
            primeira = ("\033[34mBATALHA")
            print(primeira.center(170), "\n")
            DesqNivel = (f"\033[32:7mNIVEL = {Nivel}\033[m \033[33:7mMOEDAS = {Moeda}\033[m")
            print(DesqNivel.center(187))
            print(
                f"\033[33mVamos começar a batalha! {NomeDePersonagem} a frente existe um inimigo com {Zumbi} de vida, role o dado para saber quem atacara primeiro...(1 Voce ataca primeiro | 2 O inimigo ataca primeiro)\033[m\n\033[34mTente chegar ao Nivel 100, quanto maior o nivel mais dificil é! A cada 10 niveis voce ganha mais vida e dano! e os inimigos tambem\033[m")
            Vida = Nvida
            Zumbi = Nzumbi
            if Nivel >= 10 and Nivel <= 15:
                Vida = Nvida + ResVida
                Zumbi = Nzumbi + ResVidaIni
                Arco += 1
            print(f"\033[33mVida de inimigo =\033[m \033[31m{Zumbi}\033[m \033[33m|| || || Vida {NomeDePersonagem} =\033[m \033[31m{Vida}\033[m")
            while True:

                RolarDados = input("\n\033[33mPressione enter para rolar o dado...\033[m")
                print("\033[31mRolando dadosssssssssssssssss...\033[m")
                sleep(1)
                Dado = randint(1, 2)
                print(f"\033[33mO dado foi de =\033[m \033[32m{Dado}\033[m ")
                sleep(1)
                if Dado == 1:
                    print("\033[32mVoce ira atacar primeiro!\033[m")
                    PreAtaq = str(input("\033[33mEscreva Atacar para atacar:\033[m "))
                    if PreAtaq == "Atacar" or PreAtaq == "atacar":
                        AtaqPersonagem = Arco
                        Zumbi -= AtaqPersonagem
                        print(
                            f"\033[33mInimigo =\033[m \033[31m{Zumbi}\033[m\n\033[33m{NomeDePersonagem}=\033[m \033[31m{Vida}\033[m")
                        if Zumbi <= 0:
                            print(f"\033[33mParabens {NomeDePersonagem} voce derrotou o primeiro inimigo !\033[m")
                            Nivel += 1
                            print(f"Personagem subiu de nivel + 1 || Nivel = {Nivel}")
                            break
                if Dado == 2:
                    print("\033[31mO inimigo ira atacar primeiro!\033[m")
                    Vida -= AtaqIni
                    print(
                        f"\033[33m{NomeDePersonagem} =\033[m \033[31m{Vida}\033[m\n\033[33mInimigo =\033[m \033[31m{Zumbi}\033[m")
                    if Vida <= 0:
                        print("\033[31mQue pena :( voce perdeu, mas não se preocupe tente novamente\033[m")
                        RolarDados = input("\n\033[33mPressione enter para tentar novamente...\033[m")
                        break
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------Caso Adaga-------------------------------------------------------------------------------
    elif EscolhaDeArma == 2:
        print("\033[32m-=-" * 54)
        primeira = ("\033[34m PRIMEIRA BATALHA")
        print(primeira.center(170), "\n")
        DesqNivel = (f"\033[32m NIVEL = {Nivel}\033[m")
        print(DesqNivel.center(170))
        print(f"\033[33mVamos começar a batalha! {NomeDePersonagem} a frente existe um inimigo com 100 de vida, role o dado para saber quem atacara primeiro...(1 Voce ataca primeiro | 2 O inimigo ataca primeiro)\033[m")
        while True:
            RolarDados = input("\n\033[33mPressione enter para rolar o dado...\033[m")
            print("\033[31mRolando dados...\033[m")
            sleep(1)
            Dado = randint(1, 2)
            print(f"\033[33mO dado foi de =\033[m \033[32m{Dado}\033[m ")
            sleep(1)
            if Dado == 1:
                print("\033[32mVoce ira atacar primeiro!\033[m")
                PreAtaq = str(input("\033[33mEscreva Atacar para atacar:\033[m "))
                if PreAtaq == "Atacar" or PreAtaq == "atacar":
                    AtaqPersonagem = Adaga
                    Zumbi -= AtaqPersonagem
                    print(
                        f"\033[33mInimigo =\033[m \033[31m{Zumbi}\033[m\n\033[33m{NomeDePersonagem}=\033[m \033[31m{Vida}\033[m")
                    if Zumbi <= 0:
                        print(f"\033[33mParabens {NomeDePersonagem} voce derrotou o primeiro inimigo !\033[m")
                        Nivel += 1
                        print(f"Personagem subiu de nivel + 1 || Nivel = {Nivel}")
                        break
            if Dado == 2:
                print("\033[31mO inimigo ira atacar primeiro!\033[m")
                Vida -= AtaqIni
                print(
                    f"\033[33m{NomeDePersonagem} =\033[m \033[31m{Vida}\033[m\n\033[33mInimigo =\033[m \033[31m{Zumbi}\033[m")
                if Vida <= 0:
                    print("\033[31mQue pena :( voce perdeu, mas não se preocupe tente novamente\033[m")
                    RolarDados = input("\n\033[33mPressione enter para tentar novamente...\033[m")
                    break
        break
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------Caso Espada-------------------------------------------------------------------------------
    elif EscolhaDeArma == 3:
        print("\033[32m-=-" * 54)
        primeira = ("\033[34m PRIMEIRA BATALHA")
        print(primeira.center(170), "\n")
        DesqNivel = (f"\033[32m NIVEL = {Nivel}\033[m")
        print(DesqNivel.center(170))
        print(f"\033[33mVamos começar a batalha! {NomeDePersonagem} a frente existe um inimigo com 100 de vida, role o dado para saber quem atacara primeiro...(1 Voce ataca primeiro | 2 O inimigo ataca primeiro)\033[m")
        while True:
            RolarDados = input("\n\033[33mPressione enter para rolar o dado...\033[m")
            print("\033[31mRolando dados...\033[m")
            sleep(1)
            Dado = randint(1, 2)
            print(f"\033[33mO dado foi de =\033[m \033[32m{Dado}\033[m ")
            sleep(1)
            if Dado == 1:
                print("\033[32mVoce ira atacar primeiro!\033[m")
                PreAtaq = str(input("\033[33mEscreva Atacar para atacar:\033[m "))
                if PreAtaq == "Atacar" or PreAtaq == "atacar":
                    AtaqPersonagem = Espada
                    Zumbi -= AtaqPersonagem
                    print(
                        f"\033[33mInimigo =\033[m \033[31m{Zumbi}\033[m\n\033[33m{NomeDePersonagem}=\033[m \033[31m{Vida}\033[m")
                    if Zumbi <= 0:
                        print(f"\033[33mParabens {NomeDePersonagem} voce derrotou o primeiro inimigo !\033[m")
                        Nivel += 1
                        print(f"Personagem subiu de nivel + 1 || Nivel = {Nivel}")
                        break
            if Dado == 2:
                print("\033[31mO inimigo ira atacar primeiro!\033[m")
                Vida -= AtaqIni
                print(
                    f"\033[33m{NomeDePersonagem} =\033[m \033[31m{Vida}\033[m\n\033[33mInimigo =\033[m \033[31m{Zumbi}\033[m")
                if Vida <= 0:
                    print("\033[31mQue pena :( voce perdeu, mas não se preocupe tente novamente\033[m")
                    RolarDados = input("\n\033[33mPressione enter para tentar novamente...\033[m")
                    break
        break
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
nova = input("VAMOS JOGAR ")
print("\033[32m-=-" * 54)







#-------------------------------------------------------------------------------------------------------------------------------------------------------------




