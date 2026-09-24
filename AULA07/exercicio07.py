import numpy as np

total_requisicoes = 10000
taxa_erro_teorico = 0.02

requisicoes = np.random.choice(
    ["Sucesso", "Erro"],
    size=10000,
    p=[0.98, 0.02]
    )

quantidade_sucessos = (requisicoes == "Sucesso").sum()
quantidade_erros = (requisicoes == "Erro").sum()

taxa_sucesso = quantidade_sucessos / total_requisicoes
taxa_erro = quantidade_erros / total_requisicoes

diferenca__erro = taxa_erro - taxa_erro_teorico

print("=" * 50)
print("       Relatorio de monitoramneto da API")
print("=" * 50)

print(f"Total de requisições Simuladas {total_requisicoes}")

print(
    f"Sucessos: {quantidade_sucessos}"
    f"({taxa_sucesso * 100})%"
    )

print(
    f"Erros:     {quantidade_erros}"
    f"({taxa_erro * 100})"
    )

print("-" * 50)

print(f"Taxa de erro teórica: 2.00%")
print(f"Taxa de erro simulada: {taxa_erro * 100:.2f}")
print(f"Diferença: {diferenca__erro * 100:.2f}")