import pandas as pd


dados = {
    "Produto": ["Teclado Mecânico", "Mouse Gamer", "Monitor 24", "Headset", "Mousepad", "Webcam 1080p", "Microfone USB", "Cadeira Gamer", "Gabinete ATX", "Fonte 600W", "Memória RAM 16GB", "SSD 1TB", "Placa de Vídeo", "Processador", "Cooler CPU"],
    "Categoria": ["Periféricos", "Periféricos", "Monitores", "Áudio", "Acessórios", "Periféricos", "Áudio", "Móveis", "Hardware", "Hardware", "Hardware", "Hardware", "Hardware", "Hardware", "Hardware"],
    "Preço": [250.00, 120.00, 850.00, 180.00, 45.00, 190.00, 220.00, 950.00, 320.00, 280.00, 210.00, 350.00, 2200.00, 1100.00, 95.00],
    "Quantidade": [12, 25, 4, 8, 30, 6, 3, 2, 7, 10, 15, 8, 3, 5, 14]
}


df = pd.DataFrame(dados)


df["Valor_Estoque"] = df["Preço"] * df["Quantidade"]


print("=== 3. PRIMEIROS 5 REGISTROS ===")
print(df.head(5))


print("\n=== 4. INFORMAÇÕES DA TABELA ===")
df.info()


preco_medio = df["Preço"].mean()
print(f"\n=== 5. PREÇO MÉDIO ===\nR$ {preco_medio:.2f}")


produto_mais_caro = df.loc[df["Preço"].idxmax()]
print(f"\n=== 6. PRODUTO MAIS CARO ===\n{produto_mais_caro['Produto']} (R$ {produto_mais_caro['Preço']:.2f})")


produto_mais_barato = df.loc[df["Preço"].idxmin()]
print(f"\n=== 7. PRODUTO MAIS BARATO ===\n{produto_mais_barato['Produto']} (R$ {produto_mais_barato['Preço']:.2f})")


df_ordenado_estoque = df.sort_values(by="Valor_Estoque", ascending=False)
print("\n=== 8. ORDENADO PELO VALOR DO ESTOQUE ===")
print(df_ordenado_estoque[["Produto", "Preço", "Quantidade", "Valor_Estoque"]])


produtos_baixo_estoque = df[df["Quantidade"] < 5]
print("\n=== 9. ESTOQUE INFERIOR A 5 UNIDADES ===")
print(produtos_baixo_estoque[["Produto", "Quantidade"]])


valor_total_geral = df["Valor_Estoque"].sum()
print(f"\n=== 10. VALOR TOTAL DO ESTOQUE ===\nR$ {valor_total_geral:.2f}")