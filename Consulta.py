import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados.csv", sep=None, engine="python", encoding="latin1")

df.columns = ["produto", "quantidade", "preco", "custo"]

df["preco"] = (
    df["preco"]
    .astype(str)
    .str.replace("R$", "", regex=False)
    .str.replace(",", ".", regex=False)
    .str.strip()
)

df["preco"] = pd.to_numeric(df["preco"], errors="coerce")
print(df)

# gráfico
df.plot(x="produto", y="quantidade", kind="bar")
plt.title("Quantidade em Estoque")
plt.xlabel("Produto")
plt.ylabel("Quantidade")
