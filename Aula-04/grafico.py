import pandas as pd
import matplotlib.pyplot as plt

notas = [5, 6, 7, 8, 9, 10]
frequencia = [2, 3, 5, 6, 3, 2]

plt.bar(notas, frequencia)

plt.xlabel("Nota")

plt.ylabel("Frequência")

plt.title("Frequências das Notas")