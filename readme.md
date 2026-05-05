# 📦 Análise de Estoque com Python e Power BI

Projeto de análise de dados aplicado ao controle de estoque e desempenho financeiro de produtos, com foco em geração de insights e visualização interativa.

---

## 📌 Objetivo

Transformar dados brutos em informações estratégicas para apoiar a tomada de decisão, como:

* Receita total por produto
* Custo total
* Lucro unitário e total
* Identificação dos produtos mais rentáveis

---

## 🧠 Tecnologias utilizadas

* Python
* Pandas
* Matplotlib
* Power BI

---

## 📊 Estrutura dos dados

O dataset contém as seguintes colunas:

| Coluna     | Descrição             |
| ---------- | --------------------- |
| produto    | Nome do produto       |
| quantidade | Quantidade em estoque |
| preco      | Preço de venda        |
| custo      | Custo do produto      |

---

## ⚙️ Tratamento de dados

Durante o processo, foram realizados:

* Limpeza de dados (remoção de "R$", espaços e vírgulas)
* Conversão de valores para tipo numérico
* Padronização do dataset
* Preparação dos dados para visualização no Power BI

---

## 📈 Análises realizadas

* Cálculo do valor total:

```python
df["valor_total"] = df["quantidade"] * df["preco"]
```

* Cálculo do custo total:

```python
df["custo_total"] = df["quantidade"] * df["custo"]
```

* Cálculo do lucro:

```python
df["lucro"] = df["valor_total"] - df["custo_total"]
```

* Agrupamento por produto para análise consolidada

---

## 📉 Visualizações em Python

Gráficos exploratórios foram gerados com Matplotlib:

* Quantidade por produto
* Receita por produto
* Lucro por produto

---

## 📊 Dashboard no Power BI

Os dados tratados foram utilizados para criação de um dashboard interativo com:

* 📌 Receita total
* 📌 Lucro total
* 📌 Lucro por produto
* 📌 Ranking de produtos
* 📌 Filtros dinâmicos (segmentação)

O objetivo do dashboard é permitir análise rápida e visual do desempenho do estoque.

---

## ▶️ Como executar

1. Instale as dependências:

```bash
pip install pandas matplotlib
```

2. Execute o script:

```bash
python analise.py
```

3. Abra o Power BI e importe o arquivo de dados (`dados.csv`) para criar o dashboard.

---

## 🚀 Próximos passos

* Automatizar atualização dos dados
* Criar dashboard online
* Aplicar métricas mais avançadas (margem, giro de estoque)

---

## 👨‍💻 Autor

Gabriel Ramos Cruz
Foco em Análise de Dados e Inteligência Artificial

---

## 📌 Observação

Este projeto faz parte do meu portfólio prático, com foco em aplicações reais de análise de dados e visualização interativa para tomada de decisão.
