import pandas as pd

tabela = pd.read_excel("Vendas.xlsx")
print(tabela)

faturamento_total = tabela["Valor Final"].sum()
print(faturamento_total)

# faturamento por loja
faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(faturamento_por_loja)

# faturamento por produto
faturamento_por_produto = tabela[["ID Loja","Produto", "Valor Final"]].groupby(["ID Loja","Produto"]).sum()
print(faturamento_por_produto)

#https://pages.hashtagtreinamentos.com/python-vtsd-aula-analise-dados?src=lespy-em14