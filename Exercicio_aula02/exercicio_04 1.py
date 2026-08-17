import pandas as pd

dados = {
    "Produto": ["Escova", "Pasta", "Fio-Dental", "Raspador", "Creme", "Tesoura", "Barbeador", "Esfoleante"],
    "Categoria": ["Higiene Bucal", "Higiene Bucal", "Higiene Bucal", "Higiene Bucal", "Cuidados Pele", "Acessórios", "Barbearia", "Cuidados Pele"],
    "Preço": [15.00, 8.50, 12.00, 25.00, 110.00, 45.00, 150.00, 105.00],
    "Quantidade": [30, 50, 40, 8, 5, 12, 6, 4],
}

df = pd.DataFrame(dados)

df["Valor_Total"] = df["Preço"] * df["Quantidade"]

df_ordenado = df.sort_values("Preço")

produtos_preco_maior_100 = df[df["Preço"] > 100]

produtos_qtd_menor_10 = df[df["Quantidade"] < 10]

print("--- TABELA COMPLETA COM VALOR TOTAL ---")
print(df)

print("\n--- ORDENADO POR PREÇO ---")
print(df_ordenado)

print("\n--- PREÇO > R$ 100 ---")
print(produtos_preco_maior_100)

print("\n--- QUANTIDADE < 10 ---")
print(produtos_qtd_menor_10)