from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# acessar o site https://www.novaliderinformatica.com.br/computadores-gamers
driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/computadores-gamers')

# extrair todos os títulos
titulos = driver.find_elements(By.XPATH,"//a[@class='nome-produto']")
# extrair todos os preços
precos = driver.find_elements(By.XPATH,"//strong[@class='preco-promocional']")

# Criando a planilha
workbook = openpyxl.Workbook()
# Criando a página 'produtos'
workbook.create_sheet('produtos')
# Seleciono a página produtos
sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'


# inserir os títulos e preços na planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text,preco.text])

workbook.save('produtos.xlsx')

# como entregar para o cliente