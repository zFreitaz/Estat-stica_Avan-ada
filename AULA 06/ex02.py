import pandas as pd

GrupoA = [100, 100, 100, 100, 100]
GrupoB = [80, 90, 100, 110, 120]

serie_a = pd.Series(GrupoA)
serie_b = pd.Series(GrupoB)





print("Grupo A:")
print(f"Média: {serie_a.mean()}, Amplitude: {serie_a.max() - serie_a.min()}")
print(f"Variancia Amostral: {serie_a.var()}, Variancia Populacional: {serie_a.var(ddof=0)}")
print(f"Desvio padrão Amostral: {serie_a.std()}, Desvio padrão Populacional: {serie_a.std(ddof=0)}")

print("Grupo B:")
print(f"Média: {serie_b.mean()}, Amplitude: {serie_b.max() - serie_b.min()}")
print(f"Variancia Amostral: {serie_b.var()}, Variancia Populacional: {serie_b.var(ddof=0)}")
print(f"Desvio padrão Amostral: {serie_b.std()}, Desvio padrão Populacional: {serie_b.std(ddof=0)}")