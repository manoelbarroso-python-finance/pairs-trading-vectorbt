# Otimização de Pairs Trading (Long & Short) com VectorBT

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/manoelbarroso-python-finance/pairs-trading-vectorbt/blob/main/pairs_trading.ipynb)
[![NBViewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/manoelbarroso-python-finance/pairs-trading-vectorbt/blob/main/pairs_trading.ipynb)

## 🎯 Objetivo
Implementar e otimizar uma estratégia **Market-Neutral** (Arbitragem Estatística) na B3, utilizando validação econométrica rigorosa e backtesting vetorial em larga escala.

O projeto investiga a ineficiência de preços no setor elétrico (CMIG4 vs CPLE6) para capturar *Alpha* através da reversão à média dos resíduos (cointegração).

## 📊 Destaques da Análise

O estudo foi conduzido em 4 etapas principais (descritas no notebook):

1.  **Quebra de Paradigma:** Demonstração estatística de que o *Ratio Simples* (Preço A / Preço B) falha em pares clássicos como ITUB4/BBDC4.
2.  **Engle-Granger:** Implementação de Regressão Linear (OLS) para calcular o *Hedge Ratio* dinâmico e extrair os resíduos estacionários.
3.  **Otimização Vetorial:** Teste simultâneo de **119 combinações** de parâmetros (Janela Móvel vs. Z-Score) usando a biblioteca `vectorbt`.
4.  **Resultados (2010-2025):** A estratégia ótima demonstrou perfil "Sniper": baixa frequência de trades, alta assertividade e resiliência a crises (drawdowns recuperados).

## 🛠️ Tecnologias Utilizadas

* **VectorBT:** Engine de backtesting de alta performance.
* **Statsmodels:** Testes ADF (Estacionariedade) e Regressão OLS.
* **Pandas/Numpy:** Manipulação de dados de séries temporais.
* **Yfinance:** Coleta de dados ajustados da B3.

## 🚀 Como Executar este Projeto

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/manoelbarroso-python-finance/pairs-trading-vectorbt.git](https://github.com/manoelbarroso-python-finance/pairs-trading-vectorbt.git)
    ```
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Gere os dados atualizados (ETL):
    ```bash
    python get_data.py
    ```
    *Isso baixará os dados mais recentes da B3 e criará os arquivos CSV locais.*

4.  Abra e execute o Notebook:
    ```bash
    jupyter lab pairs_trading.ipynb
    ```

---
**Autor:** Manoel Barroso Marques
[LinkedIn](https://www.linkedin.com/in/manoel-barroso-marques-433174216/)

