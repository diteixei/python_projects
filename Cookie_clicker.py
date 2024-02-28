from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Importe a classe Service do módulo correto
import time

class CookieClicker: 
    def __init__(self):
        # Corrija o caminho do executável do Chrome
        chrome_path = "C:\\Users\\ditei\\anaconda3\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe"
        service = Service(chrome_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
