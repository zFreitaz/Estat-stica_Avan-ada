import pandas as pd

notas = [
    7, 8, 6, 9, 7,
    5, 8, 7, 10, 6,
    8, 9, 7, 5, 6,
    8, 7, 9, 8, 10
]

# TRANSFORMA O VETOR EM TIPO SERIES
serie = pd.Series(notas)

#Ele conta quantas vezes cada valor aparece
#print(serie.value_counts())

# Ordenando as Frequências
#print(serie.value_counts().sort_index())

# Ordenando pela Frequência
#print(serie.value_counts().sort_values())

# Frequência Relativa
#print(serie.value_counts(normalize=True))

# Frequência Relativa /Porcentagem
#print(serie.value_counts(normalize=True) * 100)

# Frequência Acumulada
#frequencia = serie.value_counts().sort_index()
#frequencia_acumulada = frequencia.cumsum()

#print(frequencia_acumulada)
# O final sempre tem que ser a soma do conjunto

# QUANTIDADE ABSLOTUA É A QUANTIDADE DE VEZES QUE APARECE
# RELATIVA = QUANTIDADE TOTAL 
# ACUMULADA = SOMATÓRIO DAS FREQUÊNCIAS

frequencia = serie.value_counts().sort_index()
frequencia_acumulada = frequencia.cumsum()

tabela = pd.DataFrame({
    "Frequenica": frequencia,
    "Frequencia_Relativa": frequencia / len(serie),
    "Frequencia_Acumulada": frequencia_acumulada
})

print((tabela))




