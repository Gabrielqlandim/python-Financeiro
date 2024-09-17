import MetaTrader5 as mt5
import time

#iniciar metatrader

mt5.initialize()

#pegar simbolos disponiveis
simbolos = mt5.symbols_get()
print(simbolos)

simbolos[0].name

mt5.symbol_select("EGIE3")

#pegar cotações e retornar 
preco_em_tempo_real = mt5.symbol_info("PETR4").last
retorno_em_tempo_real = mt5.symbol_info("PETR4").price_change
print(preco_em_tempo_real)

tempo = time.time() + 10
tempo = 16 +1
tempo = 17

while (time.time() < tempo):
    tick = mt5.symbol_info_tick("PETR4")
    print(f"O fechamento é {tick.last}")
    print(f"O valor de compra é {tick.ask}")
    print(f"O valor de venda é {tick.bid}")
    print("----------------------------")
    time.sleep(1)
