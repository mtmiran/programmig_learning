#!/bin/python3

#Esse programa vai abrir os principais sites que eu uso (gmail, watsapp, youtube, duckduckgo)

''' lembrando que selenium e gecko(para o firefox) tem q estar instalados
- pip3 install selenium
- geckodriver: 
    https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
    tar -xvzf geckodriver-v0.26.0-linux64.tar.gz
    chmod +x geckodriver
    sudo mv geckodriver /usr/local/bin
    ou
    sudo mv geckodriver "$install_dir"
'''

# Importando as bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # keybindings do browser

# Criando a variável Browser e abrindo o primeiro site
browser = webdriver. Firefox()
browser.get('https://mail.google.com/mail/u/0/#inbox')

# Segunda aba com o segundo site
browser.execute_script("window.open('https://duckduckgo.com/')")

# Terceira aba com o terceio site
browser.execute_script("window.open('https://www.youtube.com/')")

# Quarta aba quarto site
browser.execute_script("window.open('https://web.whatsapp.com')")
