

def calculadora_bayesiana(p_a, p_b_dado_a, p_b_dado_nao_a):
 
 p_nao_a = 1 - p_a

 p_b = (p_b_dado_a * p_a) + (p_b_dado_nao_a * p_nao_a)

 p_a_dado_b = (p_b_dado_a * p_a) / p_b
 
 print("=== RELATÓRIO DE ATUALIZAÇÃO BAYESIANA ===")

 print(f"Probabilidade A Priori P(A) : {p_a:.4f} ({p_a*100:.2f}%)")

 print(f"Evidência Total P(B) : {p_b:.4f} ({p_b*100:.2f}%)")

 print(f"Probabilidade A Posteriori P(A|B): {p_a_dado_b:.4f} ({p_a_dado_b*100:.2f}%)")
 
# Testando com o caso de segurança do Exercício 6:
calculadora_bayesiana(p_a=0.02, p_b_dado_a=0.95, p_b_dado_nao_a=0.03)