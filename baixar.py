# pip3 install wget
import wget

# Lista de downloads
d = ['https://5ca0e999-de9a-47e0-9b77-7e3eeab0592c.usrfiles.com/ugd/5ca0e9_7409071f696845778d14c0b6e4f9d2da.pdf', 'https://s1.static.brasilescola.uol.com.br/vestibular/arquivos/cartilha-redacao-a-mil-2018.pdf'] 

 
for baixando in d:
    nome_arquivo = wget.download(baixando)

print('\n Terminou!')

