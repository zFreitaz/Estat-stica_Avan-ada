import numpy as np

requisicoes = np.random.choice( ["Sucesso", "Erro"], size=10000, p=[0.95, 0.05])

total = len(requisicoes)
total_erros = (requisicoes == "Erro").sum()
porcentagem_erro = (total_erros / total ) * 100

print("Total de requisições", total)
print("Total de erros", total_erros)
print("Porcentagem de erros", porcentagem_erro, "%")