import os

# Executar local 
print('Executando chromedriver nesse local > ' + os.getcwd() + '\n ------------------------')

from selenium import webdriver

# --disable-infobars", "--disable-features=EnableEphemeralFlashPermission

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

from time import sleep

# A pagina teste de leitura
canal = 'https://www.twitch.tv/johnpittertv'
abre = 5

# Local do chromedrive e abri ele
browser = webdriver.Chrome(executable_path=f'{os.getcwd()}/chromedriver')

browser.get(canal)

# nav = browser.find_element_by_id("mainnav")

nav = browser.find_elements_by_class_name('text-fragment')

# <span class="text-fragment" data-a-target="chat-message-text">voltou mesmo</span>
try:
    while True:
        for i in nav:
            print(i.text)
        sleep(2)

        # browser.close()
        if abre >= 0:
            browser.refresh()

            nav = browser.find_elements_by_class_name('text-fragment')

            abre -= 1
        else:
            print('------------------------')
            break
        # Vai abrir a quantidade de vezes definida na variavele 'abre'


except KeyboardInterrupt:
    print('------- Leitura do chat fecahda --------')
# browser.close()


