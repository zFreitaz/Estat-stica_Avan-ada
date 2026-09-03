import pandas as pd
import matplotlib.pylab as plt

tempos = [ 110, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185,
    190, 195, 200, 205, 210, 220, 230, 250, 300, 500 
]

serie = pd.Series(tempos)
frequencia = serie.value_counts()


#frequencia.plot(kind="hist")
#plt.title("Tempso")
#plt.show()


#plt.boxplot(tempos)
#plt.title("Tempos")
#plt.show()


