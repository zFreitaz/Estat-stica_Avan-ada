import pandas as pd

dados = {
    "Filme": ["O Poderoso Chefão", "Interestelar", "Parasita", "Vingadores: Ultimato", "O Iluminado", "A Origem", "Matrix", "Coringa"],
    "Gênero": ["Crime/Drama", "Ficção Científica", "Suspense/Drama", "Ação/Aventura", "Terror", "Ficção Científica", "Ficção Científica", "Drama/Crime"],
    "Ano": [1972, 2014, 2019, 2019, 1980, 2010, 1999, 2019],
    "Nota": [9.2, 8.7, 8.5, 8.4, 8.4, 8.8, 8.7, 8.4]
}

df = pd.DataFrame(dados)

filmes_nota_maior_8 = df[df["Nota"] > 8]


df_ordenado = df.sort_values(by="Nota", ascending=False)


maior_nota = df["Nota"].max()


menor_nota = df["Nota"].min()

media_notas = df["Nota"].mean()


print("=== 1. NOTA > 8 ===")
print(filmes_nota_maior_8)

print("\n=== 2. ORDENADOS POR NOTA ===")
print(df_ordenado)

print(f"\n=== 3. MAIOR NOTA: {maior_nota} ===")
print(f"=== 4. MENOR NOTA: {menor_nota} ===")
print(f"=== 5. MÉDIA DAS NOTAS: {media_notas:.2f} ===")