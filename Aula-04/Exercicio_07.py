import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('usuarios_100.csv')




frequencia_so = df['sistema_operacional'].value_counts()
frequencia_lp = df['linguagem_preferida'].value_counts()
print(frequencia_so)
print(frequencia_lp)


frequencia_so_relativa = df["sistema_operacional"].value_counts(normalize=True)
frequencia_lp_relativa = df["linguagem_preferida"].value_counts(normalize=True)
print(frequencia_so_relativa)
print(frequencia_lp_relativa)


frequencia_so.plot(kind="bar")
plt.title("Sistema Operacional")
plt.xlabel("Frequencia")
plt.ylabel("Sistema")
plt.show()

frequencia_lp.plot(kind="bar")
plt.title("Linguagem Preferida")
plt.xlabel("Frequencia")
plt.ylabel("Sistema")
plt.show()
