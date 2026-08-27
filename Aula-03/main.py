import pandas as pd


df = pd.read_csv("dados.csv")

amostra = df.sample(n=100)

medPopulacao = df["idade"].mean()
print(f"Média Populaçãp:{medPopulacao}")

medAmostra = amostra["idade"].mean()
print(f"Média da amostra: {amostra["idade"].mean()}")

print(f"Erro amostral: {medPopulacao - medAmostra}")