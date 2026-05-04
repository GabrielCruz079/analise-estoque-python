import matplotlib.pyplot as plt

# Receita total
receita_total = df["valor_total"].sum()

# Receita por produto
receita_produto = df.groupby("produto")["valor_total"].sum().sort_values(ascending=False)

# Receita por categoria
receita_categoria = df.groupby("categoria")["valor_total"].sum()

# Top 5 produtos
top5 = receita_produto.head(5)

# Produtos com menor desempenho
bottom5 = receita_produto.tail(5)

print("\n💰 Receita total:", receita_total)
print("\n🏆 Top 5 produtos:")
print(top5)

print("\n⚠️ Produtos com menor receita:")
print(bottom5)
