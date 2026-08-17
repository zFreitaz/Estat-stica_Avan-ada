import pandas as pd
import matplotlib.pyplot as plt

base = {
    "Time": ["Palmeiras", "Flamengo", "Corinthians", "São Paulo", "Santos"],
    "Pontos": [48, 46, 41, 38, 35]
}

df = pd.DataFrame(base)

print("--- Tabela do Campeonato ---")
print(df)

plt.bar(df["Time"], df["Pontos"])
plt.title("Tabela Brasileirão")
plt.xlabel("Times")
plt.ylabel("Pontos")

plt.show()
