import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados.csv", sep=None, engine="python", encoding="latin1")

df.columns = ["produto", "quantidade", "preco"]

df["quantidade"] = df["quantidade"].astype(float)
df["preco"] = df["preco"].astype(float)

df["valor_total"] = df["quantidade"] * df["preco"]

print(df)

# gráfico
df.plot(x="produto", y="quantidade", kind="bar")
plt.title("Quantidade em Estoque")
plt.xlabel("Produto")
plt.ylabel("Quantidade")
plt.show()