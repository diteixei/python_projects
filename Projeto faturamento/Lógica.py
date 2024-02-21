import pandas as pd
import win32com.client as win32

#importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

#visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

#faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

#quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

print('-' * 50)
#ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)

#enviar um email com o relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.to = 'diteixei@gmail.com'
mail.Subject = 'Relatório de vendas por loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o relatório de vendas por loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}
<p>Quantidade</p>
{quantidade.to_html()}
<p>Ticket médio por produto em cada loja</p>
{ticket_medio.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att,</p>
<p>Diego</p>
'''

mail.Send()

print("Email enviado")