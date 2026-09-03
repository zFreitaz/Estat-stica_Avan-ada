import pandas as pd

notas = pd.Series([7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 
9, 8, 10])

print(f" Média {notas.mean()}")
print(f" Mediana {notas.median()}")
print(f" Moda:" )
print(notas.mode())

print(f" Maximo: {notas.max()}, Minimo: {notas.min()} ")

## É 7,5 pois representa a Média e Mediana
