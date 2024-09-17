from datetime import datetime, date
from matplotlib import pyplot as plt
import numpy as np
from bcb import sgs

#coletar dados do ususario

capital = float(input("Digite o seu capital investido: "))
frequencia = input("Digite a frequencia do periodo (Y, M, D) : ")
inicio = input("Digite a data inicial maior do que 1995/01/01 no formato YYYY/MM/DD: ")
final = input("Digite a data final no seguinte formato YYYY/MM/DD: ")

#tratar os dado coletados

data_incial = datetime.strptime(inicio, "%Y/%m/%d").date()
data_final = datetime.strptime(final, "%Y/%m/%d").date()

#pegar dados da selic

taxas_selic = sgs.get({"selic": 11}, start = data_incial, end = data_final)
taxas_selic = taxas_selic/100
print(taxas_selic)
#calcular

capital_acumulado = capital *(1 + taxas_selic["selic"]).cumprod() - 1
print(capital_acumulado)

capital_com_frequencia = capital_acumulado.resample(frequencia).last()
print(capital_com_frequencia)

#parte 2

#filtrar dados

data_incial_2 = date(2000,1,1)
data_final_2 = date(2022,3,31)
selic_questao_2 = sgs.get({"selic": 11}, start = data_incial_2, end = data_final_2)
selic_questao_2 = selic_questao_2/100
print(selic_questao_2)

#calcular rentabilidade

janelas_500_dias = ((1 + selic_questao_2).rolling(window = 500).apply(np.prod)-1)
print(janelas_500_dias)

janelas_500_dias = janelas_500_dias.reset_index()
print(janelas_500_dias)

#criar range de datas na tabela

janelas_500_dias["data_inicial"] = janelas_500_dias["Date"].shift(500)
print(janelas_500_dias)

janelas_500_dias = janelas_500_dias.dropna()
print(janelas_500_dias)

janelas_500_dias.columns = ["data_final", "retorno_selic_500", "data_inicial"]

print(janelas_500_dias)

#pegar maior retorno da tabela

maior_retorno = janelas_500_dias["retorno_selic_500"].max()
print(maior_retorno)

gabarito = janelas_500_dias[janelas_500_dias["retorno_selic_500"] == maior_retorno]
print(gabarito)