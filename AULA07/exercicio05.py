import numpy as np
import pandas as pd

lancamentos = np.random.randint (1, 7, size=10000)

serie = pd.Series(lancamentos)

frequencia = serie.value_counts().sort_index()
frequencia_relativa = frequencia / len(lancamentos)

probabilidade_teorica = 1/6

tabela = pd.DataFrame({
    "Frequencia": frequencia,
    "Frequencia Relativa": frequencia_relativa * 100,
    "Probabilidade Teórica": probabilidade_teorica * 100
})

print(tabela)