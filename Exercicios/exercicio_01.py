import pandas as pd

base = {
    "Nome": ["João", "Maria", "Pedro", "Ana", "Lucas", "Julia", "Carlos", "Fernanda"],
    "Idade": [18, 20, 19, 22, 21, 18, 23, 20]
}

df = pd.DataFrame(base)

print(df)
print(df.head(5))
df.info()
print(df.describe())


