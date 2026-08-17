
import pandas as pd

base = {
    "Produto": ["Mouse", "Teclado", "Munitor", "WebCam", "HeadSet"],
    "Preço": [85, 150, 980, 220, 320],
    "Quantidade": [12, 8, 4, 10, 6]
}

df = pd.DataFrame(base)

print(f"Quantidade de Produtos: {len(df)}")

print(f"Maior preço {df.loc[df['Preço'].idxmax(), 'Produto']}")

print(f"Menor preço {df.loc[df['Preço'].idxmin(), 'Produto']}")

print(f"Soma da Quantidades: {df['Quantidade'].sum()}")