import numpy as np

# Gerando 100.000 lançamentos para cada dado de forma independente
dado1 = np.random.randint(1, 7, 100000)
dado2 = np.random.randint(1, 7, 100000)

# Verificando onde AMBOS os dados resultaram em 6
resultado_duplo_1 = (dado1 == 1) & (dado2 == 1)
resultado_duplo_2 = (dado1 == 2) & (dado2 == 2)
resultado_duplo_3 = (dado1 == 3) & (dado2 == 3)
resultado_duplo_4 = (dado1 == 4) & (dado2 == 4)
resultado_duplo_5 = (dado1 == 5) & (dado2 == 5)
resultado_duplo_6 = (dado1 == 6) & (dado2 == 6)

#resultado_duplo_igual = (dado1 == dado2)

# Probabilidade experimental (proporção de True)
prob_simulacao1 = resultado_duplo_1.mean()
prob_simulacao2 = resultado_duplo_2.mean()
prob_simulacao3 = resultado_duplo_3.mean()
prob_simulacao4 = resultado_duplo_4.mean()
prob_simulacao5 = resultado_duplo_5.mean()
prob_simulacao6 = resultado_duplo_6.mean()

result_um_dois = (dado1 == 2) | (dado2 == 2)
resultado_um_dois = result_um_dois.mean()

pro_duplo_igual = prob_simulacao1 + prob_simulacao2 + prob_simulacao3 + prob_simulacao4 + prob_simulacao5 + prob_simulacao6
prob_teorica = 1 / 36

print(f"Probabilidade Experimental: {resultado_um_dois:.4f} ({resultado_um_dois*100:.2f}%)")
print(f"Probabilidade Teórica (1/36): {resultado_um_dois:.4f} ({resultado_um_dois*100:.2f}%)")