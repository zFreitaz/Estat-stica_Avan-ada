import pandas as pd
import matplotlib.pyplot as plt

tempos = pd.Series([100, 105, 110, 108, 115, 120, 125, 130, 500, 550])

print(f" Media {tempos.mean()}")

print(f" Mediana {tempos.median()}")

print(f" Moda:" )
print(tempos.mode())

plt.figure()
plt.hist(tempos, edgecolor="black")
plt.title("Histograma dos Tempos de Resposta")
plt.xlabel("Tempo (ms)")
plt.ylabel("Frequência")
plt.show()

plt.figure()
plt.boxplot(tempos)
plt.title("Boxplot dos Tempos de Resposta")
plt.ylabel("Tempo (ms)")
plt.show()