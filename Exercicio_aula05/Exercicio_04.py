import numpy as np

tempos = [100, 200, 500]
quantidades = [500, 300, 200]

soma_ponderada = sum(t * q for t, q in zip(tempos, quantidades))
total_pesos = sum(quantidades)
media1 = soma_ponderada / total_pesos

print(f"Média Ponderada: {media1:.1f} ms")

media2 = np.average(tempos, weights=quantidades)

print(f"Média Ponderada (NumPy): {media2:.1f} ms")
