p_spam = 0.10
p_palavra_spam = 0.80
p_palavra_normal = 0.05
p_normal = 1 - p_spam
p_palavra = (p_palavra_spam * p_spam) + (p_palavra_normal * p_normal)
p_spam_dado_palavra = (p_palavra_spam * p_spam) / p_palavra

print("Resultado em Decimal:", p_spam_dado_palavra)

# Função genérica para calcular P(A|B) via Teorema de Bayes

def calcular_bayes(p_b_dado_a, p_a, p_b):
 """
 Calcula a probabilidade a posteriori P(A|B).
 p_b_dado_a: Verossimilhança P(B|A)
 p_a: Probabilidade a priori P(A)
 p_b: Probabilidade total da evidência P(B)
 """
 return (p_b_dado_a * p_a) / p_b

# Executando para o filtro de spam:

resultado = calcular_bayes(p_palavra_spam, p_spam, p_palavra)

print("Resultado via Função:", resultado) # Saída: 0.6