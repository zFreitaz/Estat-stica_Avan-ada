import pandas as pd
import matplotlib.pyplot as plt

notas = [7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 9, 8, 10]

serie = pd.Series(notas)

fab = serie.value_counts()

fr = serie.value_counts(normalize=True)

fac = fab.cusmum()

tabela = pd.DataFrame({
    "F_absoluta": fab,
    "F_relativa": fr,
    "F_acumulada": fac

})

fab.plot(kind="bar")

plt.title("Frequencias das Notas")
plt.xlabel("Notas")
plt.ylabel("Frequencia")
#plt.show()

fab.plot(kind="pie", autopct="%1.1%%")

plt.title("Frequencias das Notas")

plt.show()




