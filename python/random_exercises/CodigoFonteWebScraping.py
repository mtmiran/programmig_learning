'''
1. Pegar conteúdo HTML a partir da URL
2. Parsear o conteúdo HTML - BeaultifulSoup
3. Estruturar o conteúdo em um Data Frame - Pandas
4. Transformar os Dados em um Dicionário de dados próprio 
5. converter e salvar em um arquivo JSON

Instalar

pip3 install requests2
pip3 install pandas
pip3 install lxml
pip3 install beautifulsoup4
pip3 install selenium
'''
# Bibliotecas

import time
import requests
import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# 1 Pegar conteúdo HTML a partir da URL

url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"

option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.get(url)
time.sleep(10)

driver.find_element




driver.quit()