import pandas as pd

dados = {
    "Produto": ["Mouse", "Teclado", "Monitor", "Webcam", "Headset"],
    "Categoria": ["Periférico", "Periférico", "Vídeo", "Vídeo", "Áudio"],
    "Preço": [80, 120, 900, 250, 300],
    "Quantidade": [10, 8, 4, 6, 5]
}

df = pd.DataFrame(dados)

print(df.shape)
print(df.info())
print(df.describe())


print(df[["Produto", "Preço"]])

print(df.head(2))

print(df.loc[df['Preço'].idxmax()])

df["Valor_Estoque"] = df["Preço"] * df["Quantidade"]

print(df.loc[df["Valor_Estoque"].idxmax(), "Produto"])
print(df.loc[df["Valor_Estoque"].idxmin(), "Produto"])
print(df["Valor_Estoque"].sum())


