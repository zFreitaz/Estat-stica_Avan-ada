import pandas as pd

grupo_a = pd.Series([10, 10, 10, 10, 10])
grupo_b = pd.Series([2, 6, 10, 14, 18])

media_a = grupo_a.mean()
mediana_a = grupo_a.median()

print(f" Media do Grupo A {media_a}")
print(f" Mediana do Grupo A {mediana_a}")

media_b = grupo_b.mean()
mediana_b = grupo_b.median()

print(f" Media Grupo B {media_b}")
print(f" Mediana Grupo B {mediana_b}")

# Não, mesmo tendo respostas iguais, não devemos olhar para o calculo no geral, e sim observar as ocilações
# que diferem ambos

# Por causa das ocilações, por exemplo, a latencia de uma API, mesmo tendo os valores iguais, o grupo B ainda sim vai ter ocilações
