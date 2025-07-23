#Instalar:
# Pandas
# openpyxl
# twilio

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "TWILIO_ACCOUNT_SID"
# Your Auth Token from twilio.com/console
auth_token = "TWILIO_AUTH_TOKEN"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em excel;
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000). any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values [0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas {vendas}')
        message = client.messages.create(
            to= 'YOUR_PHONE_NUMBER',
            from_= "YOUR_TWILIO_PHONE_NUMBER,
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas {vendas}')
        print(message.sid)

# Para cada arquivo:

# Verificar se algum valor naquele arquivo na coluna Vendas é maior que 55.000;

# Se for maior que 55.000 -> Enviar SMS como Nome, Mês e o volume de Vendas do Vendedor

# Caso não seja maior que 55.000 nao fazer nada

