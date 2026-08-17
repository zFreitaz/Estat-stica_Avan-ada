import pandas as pd

dados = {
    "Aluno": ["João", "Maria", "Pedro", "Ana"],
    "Idade": [18, 20, 19, 22]
}

df = pd.DataFrame(dados)

df.info()


print(df.describe())
print(df.head())
