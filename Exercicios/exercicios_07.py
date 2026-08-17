import pandas as pd

dados = {
    "Nome": ["Ana","Bruno","Carlos","Daniela","Eduardo","Fernanda","Gabriel","Helena", "Igor","Julia", "Lucas","Mariana", "Nicolas","Olivia", "Pedro", "Rafaela","Samuel","Tatiana","Vinicius","Yasmin", ],
    "Idade": [18,19,20,18,21,22,19,20,18,23, 21,19,20,22,18, 21, 19, 20,22,18, ],
    "Nota": [ 8.5, 7.0,9.2, 6.5,8.0,9.5,7.8, 8.9, 5.5,9.0, 6.8,8.2, 7.5,9.8,6.0,8.7,7.2,8.4, 9.1, 7.9,],
}

df = pd.DataFrame(dados)

print(df.head())
print(df.describe())
print(df.info)