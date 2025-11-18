import yfinance as yf
import pandas as pd
from datetime import datetime

print("--- INICIANDO ATUALIZAÇÃO DOS BANCOS (2010-2025) ---")

# --- CONFIGURAÇÃO ---
# 1. Tickers dos Bancos
tickers = ["ITUB4.SA", "BBDC4.SA"]

# 2. O nome EXATO que o seu notebook espera ler
output_file = "dados_bancos_itub_bbdc.csv" 
# --------------------

# Datas: do início até hoje
start_date = "2010-01-01"
end_date = datetime.today().strftime('%Y-%m-%d')

print(f"Baixando dados para {tickers}...")
print(f"Período: {start_date} até {end_date}")

try:
    # Baixar dados
    data = yf.download(tickers, start=start_date, end=end_date)
    
    # Pegar apenas o fechamento (Close) e remover falhas
    adj_close_data = data['Close'].dropna()
    
    # Salvar no arquivo correto
    adj_close_data.to_csv(output_file)
    
    print(f"\n--- SUCESSO! ---")
    print(f"Dados salvos em: '{output_file}'")
    print(f"Total de linhas: {len(adj_close_data)}")

except Exception as e:
    print(f"\n--- ERRO ---")
    print(f"Ocorreu um erro: {e}")