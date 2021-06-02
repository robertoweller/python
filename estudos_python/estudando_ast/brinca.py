print("""Python 3.8.4 (default, Jul 13 2020, 23:56:11) 
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.""")
exe = ''
t = 'while usu != "sair":\n usu = input("Qual seu nome? ")\n print(f"Prazer de te conhecer {usu}")'
while exe != 'sair':
    exe = input('>>> ')
    exec(exe)


