import pandas as pd
import matplotlib.pyplot as plt

base = {
    "Produto": ["Ferro", "Tesoura", "Chinelo", "Borracha"],
    "Preço": [50, 8, 27, 9],
    "Quantidade": [1, 2, 1, 5]
}

df = pd.DataFrame(base)

plt.plot(
    df["Preço"], df["Quantidade"],
    color="black"
    ) 
 
plt.title("Grafíco de Aura")
plt.xlabel("Preço")
plt.ylabel("Quantidade")
plt.show()

plt.bar(df["Produto"], df["Quantidade"])
plt.show()
plt.bar(df["Preço"], df["Produto"])
plt.show()