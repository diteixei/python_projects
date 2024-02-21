from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

# acessar o site https://www.jusbrasil.com.br/jurisprudencia/
driver = webdriver.Chrome()
driver.get('https://www.jusbrasil.com.br/jurisprudencia/')

# login
driver.find_element('xpath', '/html/body/div[2]/topbar/header/div/div/span[2]/a').click()

# Aguardar antes de fechar a página
input("Pressione Enter para continuar...")

driver.find_element('//*[@id="root"]/div/div[2]/div[2]/div[2]/form/fieldset[1]').send_keys("chancelis.adv@gmail.com")

driver.find_element('xpath', '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/fieldset[2]"]').send_keys("chancelis")

driver.find_element('xpath', '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/button').click()

# selecionar tipo: jurisprudencia
xpath_input = '//*[@id="CourtsBottomSearch-form"]/fieldset/div/input'
jurisprudencia = driver.find_element(By.XPATH, xpath_input)
jurisprudencia.send_keys("Cobrança indevida rj")

# digitar o texto
xpath_button = '//*[@id="CourtsBottomSearch-form"]/fieldset/div/div[1]/button'
driver.find_element(By.XPATH, xpath_button).click()

# Agora, fazer a requisição HTTP usando a biblioteca requests
url = driver.current_url  # Obter a URL atual do Selenium
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

# O restante do seu código aqui...

# Aguardar antes de fechar a página
input("Pressione Enter para fechar a página...")

# Fechar o navegador
driver.quit()

d#ef proximapagina(soup):
    #procurar botao proxima pagina
    #paginas = soup.find('a', {'class': '//*[@id="__next"]/div/main/div[1]/div/nav/ul/li[2]/ul/li[2]'})
    #ir na ultima pagina com o botao proxima desativado
    #if not paginas.find('span', {'class': '//*[@id="__next"]/div/main/div[1]/div/nav/ul/li[2]/ul/li[4]'})
