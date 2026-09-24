import numpy as np

n_lancamentos = 100000
dado1 = np.random.randint(1, 7, size=n_lancamentos)
dado2 = np.random.randint(1, 7, size=n_lancamentos)

mesmo_numero = (dado1 == dado2)
prob_exp = np.mean(mesmo_numero)

prob_teorica = 6/36

dif_percentual = abs(prob_exp - prob_teorica) / prob_teorica * 100

print(f"Probabilidade Experimental: {prob_exp:.4f} ({prob_exp * 100:.2f}%)")
print(f"Probabilidade Teórica: {prob_teorica:.4f} ({prob_teorica * 100:.2f}%)")
print(f"Diferença Relativa: {dif_percentual:.2f}%")