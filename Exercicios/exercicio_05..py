import pandas as pd
import matplotlib.pyplot as plt


base = {
    "Filme": ["Avatar", "Matrix", "Interestelar", "Vingadores", "Barbie"],
    "Nota": [9.2, 9.5, 9.8, 8.9, 7.5]
}

df = pd.DataFrame(base)

print(df)

print(df.head())

print(df.describe())

plt.bar(df["Filme"], df["Nota"])
plt.title("Notas dos Filmes")
plt.xlabel("Filmes")
plt.ylabel("Notas")

plt.show()