import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Jogos": ["Minecraft", "Lol", "GTA V", "Tetris", "The Witcher 3", "Valorant", "Elden Ring", "Fifa 24", "God of War", "Cyberpunk"],
    "Nota": [9.3, 9.6, 8.8, 9.8, 8.2, 9.7, 7.5, 9.5, 8.4, 9.2],
    "Horas_Jogadas": [350, 200, 45, 120, 300, 150, 180, 80, 95, 210]
}

df = pd.DataFrame(dados)

print(df)


plt.bar(df["Jogos"], df["Nota"])
plt.title("Jogos e suas Avaliações")
plt.xlabel("Jogos")
plt.ylabel("Notas")
plt.show()

plt.bar(df["Jogos"], df["Horas_Jogadas"])
plt.title("Jogos e suas Horas jogadas")
plt.xlabel("Jogos")
plt.ylabel("Horas Jogadas")
plt.show()

print(df.head())
print(df.describe())
print(df.info)
