# listar arquivos
import os

arquivos = os.listdir()
print(arquivos)

#caminho da pasta
caminho = os.getcwd()
print(caminho)

# renomear
#os.rename('Vendas 1.xlsx', 'Vendas - 1.xlsx')

# mover
#os.rename('Vendas - 1.xlsx', 'Vendas\Vendas - 1.xlsx')

# copiar arquivos
#import shutil

#shutil.copy2('Vendas - 1.xlsx', 'Vendas\Vendas - 1.xlsx')
import os

lista_arquivos = os.listdir()

for arquivo in lista_arquivos:
    if 'xlsx' in arquivo:
        if"Compras" in arquivo:
            #jogar para a pasta de compras
            os.rename(arquivo, f'Compras//{arquivo}')
        elif "Vendas" in arquivo:
            #jogar para a pasta de vendas
            os.rename(arquivo, f'Vendas//{arquivo}')

#A maneira correta de executar um script Python 
#é abrir um terminal (prompt de comando ou PowerShell) e usar 
#o comando python seguido do caminho do seu script. Algo assim:

# python C:/Users/ditei/Downloads/Mover\ arquivos\ do\ computador/Mover.py
