import pandas as pd
import numpy as np

np.random.seed(42)

produtos = ["Cimento", "Areia", "Tijolo", "Ferro", "Brita", "Cal", "Argamassa"]
categorias = ["Construção", "Estrutura", "Acabamento"]

n = 500  # volume de dados

df = pd.DataFrame({
    "produto": np.random.choice(produtos, n),
    "categoria": np.random.choice(categorias, n),
    "quantidade": np.random.randint(1, 200, n),
    "preco": np.round(np.random.uniform(5, 100, n), 2),
    "data": pd.date_range(start="2024-01-01", periods=n, freq="D")
})

df["valor_total"] = df["quantidade"] * df["preco"]

print(df.head())

# salvar CSV
df.to_csv("dados_grandes.csv", index=False)
