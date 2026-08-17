import pandas as pd

lista = [12, 25, 18, 40, 32, 11, 9, 28, 37, 15]

df = pd.DataFrame(lista, columns=["Nota"])

print(len(lista))

print(sum(lista))

print(df["Nota"].mean())

print(f"Maior valor {df['Nota'].max()}")

print(f"Menor valor {df['Nota'].min()}")

df_ordenado = df.sort_values(by="Nota")
print(df_ordenado)
