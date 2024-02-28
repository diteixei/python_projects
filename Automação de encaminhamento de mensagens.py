# Automação de encaminhamento de mensagens no Whatsapp
# Usando a funcionalidade nativa do Whatsapp de encaminhar mensagens
# Encaminhar de 5 em 5 mensagens, porque o Whatsapp pode bloquer 
# Código lento propositalmente para que o Whatsapp ppense que é uma pessoa

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time #- criar um gap de tempo no código
service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com/")
time.sleep(1) #- esses gaps atrasam, para dar tempo de conectar no Whatsapp
input("Pressione Enter para fechar o navegador...")

mensagem = """Fala galera!
Se inscreve no canal!!!"""

lista_contatos = ["Meu Numero", "Barbosa Carlos"]

# Enviar a mensagem para o meu número para depois encaminhar
# Clicar na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/').send_keys("Meu Numero")
# Escrever Meu Número e depois enter
# Encaminhar a mensagem para a lista de contatos




# clicar na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys("Barbosa carlos")
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(1)

# escrever a mensagem para nós mesmos
pyperclip.copy(mensagem)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + "v")
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)