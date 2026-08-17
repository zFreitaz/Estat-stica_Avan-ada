# import pandas as pd

#dados = {
    #"Nome": ["Ana", "Carlos", "João", "Felipe", "Marcos", "José"],
    #"Idade": [20, 25, 63, 10, 58, 25],
    #"Nota": [10, 5, 9, 8, 7, 3]
#}

#df = pd.DataFrame(dados)

#df["Nota_final"] = df["Nota"] + 1.3

#print(df) 

#import pandas as pd

#dados = {
    #"Produto": ["Mouse", "Teclado", "Monitor", "Gabinete"],
    #"Preço": [80, 50, 800, 250],
    #"Quantidade": [10, 50, 15, 25]
#}

#df = pd.DataFrame(dados)

#df["Valor_total"] = df["Preço"] * df["Quantidade"]

#print(df[(df["Quantidade"]< 20) & (df["Preço"] < 300)])

import pandas as pd

df = pd.read_csv("dados.csv")

print(df)
