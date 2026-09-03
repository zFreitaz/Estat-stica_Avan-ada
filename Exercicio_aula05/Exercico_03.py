import pandas as pd

salarios = pd.Series([2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 
2800, 20000])

# 2450 Representa a média do salário dos funcionários
print(f" Media {salarios.mean()}")


print(f" Mediana {salarios.median()}")

# Não possui moda essa desgraça
print(f" Moda:" )
print(salarios.mode())


# A desgraça do valor do Chefe é muito descrepante, puxou a média pra 41600, portanto isso não
# representa a média do salário dos funcionários, ou seja, uma pura ilusão



