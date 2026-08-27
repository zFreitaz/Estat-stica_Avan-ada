import pandas as pd

alunos = pd.DataFrame({
 "Nome": [
 "Ana", "Bruno", "Carlos", "Daniela",
 "Eduardo", "Fernanda", "Gabriel", "Helena",
 "Igor", "Julia", "Lucas", "Marina"
 ],
 "Idade": [18, 19, 20, 21, 22, 23, 50, 44, 65, 10, 11],
 "Nota": [8, 7, 9, 6, 10, 8, 7, 9, 5, 8, 6, 10]
})

media_populacao = alunos["Idade"].mean()
print(f"Média da populacao: {media_populacao}")