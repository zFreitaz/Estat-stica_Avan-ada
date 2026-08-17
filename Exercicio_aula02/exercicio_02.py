import pandas as pd

dados = {
    "Alunos": ["Vinícius", "Rafael", "Gabriel", "Fabrício", "Vitor", "Miguel", "Renan", "Carlos", "Guilherme", "Jorge"],
    "Idade": [20, 25, 24, 20, 20, 19, 19, 19, 21, 21],
    "Nota": [10, 9, 8, 7, 9, 4, 9, 1, 10, 7]
}

df = pd.DataFrame(dados)

print(df["Nota"].mean())

print(df["Nota"].max())

print(df["Nota"].min())

print(df.sort_values("Nota"))

print(df[df["Nota"] >= 7]["Alunos"])