import pandas as pd
import matplotlib.pyplot as plt

Linguagens = ['Python', 'Java', 'Python', 'JavaScript', 'Python', 'C#', 
'Java', 'Python', 'C#', 'Python']

serie_linguagens = pd.Series(Linguagens)

freq_absoluta = serie_linguagens.value_counts()

print(" === Frequência Absoluta ===")
print(freq_absoluta)


print(f" Moda: {serie_linguagens.mode()}")

freq_relativa = serie_linguagens.value_counts(normalize=True) * 100

print(" === Frequência Relativa === ")
print(freq_relativa)

plt.figure()
plt.bar(freq_absoluta.index, freq_absoluta.values, color="teal", edgecolor="black")
plt.title("Preferência de Linguagens de Programação")
plt.xlabel("Linguagens")
plt.ylabel("Quantidade de Votos")
plt.show()