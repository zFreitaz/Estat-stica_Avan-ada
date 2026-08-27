import pandas as pd

tabela = pd.read_csv('dados.csv')

print(tabela.head())

serie = tabela["cidade"]

frequencia = serie.value_counts()
frequencia_acumulada = frequencia.cumsum()

tabela = pd.DataFrame({
    "Frequenica": frequencia,
    "Frequencia_Relativa": frequencia / len(serie),
    "Frequencia_Acumulada": frequencia_acumulada
})

print((tabela))