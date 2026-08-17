import matplotlib.pyplot as plt
import pandas as pd


produtos = ["Mouse", "Teclado", "Monitor", "Webcam", "Headset", "Gabinete"]
precos = [80, 150, 900, 200, 300, 450]
quantidades = [10, 8, 3, 5, 12, 4]


dados = {"Produto": produtos, "Preço": precos, "Quantidade": quantidades}

df = pd.DataFrame(dados)

df["Valor em Estoque"] = df["Preço"] * df["Quantidade"]


print(df)


print(f"Total de produtos cadastrados (len): {len(df)}")


print(f"Total de itens em estoque (sum): {df['Quantidade'].sum()}")
print(f"Valor total investido em estoque (sum): R$ {df['Valor em Estoque'].sum()}")


print(f"Maior preço de produto (max): R$ {df['Preço'].max()}")


print(f"Menor preço de produto (min): R$ {df['Preço'].min()}")
print()


print(df.head(3))
print()


print("--- Resumo Estatístico (describe) ---")
print(df.describe())
print()


print("--- Informações do DataFrame (info) ---")
df.info()

plt.bar(df["Produto"], df["Valor em Estoque"], color="teal")
plt.title("Valor Total em Estoque por Produto")
plt.xlabel("Produtos")
plt.ylabel("Valor em Estoque (R$)")
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()