import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def simulacion(data,ticker,dia_inicial,N_dias,N_escenarios):
    delta=data.pct_change().dropna()
    delta_sim=np.random.normal(delta[ticker].mean(),delta[ticker].std(),(N_dias,N_escenarios))
    rango_tiempo=pd.date_range(dia_inicial,periods=N_dias)
    delta_sim=pd.DataFrame(delta_sim,index=rango_tiempo)
    precios_simulados=data[ticker].iloc[-1]*((delta_sim+1).cumprod())
    B = precios_simulados>data[ticker].iloc[-1]*1.08
    return B.mean(axis=1)


# marca de amazon:
ticker = "AMZN"
data = yf.download(ticker, start="2015-10-24", end="2025-10-24")["Close"]
data.plot(grid=True)
plt.show()

# Simulamos cien mil escenarios de los próximos 30 días
N_dias = 30
N_escenarios = 100000

prob = simulacion(data, ticker, '2025-10-24', N_dias, N_escenarios)

# Graficamos la evolución de la probabilidad
prob.plot(grid=True, label='Probabilidad > +8%')
plt.title("Probabilidad acumulada de que el precio supere +8%")
plt.xlabel("Fecha")
plt.ylabel("Probabilidad")
plt.legend()
plt.show()

# Probabilidad final al día 30
print(f"Probabilidad al día 30 de superar +8%: {prob.iloc[-1]:.2%}")


