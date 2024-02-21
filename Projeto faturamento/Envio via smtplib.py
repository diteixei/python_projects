import smtplib
from email.mime.text import MIMEText

# Configurações de e-mail
de = 'seu_email@gmail.com'
para = 'diteixei@gmail.com'
assunto = 'Relatório de vendas por loja'
mensagem = '''
Prezados,

Segue o relatório de vendas por loja.

Faturamento:
{}
Quantidade
{}
Ticket médio por produto em cada loja
{}

Qualquer dúvida estou à disposição.

Att,
Diego
'''.format(faturamento, quantidade, ticket_medio)

# Configurações do servidor SMTP do Gmail (altere conforme necessário)
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_usuario = 'seu_email@gmail.com'
smtp_senha = 'sua_senha'

# Criar mensagem
msg = MIMEText(mensagem)
msg['Subject'] = assunto
msg['From'] = de
msg['To'] = para

# Conectar e enviar e-mail
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_usuario, smtp_senha)
    server.sendmail(de, [para], msg.as_string())
    server.quit()
    print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar e-mail: {e}')
