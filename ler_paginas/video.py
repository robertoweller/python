from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
# from time import sleep
import os

# A pagina teste de leitura
# https://animeshouse.net/episodio/spyxfamily-s1-episodio-1-legendado-hd/
site = 'https://animeshouse.net/episodio/spyxfamily-s1-episodio-1-legendado-hd/'




opts = Options()
opts.add_argument("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174")

# Local do chromedrive
pasta = f'{os.getcwd()}/chromedriver'

if os.path.isdir('ler_paginas'):
    pasta = f'{os.getcwd()}/ler_paginas/chromedriver'

browser = webdriver.Chrome(executable_path = pasta, chrome_options=opts)

browser.get(site)

# sleep(20)

# sejasaudavel
# tag = browser.find_element_by_tag_name('video')


# Url da pagina que está
# driver.current_url

# print(browser.find_elements())
# Click the link to activate the alert

# WebDriverWait(driver, timeout=10).until(document_initialised)

browser.implicitly_wait(0.5)
agent = browser.execute_script("return navigator.userAgent")

print('\n', browser.title)
print( browser.current_url)

print("\n\n", agent)

# print(browser.create_web_element())
# https://animeshouse.net/episodio/spyxfamily-s1-episodio-1-legendado-hd/
browser.implicitly_wait(60)

browser.close()




"""Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"""
