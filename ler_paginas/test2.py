from time import sleep
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import os

# Local do chromedrive
pasta = f'{os.getcwd()}/chromedriver'

if os.path.isdir('ler_paginas'):
    pasta = f'{os.getcwd()}/ler_paginas/chromedriver'


#object of Options class
op = webdriver.ChromeOptions()


#add user Agent
op.add_argument
("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
+"AppleWebKit/537.36 (KHTML, like Gecko)"
+"Chrome/87.0.4280.141 Safari/537.36")


#set chromedriver.exe path
driver = webdriver.Chrome(executable_path=pasta, options=op)

#launch URL
driver.get("https://site112.com/qual-o-meu-user-agent")

#get user Agent with execute_script
a = driver.execute_script("return navigator.userAgent")

print("\nUser agent:")
print(a)
sleep(60)
# driver.implicitly_wait(60)
driver.quit()

# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36

# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36