"""
# Desafio 004

Faça um programa que leia algo pelo
teclado e mostre na tela o seu
tipo primitivo e todas as informações
possiveis sobre ele.

Exemplo de saida:
----------------------------------------------
Digite algo: Programador: Programador
O tipo primitivo desse valor é <clas 'str'> # type(digite)
Só tem espaços?  False # digite.isspace()
É um número?  False # digite.isnumeric()
É alfabético?  True # digite.isalpha()  
Está em maiúsculas?  False # digite.isupper()
Está em minúsculas?  False # digite.islower()
Está capitalizada?  True # iscapitalize(digite)


"""

# Função criada por mim, para verificar se está capitalizada
def iscapitalize(string):
    """
    Retorna True se a primeira letra da
    string é uma string maiúscula, False caso contrário.

    Uma string é capitalizada se apenas o primeiro caracterer na
    string é maiúsculo e se há pelo menos um caractere na string.
    """
    if string == string.capitalize():
        return True
    else:
        return False


d = input("Digite algo: ")


tipo = type(d)

letras = d.isalpha()

# Quando tem letras ou números inteiros -> True
numeLetras = d.isalnum()

# Se está dentro da tabela ASCII (caracter válido) -> True
ascii = d.isascii()

# Se é um número decimal, se tem uma ou mais casa (exemplo: "100") -> True
decimal = d.isdecimal()

# Se todos os caracteres forem dígitos (exemplo: "²" ou "10") -> True
digito = d.isdigit()

# Se é uma palavra reservada do python (exemplo: "def" ou class) -> True
palaReservada = d.isidentifier()

# Se todos caracters forem maiusculos -> True
maiuscula = d.isupper()

# Se todos caracters forem minuscolos -> True
minuscula = d.islower()

# Se a string é apenas espaço em branco (tem que ter literalmente um " ")-> True
td_espaco = d.isspace()

# Se tem letra maiuscula no inicio de cada palavra -> True
# Se tem mais de uma letra maiuscula na palavra -> False
# Se cada palavra começar com letra maiuscula -> True
titolo = d.istitle()


# Se é numérica -> True
numerica = d.isnumeric()

# Se é imprimivel -> True
esc = d.isprintable()


# Se é capitalizada (se a primeira letrar for maiúscula) -> True
cap = iscapitalize(d)


print(
    f"""O tipo primitivo desse valor é {tipo}
Só tem espaços? {td_espaco}
É um número? {numerica}
É alfabético? {letras}
Está em minúsculas?  {maiuscula}
Está em minúsculas?  {minuscula}
Está capitalizada?  {cap}
"""
)
