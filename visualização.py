import pandas as pd
import matplotlib.pyplot as plt

# 📥 Ler CSV corretamente
df = pd.read_csv(
    "dados.csv",
    sep=";",              # separador correto
    skip_blank_lines=True
)

# Remover linhas inválidas
df = df[df["produto"].notna()]

# Limpar espaços
df["produto"] = df["produto"].str.strip()

# Converter quantidade
df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")

# Limpar preco
df["preco"] = (
    df["preco"]
    .astype(str)
    .str.replace("R$", "", regex=False)
    .str.replace(",", ".", regex=False)
    .str.strip()
)
df["preco"] = pd.to_numeric(df["preco"], errors="coerce")

# Limpar custo
df["custo"] = (
    df["custo"]
    .astype(str)
    .str.replace("R$", "", regex=False)
    .str.replace(",", ".", regex=False)
    .str.strip()
)
df["custo"] = pd.to_numeric(df["custo"], errors="coerce")

#  remover possíveis NaN
df = df.dropna()

#  Cálculos
df["faturamento"] = df["preco"] * df["quantidade"]
df["lucro_total"] = (df["preco"] - df["custo"]) * df["quantidade"]

#  Agrupar
agrupado = df.groupby("produto").agg({
    "faturamento": "sum",
    "lucro_total": "sum"
}).sort_values(by="lucro_total", ascending=False)

print("\nResumo por produto:")
print(agrupado)

#  Gráfico
agrupado.plot(kind="bar")

plt.title("Faturamento e Lucro por Produto")
plt.xlabel("Produto")
plt.ylabel("Valor")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
