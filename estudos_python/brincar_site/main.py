from requests import get
# from os import chdir, getcwd


data = get('https://www.youtube.com/').content.decode('utf-8')
abrir = open('legal.html', 'w')
abrir.write(data)
abrir.close()