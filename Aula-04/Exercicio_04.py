import pandas as pd
import matplotlib.pyplot as plt

dados = [  102, 105, 110, 112, 115, 118, 120, 122, 125, 128,
        130, 131, 135, 138, 140, 142, 145, 147, 148, 150,
        152, 153, 155, 158, 160, 162, 165, 167, 169, 170,
        172, 175, 178, 180, 182, 185, 188, 190, 192, 195,
        198, 202, 205, 210, 215, 220, 225, 230, 240, 250
]

serie = pd.Series(dados)


frequencia = serie.value_counts()
print("Frequencia absoluta")
print(frequencia)


frequencia.plot(kind="hist", bin=5)
plt.title("Tempo de resposta")
plt.show()