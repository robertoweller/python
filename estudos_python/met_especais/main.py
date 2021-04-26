"""
Faça um programa que contenha uma classe
IntSet. No método de inicialização __init__
desta classe, deve ser inicializado um 
atributo vals do tipo lista. Esta classe também
deve conter outros dois métodos. O primeiro
método deve receber como argumento número inteiro
e deve adicionar este valor na lista vals somente se
o valor ainda não esteja presente nesta lista.
Já o segundo método deve utilizar o método especial
__str__ e retornar uma string que representa os 
valores contidos em vals no formato {v1, v2, v3, ...}.
No programa principal deve ser feita a instanciação da
classe IntSet, juntamente com um laço para a inserção dos
valores. O laço deve se repetir até que a string "s" seja
digitada, quando deverá ser exibido o conjunto de inteiro
presentes na classe IntSet e então encerrar o programa. Dica:
utilize a função auxiliar str_to_int(s) para verificar se uma
string s é do tipo int.

Exemplo de saída:

---------------------------------------
Insira um valor (ou s para sair): 1
Insira um valor (ou s para sair): 3
Insira um valor (ou s para sair): 5
Insira um valor (ou s para sair): 5
Insira um valor (ou s para sair): 5
Insira um valor (ou s para sair): -2
Insira um valor (ou s para sair): 1
Insira um valor (ou s para sair): s

Valores contidos no conjunto de inteiros:
{1, 3, 5, -2}
---------------------------------------

def str_is_int(s):
    try:
        int(s)
        return True
    except ValueErro:
        return False

"""


class IntSet:

    vals = list()

    def __init__(self, inteiro):

        self.inteiros(inteiro)
    
    def inteiros(self, inte):
        # Se for diferentede s vai adicionar

            if inte not in self.vals and self.str_is_int(inte):
                
                self.vals.append(inte)
         

    def __str__(self):

        self.xxx = ', '.join(map(str, self.vals))
        
        return '{'+ self.xxx +'}'
    

    def str_is_int(self, s):
        try:
            int(s)
            return True

        except ValueError:
            
            return False
            


if __name__ == '__main__':
    
    per = input("Insira um valor (ou s para sair): ")

    # Se digitar uma letra diferente de s, continua o looping
    # mas não adiciona a lista
    while IntSet(per).str_is_int(per) or per != "s":

        per = input("Insira um valor (ou s para sair): ")
    
    print(
        f'\nValores contidos no conjunto de {IntSet.inteiros.__name__}:\n'
        f'{IntSet("")}')