import pandas as pd
import matplotlib.pyplot as plt

base = {
    "Produto": ["Arroz", "Feijão", "Café", "Açucar", "Leite", "Óleo", "Macarrão"],
    "Preço":[32, 11, 24, 6, 8, 9, 7]
}

df = pd.DataFrame(base)

plt.bar(df["Produto"], df["Preço"])

plt.title("Preço dos Produtos de Mercado")
plt.xlabel("Produtos")
plt.ylabel("Preço")

plt.show()

