import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk


#cotaação historica

tickers = ["^BVSP", "^GSPC", "BRL=X"]

dados_mercado = yf.download(tickers, period = "6mo")
dados_mercado = dados_mercado["Adj Close"]
dados_mercado

#tratar dados

dados_mercado = dados_mercado.dropna()

dados_mercado.columns = ["DOLAR", "IBOVESPA", "S&P500"]

#criar graficos

plt.style.use("cyberpunk")
plt.plot(dados_mercado["IBOVESPA"])
plt.title("IBOVESPA")

plt.show()
plt.savefig("ibovespa.png")

#dolar
plt.plot(dados_mercado["DOLAR"])
plt.title("DOLAR")

plt.show()
plt.savefig("DOLAR.png")

#s&p500
plt.plot(dados_mercado["S&P500"])
plt.title("S&P500")

plt.show()
plt.savefig("S&P500.png")

#calculo de retorno diario 

retorno_diarios = dados_mercado.pct_change()

retorno_diarios

retorno_dolar = retorno_diarios ["DOLAR"].iloc[-1]
retorno_ibovespa = retorno_diarios ["IBOVESPA"].iloc[-1]
retorno_sp = retorno_diarios ["S&P500"].iloc[-1]

retorno_dolar = str(round(retorno_dolar * 100,2)) + "%"

retorno_dolar
retorno_ibovespa = str(round(retorno_ibovespa * 100,2)) + "%"

retorno_ibovespa
retorno_sp = str(round(retorno_sp * 100,2)) + "%"

retorno_sp

#configurar e enviar o email

import win32com.client as win32
outlook = win32.Dispatch("outlook.application")
email = outlook.CreatItem(0)
email.To = "evento@varos.com.br"
email.Subject = "Relatorio de Mercado"
email.Body = f'''Prezado diretor, segue o relatório de mercado:

* O Ibovespa teve o retorno de {retorno_ibovespa}.
* O Dólar teve o retorno de {retorno_dolar}.
* O S&P500 teve o retorno de {retorno_sp}.

Segue em anexo a peformance dos ativos nos últimos 6 meses.

Att,
Melhor estagiário do mundo


'''

anexo_ibovespa = r"C:\Users\gabri\OneDrive\Área de Trabalho\varus\ibovespa.png"
anexo_dolar = r"C:\Users\gabri\OneDrive\Área de Trabalho\varus\DOLAR.png"
anexo_sp =  r"C:\Users\gabri\OneDrive\Área de Trabalho\varus\S&P500.png"
email.Attachments.Add(anexo_ibovespa)
email.Attachments.Add(anexo_dolar)
email.Attachments.Add(anexo_sp)
email.Send()